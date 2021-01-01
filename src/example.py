import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("PyButton Module Example")

#Import PyButton:
import easy_button

mouse = [0, 0, False]
keys_down = []

#Function command for button:
def greeter():
    print("Hello World!")

#Define button objects:
button = easy_button.rect(margin = 5,
                       hover_margin = 10,
                       pos = (100, 100), #Tuple object — non-assignable
                       width = 150,
                       height = 75,
                       text = "Greet World Here",
                       font = "timesnewroman",
                       hover_border = 10,
                       hover_bc = (255, 255, 255),
                       command = greeter,
                       hover_bg = (255, 0, 255)
                       )
movable_button = easy_button.rect(
    pos = [400, 300], #List object — assingable
    width = 150,
    height = 25,
    text = "ARROW KEYS TO MOVE ME",
    hover_border = 0,
    hover_bg = (0, 0, 0)
    )

#Print PyButton version:
print("PyButton version", pybutton.__version__)
while True:
    screen.fill((0, 0, 0))
    #Function commands to draw and use button:
    button.draw(screen)
    button.hover((mouse[0], mouse[1]))
    button.click((mouse[0], mouse[1]), mouse[2])
    
    #Use button check_click method to put mouse up
    #if button is clicked to prevent button from
    #executing greet command multiple times:
    if(button.check_click((mouse[0], mouse[1]), mouse[2]) == True):
        mouse[2] = False

    #Function command to draw and use movable_button
    movable_button.draw(screen)
    movable_button.hover((mouse[0], mouse[1]))
    
    #If operations to modify movable_buton to
    #change its pos when arrow keys are pressed
    if("Ĕ" in keys_down): #Left
        movable_button.pos[0] = movable_button.pos[0] - 1
    if("ē" in keys_down): #Right
        movable_button.pos[0] = movable_button.pos[0] - 1
    if("Ē" in keys_down): #Down
        movable_button.pos[1] = movable_button.pos[1] - 1
    if("đ" in keys_down): #Up
        movable_button.pos[1] = movable_button.pos[1] - 1
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif(event.type == KEYDOWN):
            #print(chr(event.key))
            keys_down.append(chr(event.key))
        elif(event.type == KEYUP):
            if(chr(event.key) in keys_down):
                keys_down.remove(chr(event.key))
        elif(event.type == MOUSEMOTION):
            mouse = [event.pos[0], event.pos[1], mouse[2]]
        elif(event.type == MOUSEBUTTONDOWN):
            if(event.button == 1):
                mouse[2] = True
        elif(event.type == MOUSEBUTTONUP):
            if(event.button == 1):
                mouse[2] = False
    pygame.display.update()
