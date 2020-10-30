"""
Player Class
Author: Bryson Rogers
Functions: initialize, move , draw, kill, turn left, turn right, collision
"""

import pygame
import math
#import bullet

class Player():
    # loc for location and ori for orientation
    def __init__(self, x, y):
        self.radius = 10
        self.length = 16
        self.x = x
        self.y = y
        self.oriX = x
        self.oriY = y - 16
        self.oxp = 26
        self.oyp = 0
        self.vel = 3
        self.health = 10
        self.shoot = False
        self.angle = [-16,-16,-16,-15,-15,-15,-14,-14,-13,-13,-12,-12,-11,-10,-9,-9,-8,-8,-7,-6,-5,-4,-3,-2,-1, #0 - 25
            0,1,2,3,4,5,6,7,8,8,9,9,10,11,12,12,13,13,14,14,15,15,15,16,16,16, #26 - 51
            16,16,15,15,15,14,14,13,13,12,12,11,10,9,9,8,8,7,6,5,4,3,2,1,0, #52 - 76
            -1,-2,-3,-4,-5,-6,-7,-8,-8,-9,-9,-10,-11,-12,-12,-13,-13,-14,-14,-15,-15,-15,-16,-16, -16] # 77 - 100

    # Draw self
    def draw(self, surface):
        #print ("x ori = ", self.oriX, "y ori = ", self.oriY)
        if self.health != 0:
            pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)
            pygame.draw.line(surface, (255, 255, 255), (self.x, self.y), (self.oriX, self.oriY), 3)
    def clientDraw(self, surface, x, y):
        #print ("x ori = ", self.oriX, "y ori = ", self.oriY)
        oriX = x + self.angle[(self.oxp)]
        oriY = y + self.angle[(self.oyp)]
        if self.health != 0:
            pygame.draw.circle(surface, (255, 255, 255), (x, y), self.radius)
            pygame.draw.line(surface, (255, 255, 255), (x, y), (oriX, oriY), 3)


    # turn left and right cycle OriX and OriY through
    # 100 different preset values to avoid trying to draw half a pixel
    def turnLeft(self):
        if (self.oyp == 0):
            self.oyp = 100
            self.oxp = 25
        elif (self.oxp == 0):
            self.oxp = 100
            self.oyp = 74
        else:
            self.oyp -= 1
            self.oxp -= 1

        self.oriX = self.x + self.angle[(self.oxp)]
        self.oriY = self.y + self.angle[(self.oyp)]
       

    def turnRight(self):
        if (self.oyp == 100):
            self.oyp = 0
            self.oxp = 26
        elif (self.oxp == 100):
            self.oxp = 0
            self.oyp = 75
        else:
            self.oyp += 1
            self.oxp += 1
        
        self.oriX = self.x + self.angle[(self.oxp)]
        self.oriY = self.y + self.angle[(self.oyp)]

    # Adjust location
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel
            self.oriX -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel
            self.oriX += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel
            self.oriY -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel
            self.oriY += self.vel

        if keys[pygame.K_LEFT]:
            self.turnLeft()

        if keys[pygame.K_RIGHT]:
            self.turnRight()

        if keys[pygame.K_UP]:
            self.shoot = True
        else:
            self.shoot = False
    """
    # check for collisions
    def collision(self, enemies):
        for e in range(len(enemies)):
            if (math.sqrt((abs(self.x - enemies[e].x)**2) + abs(self.y - enemies[e].y)**2) < self.radius):
                return True"""
    # delete self
    def kill(self):
        del self