"""
This module implements a speech-bubble effect renderer
"""
from wcwidth.wcwidth import wcswidth
from asciimatics.renderers.base import StaticRenderer

class Card(StaticRenderer):
    """
    Renders supplied text into a card.
    """

    def __init__(self, text):
        """
        :param text: The text to be put on the card.
        """
        super().__init__()
        max_len = max(wcswidth(x) for x in text.split("\n"))
        hmargin = 5
        vmargin = 1

        # prepare vertical margins
        margin_lines = ""
        for x in range(vmargin):
            margin_lines += "|" + " "*hmargin + " "*max_len + " "*hmargin + "|\n"

        # draw the card
        card = "+" + "-"*hmargin + "-"*max_len + "-"*hmargin + "+\n"
        card += margin_lines
        for line in text.split("\n"):
            filler = " " * (max_len - len(line))
            card += "|" + " "*hmargin + line + filler + " "*hmargin + "|\n"
        card += margin_lines
        card += "+" + "-"*hmargin + "-"*max_len + "-"*hmargin + "+\n"

        self._images = [card]
