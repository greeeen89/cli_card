from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Cycle, Stars, Snow
from asciimatics.particles import StarFirework, SerpentFirework, PalmFirework, RingFirework
from asciimatics.renderers import FigletText, Fire
from random import randint, choice
from time import sleep

from card import Card

def run (screen):
    with open("card.txt","r") as file:
        card_text = file.read()
    card_renderer = Card(card_text)

    effects_intro = [
        Print(screen, FigletText("Happy Birthday"), (screen.height//2)-6, transparent=False),
        Print(screen, FigletText("Gabby!"), (screen.height//2)+1, transparent=False),
        Stars(screen, screen.width)
    ]

    # prepare fireworks
    for i in range(20):
        firework = choice([PalmFirework, StarFirework, RingFirework, SerpentFirework])
        effects_intro.append(
            firework(
                screen,
                randint(0, screen.width),
                randint(screen.height//8, (screen.height*3)//4),
                randint(20, 35),
                start_frame=randint(0,150)
            )
        )

    effects_card = [
        Snow(screen),
        #Stars(screen, 10),
        #Print(screen, Fire(20, 20, "", 0.5, 5, 5), 30),
        #RingExplosion(screen, 25, 20, 10),
        Print(screen, card_renderer, 6, transparent=False)
    ]
    
    intro = [Scene(effects_intro, 150)]
    scenes = [Scene(effects_card, 50, False)]

    screen.play(intro, repeat=False)
    screen.play(scenes)

Screen.wrapper(run)
