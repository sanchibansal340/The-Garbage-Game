import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpg')

# title and icon
pygame.display.set_caption("The Garbage Game")
icon = pygame.image.load('recycling-bin.png')
pygame.display.set_icon(icon)

# dustbin
dustbinImg = pygame.image.load('green-dustbin.png')
dustbinX = 370
dustbinY = 450
dustbinX_change = 0

# Trash
garbage = [pygame.image.load('apple.png'), pygame.image.load('chemicals.png'),
         pygame.image.load('organic.png'), pygame.image.load('plastic.png'),
         pygame.image.load('plastic-bottle.png'), pygame.image.load('vegetable.png')]

trashImg = random.choice(garbage)
trashX = random.randint(0, 736)
trashY = 25
trashY_change = 3

# score
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


'''def lose(void):
    lost = font.render("You lost!!!", True, (255, 255, 255))'''


def dustbin(x, y):
    screen.blit(dustbinImg, (dustbinX, dustbinY))


def trash(x, y):
    screen.blit(trashImg, (trashX, trashY))


def isCollision(trashX, trashY, dustbinX, dustbinY, trashImg):
    distance = math.sqrt((math.pow(dustbinX - trashX, 2)) + (math.pow(dustbinY - trashY, 2)))
    if distance < 27:
        if trashImg == garbage[0] or trashImg == garbage[2] or trashImg == garbage[5]:
            return True
        else:
            return False
    else:
        return False


# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dustbinX_change = -5
        if event.key == pygame.K_RIGHT:
            dustbinX_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            dustbinX_change = 0

    dustbinX += dustbinX_change
    if dustbinX <= 0:
        dustbinX = 0
    elif dustbinX >= 676:
        dustbinX = 676

    trashY += trashY_change

    # collision
    collision = isCollision(trashX, trashY, dustbinX, dustbinY, trashImg)
    if collision:
        score_value += 1
        trashImg = random.choice(garbage)
        trashX = random.randint(0, 736)
        trashY = 25

    '''elif collision == False:
        lost = font.render("You lost!!!", True, (255, 255, 255))
        screen.blit(lost, (300, 300))'''

    dustbin(dustbinX, dustbinY)
    show_score(textX, textY)
    trash(trashX, trashY)
    pygame.display.update()
