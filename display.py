from hands import *
from button import *

def display():
    screen.fill("#95a5a6")
    tiles.display()
    hand.display()
    for button in buttonGroup:
        button.draw()
    pygame.display.update()
    clock.tick(FPS)