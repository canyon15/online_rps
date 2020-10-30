import pygame
from network import Network
from player import *

width = 300
height = 300

black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
FPS = pygame.time.Clock()


    

def gameLoop():
    ip = input("Your servers IP address: ")
    game = True
    n = Network(ip)
    me = n.p

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        
        me.move()
        n.send(me)
        me = n.getP()
        print("x and y: ", me.x, me.y)


        surface.fill(black)
        me.clientDraw(surface, 150, 150)
        pygame.display.update()
        FPS.tick(30)

def main():
    gameLoop()

if __name__=="__main__":
    main()


