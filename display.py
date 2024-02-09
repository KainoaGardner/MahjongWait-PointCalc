from hands import *
from button import *
from tiles import *

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
    # else:
    #     tiles.notNaki()

    pygame.display.update()
    clock.tick(FPS)