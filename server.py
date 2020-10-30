import socket
from _thread import *
import pygame
from pygame.locals import *
from player import Player
#import bullet
#import enemy
import math
import pickle

pygame.font.init()

server = socket.gethostbyname(socket.gethostname())
print("Only give this to players you trust: " , server)
port = 5321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# for score board
myfont = pygame.font.SysFont('Comic Sans MS', 30)
# screen dimensions
height = 720
width = 1080
# set display surface
surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Server")
#preset colors
black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red
# for screen refresh rate
FPS = pygame.time.Clock()

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
player1 = Player(500,300)
player2 = Player(550,400)
players = [player1, player2]

def threaded_client(conn, player):
    conn.send(pickle.dumps(player))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            player = data

            if not data:
                print("Disconnected")
                break
            else:
                """
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                    """
                reply = player
                print("Received: ", data)
                print("Sending : ", reply)
                print("player x: ", player.x)
                print("player y: ", player.y)
                player1.x = player.x
                player1.y = player.y
                player1.oriX = player.oriX
                player1.oriY = player.oriY


            conn.send(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()
    
def acceptConnections(player):
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, player))
    #currentPlayer += 1

# a Round function so increasing 
# numbers of enemies come in waves.
def nextRound(Round, enemies): 
    r = 0               
    while (r < Round):
        xO = 1 + r * 5
        yO = -50 - r
        enemies.append(enemy.Enemy(xO, yO))
        xT = width + 50 + r
        yT = 1 + r * 5
        enemies.append(enemy.Enemy(xT, yT))
        xH = -50 - r
        yH = height - r * 5 
        enemies.append(enemy.Enemy(xH, yH))
        xF = width - r * 5
        yF =  height + 50 + r
        enemies.append(enemy.Enemy(xF, yF))
        r += 1



def gameLoop():
    
    start_new_thread(acceptConnections,(player1, ))
    #talk(player1)
    game = True
    #currentPlayer = 0
    #threading.Thread(target=acceptConnections, args=(player1,))
    # initialize first two enemies
    #enemyO = enemy.Enemy(-50, 50)
    #enemyT = enemy.Enemy(1000, 740)

  #  enemies = [enemyO, enemyT]

    # Variables for display
    Round = 1
    score = 0
    # List of bullet instances
  #  bullets = []

    while game:
        # variables to be drawn on display
        scoreTxt = myfont.render('Score: ', False, grey)
        scoreNum = myfont.render((str(score)) , False, grey)
        roundTxt = myfont.render('Round: ', False, grey)
        roundNum = myfont.render((str(Round)) , False, grey)
         # Collects user inputs and exit condition.
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # exit condition / X button in corner 
                game = False 




        #Draw Everything.
        surface.fill(black)
        surface.blit(scoreTxt,(5,5)) # Draw score
        surface.blit(scoreNum,(100,5))
        surface.blit(roundTxt,(5,55)) # Draw round
        surface.blit(roundNum,(100,55))
        player1.draw(surface)
        player2.draw(surface)
        pygame.display.update()
        FPS.tick(30)




def main():
    gameLoop()
    quit()
    exit()

if __name__=="__main__":
    main()