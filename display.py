from hands import *
from button import *
from tiles import *
from score import *

def display():
    screen.fill("#95a5a6")
    tiles.display()
    hand.display()
    for button in buttonGroup:
        button.draw()
    # if hand.callButton:
    for button in callButtonGroup:
        button.draw()
    hand.displayButtonShader()

    score.display()
    screen.blit(text, textRect)
    # else:
    #     tiles.notNaki()

    pygame.display.update()
    clock.tick(FPS)