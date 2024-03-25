import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import gfxdraw

pygame.init()

class Screen():
    w = 1000
    h = 800
    x = 0
    y = 0
    posx = 0
    lastTick = 0
    background = (0,0,0)

screen = Screen()

window = pygame.display.set_mode((screen.w,screen.h))

run = True

DrawBuffer = []

class Rectangle():
    x = 0
    y = 0
    w = 0
    h = 0
    color = (0,0,0)

    def __init__(self,x,y,w,h,color=(0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        DrawBuffer.insert(len(DrawBuffer),self)

class Image():
    x = 0
    y = 0
    w = 0
    h = 0
    rotation = 0
    image = None

    def __init__(self,x,y,image,w=None,h=None,rotation=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.rotation = rotation
        DrawBuffer.insert(len(DrawBuffer),self)
    

class Circle():
    x = 0
    y = 0
    r = 0
    color = (0,0,0)
    def __init__(self,x,y,r,color=color):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        DrawBuffer.insert(len(DrawBuffer),self)

class Player():
    x = 0
    y = 0
    team = 0
    heading = 0

    gun = None
    main = Circle(x,y,30,(0,0,0))
    def __init__(self,x,y,team,heading=0):
        self.x = x
        self.y = y
        self.team = team
        self.heading = heading

        TeamColor = (255,0,0)
        if team == 1:
            TeamColor = (0,0,255)
        
        self.main.color = TeamColor
        print(self.main)
    def __setattr__(self, __name: str, __value):
        if self.main != None:
            if __name == "x":
                self.main.x = __value
            elif __name == "y":
                self.main.y = __value
        

def Draw():
    window.fill(screen.background)
    for shape in DrawBuffer:
        if type(shape) == Rectangle:
            DrawRect = pygame.Rect(shape.x+screen.x,shape.y+screen.y,shape.w,shape.h)
            pygame.draw.rect(window,shape.color,DrawRect)
        elif type(shape) == Image:
            RenderedImage = shape.image
            if shape.w != None and shape.h != None:
                RenderedImage = pygame.transform.scale(shape.image,(shape.w,shape.h))
            else:
                RenderedImage = shape.image
            if shape.rotation != 0:
                RenderedImage = pygame.transform.rotate(RenderedImage,shape.rotation).convert_alpha()
            window.blit(RenderedImage,(shape.x+screen.x,shape.y+screen.y))
        elif type(shape) == Circle:
            gfxdraw.aacircle(window,shape.x+screen.x,shape.y+screen.y,shape.r,shape.color)
            gfxdraw.filled_circle(window,shape.x+screen.x,shape.y+screen.y,shape.r,shape.color)
    pygame.display.flip()

Background = Image(0,0,pygame.image.load("media/floortiles.png"),w=5000,h=5000)



# Map

Map_Top = Rectangle(55*3,112*3,403*3,38*3,color=(0,0,0))
Map_Bottom = Rectangle(55*3,337*3,403*3,38*3,color=(0,0,0))
Map_Right = Rectangle(422*3,112*3,36*3,263*3,color=(0,0,0))
Map_Left = Rectangle(55*3,112*3,36*3,263*3,color=(0,0,0))

#end map


screen.background = (255,0,0)

screen.lastTick = time.time()
Crosshair = Image(0,0,pygame.image.load("media/crosshair.png"),w=50,h=50)

DefaultPlayer = Player(350,350,0,heading=0)



def Tick():
    x,y = pygame.mouse.get_pos()
    Crosshair.x = x-25
    Crosshair.y = y-25

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    Tick()
    Draw()

pygame.quit()