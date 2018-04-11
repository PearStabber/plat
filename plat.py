import os, pygame, math, random, pygame.freetype
from pygame.locals import *

# xsize and ysize are the number of pixels in each direction of the game window
xsize = 1280
ysize = 720

# number of frames in between the CPU's inputs (increasing this value decreases the difficulty)
cpureaction = 9

# number of frames a player is hurt for before being vulnerable again
invulnerable = 30

class Player1(pygame.sprite.Sprite):
    """the game object that is controlled by Player 1"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player1.png")
        self.rect = self.image.get_rect()
        self.xvel = 0
        self.yvel = 0
        self.pos = [280, 480]
        self.grounded = True
        self.jumps = 2
        self.press = 0
        self.unpress = 0
        self.recentpress = 0
        self.recentunpress = 0
        self.rightheld = False
        self.leftheld = False
        self.hurtfor = 0
        self.ishurt = False
        self.points = 0

    def update(self):
        # updates if direction keys are being held
        if self.press == K_d:
            self.rightheld = True
        elif self.unpress == K_d:
            self.rightheld = False
        if self.press == K_a:
            self.leftheld = True
        elif self.unpress == K_a:
            self.leftheld = False

        # resets jumps and y velocity when the player is on the platform
        if self.pos[1] + self.yvel >= 480 and self.pos[0] > 160 and self.pos[0] < 1040:
            self.yvel = 0
            self.pos[1] = 480
            self.grounded = True
            self.jumps = 2
        # updates y-position and jumps if the player is not on the platform
        else:
            self.pos[1] = self.pos[1] + self.yvel
            self.grounded = False
            if self.jumps == 2:
                self.jumps = 1

        # respawns the player
        if self.pos[1] > 720:
            self.respawn()

        # vertical acceleration due to gravity
        if self.pos[1] < 480 or self.grounded == False:
            self.yvel += 1

        # movement options while grounded
        if self.grounded == True:
            if (self.rightheld == True and self.leftheld == False) or (self.rightheld == True and self.recentpress == K_d):
                if self.xvel < 10:
                    self.xvel = 10
            elif (self.leftheld == True and self.rightheld == False) or (self.leftheld == True and self.recentpress == K_a):
                if self.xvel > -10:
                    self.xvel = -10
            else:
                self.xvel = 0               
        # movement options while in the air
        else:
            if (self.rightheld == True and self.leftheld == False) or (self.rightheld == True and self.recentpress == K_d):
                if self.xvel < 12:
                    self.xvel += 2
            elif (self.leftheld == True and self.rightheld == False) or (self.leftheld == True and self.recentpress == K_a):
                if self.xvel > -12:
                    self.xvel += -2

        # allows the player to use jumps
        if self.jumps == 2 and self.press == K_SPACE:
            self.yvel += -15
            self.jumps = 1
        elif self.jumps == 1 and self.press == K_SPACE:
            if self.yvel < 0:
                self.yvel += -12
            else:
                self.yvel = -12
            self.jumps = 0

        # updates x position from velocity
        self.pos[0] = self.pos[0] + self.xvel
        self.rect.topleft = self.pos[0], self.pos[1]

    def hurt(self):
        # shows hurt version of self for a quarter of a second
        self.ishurt = True
        self.hurtfor = invulnerable
        self.image = pygame.image.load("player1hurt.png")
        self.rect = self.image.get_rect()

    def unhurt(self):
        # returns to normal version of self
        self.ishurt = False
        self.image = pygame.image.load("player1.png")
        self.rect = self.image.get_rect()

    def respawn(self):
        # respawns player above center of platform if they fell offscreen
        if self.pos[0] > 1200 or self.pos[0] < 0:
            self.pos = [600, 20]
        # respawns player above opposite side if it was onscreen
        else:
            self.pos = [1200 - self.pos[0], 20]
        self.rect.topleft = self.pos[0], self.pos[1]
        self.yvel = 0
        self.xvel = 0
        self.jumps = 1
            
class Player2(pygame.sprite.Sprite):
    """the game object that is controlled by the CPU"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player2.png")
        self.rect = self.image.get_rect()
        self.xvel = 0
        self.yvel = 0
        self.pos = [920, 480]
        self.grounded = True
        self.jumps = 2
        self.press = 0
        self.unpress = 0
        self.recentpress = 0
        self.recentunpress = 0
        self.rightheld = False
        self.leftheld = False
        self.hurtfor = 0
        self.ishurt = False
        self.points = 0
        self.reaction = cpureaction

    def update(self):
        # updates if direction keys are being held
        if self.press == K_d:
            self.rightheld = True
        elif self.unpress == K_d:
            self.rightheld = False
        if self.press == K_a:
            self.leftheld = True
        elif self.unpress == K_a:
            self.leftheld = False

        # resets jumps and y velocity when the player is on the platform
        if self.pos[1] + self.yvel >= 480 and self.pos[0] > 160 and self.pos[0] < 1040:
            self.yvel = 0
            self.pos[1] = 480
            self.grounded = True
            self.jumps = 2
        # updates y-position and jumps if the player is not on the platform
        else:
            self.pos[1] = self.pos[1] + self.yvel
            self.grounded = False
            if self.jumps == 2:
                self.jumps = 1

        # respawns the player
        if self.pos[1] > 720:
            self.respawn()

        # vertical acceleration due to gravity
        if self.pos[1] < 480 or self.grounded == False:
            self.yvel += 1

        # movement options while grounded
        if self.grounded == True:
            if (self.rightheld == True and self.leftheld == False) or (self.rightheld == True and self.recentpress == K_d):
                if self.xvel < 10:
                    self.xvel = 10
            elif (self.leftheld == True and self.rightheld == False) or (self.leftheld == True and self.recentpress == K_a):
                if self.xvel > -10:
                    self.xvel = -10
            else:
                self.xvel = 0               
        # movement options while in the air
        else:
            if (self.rightheld == True and self.leftheld == False) or (self.rightheld == True and self.recentpress == K_d):
                if self.xvel < 12:
                    self.xvel += 2
            elif (self.leftheld == True and self.rightheld == False) or (self.leftheld == True and self.recentpress == K_a):
                if self.xvel > -12:
                    self.xvel += -2

        # allows the player to use jumps
        if self.jumps == 2 and self.press == K_SPACE:
            self.yvel += -15
            self.jumps = 1
        elif self.jumps == 1 and self.press == K_SPACE:
            if self.yvel < 0:
                self.yvel += -12
            else:
                self.yvel = -12
            self.jumps = 0

        # updates x position from velocity
        self.pos[0] = self.pos[0] + self.xvel
        self.rect.topleft = self.pos[0], self.pos[1]

    def hurt(self):
        # shows hurt version of self for a quarter of a second
        self.ishurt = True
        self.hurtfor = invulnerable
        self.image = pygame.image.load("player2hurt.png")
        self.rect = self.image.get_rect()
    
    def unhurt(self):
        # returns to normal version of self
        self.ishurt = False
        self.image = pygame.image.load("player2.png")
        self.rect = self.image.get_rect()

    def respawn(self):
        # respawns player above center of platform if they fell offscreen
        if self.pos[0] > 1200 or self.pos[0] < 0:
            self.pos = [600, 20]
        # respawns player above opposite side if it was onscreen
        else:
            self.pos = [1200 - self.pos[0], 20]
        self.rect.topleft = self.pos[0], self.pos[1]
        self.yvel = 0
        self.xvel = 0
        self.jumps = 1

class Platform1(pygame.sprite.Sprite):
    """a platform the game takes place on"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("platform1.png")
        self.rect = self.image.get_rect()
        self.pos = [240, 560]
        self.rect.topleft = self.pos[0], self.pos[1]

    def update(self):
        self.rect.topleft = self.pos[0], self.pos[1]

pygame.init()
screensize = xsize, ysize
screen = pygame.display.set_mode(screensize)
background = pygame.image.load("background.png").convert()
pygame.display.set_caption("Plat Battle")
arialfont = pygame.freetype.SysFont('Arial', 50)
biggerarialfont = pygame.freetype.SysFont('Arial', 100)
smallerarialfont = pygame.freetype.SysFont('Arial', 25)
player1 = Player1()
player2 = Player2()
platform1 = Platform1()
thesprites = pygame.sprite.Group(player1, player2, platform1)
clock = pygame.time.Clock()
running = True

while running:
    # 60 frames per second
    clock.tick(60)
    player1.press = 0
    player1.unpress = 0
    player2.press = 0
    player2.unpress = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            player1.press = event.key
            if event.key == K_a or event.key == K_d:
                player1.recentpress = event.key
        elif event.type == KEYUP:
            player1.unpress = event.key
            player1.recentunpress = event.key

    # START OF CPU CALCULATIONS
    # if the CPU is ready for its next move it will unpress the direction
    if player2.reaction <= 0:
        if player2.press == K_a:
            player2.unpress = K_a
        elif player2.press == K_d:
            player2.unpress = K_d
    # ticks down time before CPU can make its next move
    if player2.reaction > 0:
        player2.reaction += -1
    # if the CPU can react and is offstage, what does it do?
    elif player2.pos[1] > 480 and player2.jumps > 0:
        player2.press = K_SPACE
        player2.reaction = cpureaction
    elif player2.pos[0] <= 160:
        player2.press = K_d
        player2.recentpress = K_d
        player2.reaction = cpureaction
    elif player2.pos[0] >= 1040:
        player2.press = K_a
        player2.recentpress = K_a
        player2.reaction = cpureaction
    # if the CPU can react and is on the stage, what does it do?
    else:
        randmove = random.randint(0, 99)
        if randmove > 49:
            jumpat = random.randint(0,9)
            # if the CPU is below Player 1, it has a chance of jumping or moving towards them
            if player1.pos[1] < player2.pos[1] and jumpat > 6:
                player2.press = K_SPACE
                player2.reaction = cpureaction
            elif player1.pos[0] > player2.pos[0]:
                player2.press = K_d
                player2.recentpress = K_d
                player2.reaction = cpureaction
            else:
                player2.press = K_a
                player2.recentpress = K_a
                player2.reaction = cpureaction
        # the CPU will sometimes move in the opposite direction to throw you off
        elif randmove > 29:
            if player1.pos[0] > player2.pos[0]:
                player2.press = K_a
                player2.recentpress = K_a
                player2.reaction = cpureaction
            else:
                player2.press = K_d
                player2.recentpress = K_d
                player2.reaction =cpureaction
        # or randomly jump
        else:
            player2.press = K_SPACE
            player2.reaction = cpureaction
    # END OF CPU CALCULATIONS

    # updates hurt players
    if player1.ishurt == True:
        player1.hurtfor += -1
        if player1.hurtfor <= 0:
            player1.unhurt()
    if player2.ishurt == True:
        player2.hurtfor += -1
        if player2.hurtfor <= 0:
            player2.unhurt()

    # updates players being hurt
    if player1.ishurt == False and player2.ishurt == False:
        if (abs(player1.pos[0] - player2.pos[0]) < 80) and (abs(player1.pos[1] - player2.pos[1]) < 80):
            if player1.pos[1] < player2.pos[1]:
                player2.hurt()
                player1.points += 1
            elif player1.pos[1] > player2.pos[1]:
                player1.hurt()
                player2.points += 1

    # updates characters and display            
    thesprites.update()
    arialfont.render_to(background, (80,20), "Player 1 (Green): " + str(player1.points) + " points", fgcolor=(255,255,255), bgcolor=(30,30,30))
    arialfont.render_to(background, (720,20), "Player 2 (Purple): " + str(player2.points) + " points", fgcolor=(255,255,255), bgcolor=(30,30,30))
    smallerarialfont.render_to(background, (450,70), "(Game Over when Player 2 reaches 5 Points)", fgcolor=(255,255,255), bgcolor=(30,30,30))
    screen.blit(background, (0,0))
    thesprites.draw(screen)
    pygame.display.flip()

    # ends the game when the CPU scores 5 points
    if player2.points >= 5:
        running = False

#displays GAME OVER screen
biggerarialfont.render_to(background, (360,300), "GAME OVER", fgcolor=(255,255,255), bgcolor=(30,30,30))
if player1.points > 1 or player1.points == 0:
    biggerarialfont.render_to(background, (260,400), "You scored " + str(player1.points) + " points", fgcolor=(255,255,255), bgcolor=(30,30,30))
else:
    biggerarialfont.render_to(background, (260,400), "You scored 1 point", fgcolor=(255,255,255), bgcolor=(30,30,30))
screen.blit(background, (0,0))
pygame.display.flip()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
pygame.quit()