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
        self.jumpagain = True
        self.hurtfor = 0
        self.ishurt = False
        self.pressed = []
        self.prevright = False
        self.prevleft = False

    def update(self):
        # resets jumps and y velocity when the player is on the platform
        if self.pos[1] + self.yvel >= 480 and self.pos[0] > 160 and self.pos[0] < 1040:
            self.yvel = 0
            self.pos[1] = 480
            self.grounded = True
            self.jumps = 2
        # updates y-position and number of jumps if the player is not on the platform
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
            if self.pressed[K_d]:
                if (self.pressed[K_a] == False) or (self.prevleft):
                    if self.xvel < 10:
                        self.xvel = 10
            if self.pressed[K_a]:
                if (self.pressed[K_d] == False) or (self.prevright):
                    if self.xvel > -10:
                        self.xvel = -10
            if self.prevleft == False and self.prevright == False:
                self.xvel = 0               
        # movement options while in the air
        else:
            if self.pressed[K_d]:
                if (self.pressed[K_a] == False) or (self.prevleft):
                    if self.xvel < 12:
                        self.xvel += 2
            if self.pressed[K_a]:
                if (self.pressed[K_d] == False) or (self.prevright):
                    if self.xvel > -12:
                        self.xvel += -2

        # allows the player to use jumps
        if self.jumps == 2 and self.pressed[K_SPACE] and self.jumpagain:
            self.yvel += -15
            self.jumps = 1
            self.jumpagain = False
        elif self.jumps == 1 and self.pressed[K_SPACE] and self.jumpagain:
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
    """the game object that is controlled by Player 2"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player2.png")
        self.rect = self.image.get_rect()
        self.xvel = 0
        self.yvel = 0
        self.pos = [920, 480]
        self.grounded = True
        self.jumps = 2
        self.jumpagain = True
        self.hurtfor = 0
        self.ishurt = False
        self.pressed = []
        self.prevright = False
        self.prevleft = False

    def update(self):
        # resets jumps and y velocity when the player is on the platform
        if self.pos[1] + self.yvel >= 480 and self.pos[0] > 160 and self.pos[0] < 1040:
            self.yvel = 0
            self.pos[1] = 480
            self.grounded = True
            self.jumps = 2
        # updates y-position and number of jumps if the player is not on the platform
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
            if self.pressed[K_KP6]:
                if (self.pressed[K_KP4] == False) or (self.prevleft):
                    if self.xvel < 10:
                        self.xvel = 10
            if self.pressed[K_KP4]:
                if (self.pressed[K_KP6] == False) or (self.prevright):
                    if self.xvel > -10:
                        self.xvel = -10
            if self.prevleft == False and self.prevright == False:
                self.xvel = 0               
        # movement options while in the air
        else:
            if self.pressed[K_KP6]:
                if (self.pressed[K_KP4] == False) or (self.prevleft):
                    if self.xvel < 12:
                        self.xvel += 2
            if self.pressed[K_KP4]:
                if (self.pressed[K_KP6] == False) or (self.prevright):
                    if self.xvel > -12:
                        self.xvel += -2

        # allows the player to use jumps
        if self.jumps == 2 and self.pressed[K_KP_ENTER] and self.jumpagain:
            self.yvel += -15
            self.jumps = 1
            self.jumpagain = False
        elif self.jumps == 1 and self.pressed[K_KP_ENTER] and self.jumpagain:
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

class PlayerCPU(pygame.sprite.Sprite):
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

def mainmenu():
    # contains different game modes, instructions, and the ability to exit the application
    global option
    background = pygame.image.load("background.png").convert()
    biggerarialfont.render_to(background, (450,50), "MAIN MENU", fgcolor=(255,255,255), bgcolor=(120,120,120))
    biggerarialfont.render_to(background, (150,200), "(1) Player vs CPU (Arcade)", fgcolor=(255,255,255), bgcolor=(120,120,120))
    biggerarialfont.render_to(background, (150,300), "(2) Player vs Player (PVP)", fgcolor=(255,255,255), bgcolor=(120,120,120))
    biggerarialfont.render_to(background, (150,400), "(3) Instructions", fgcolor=(255,255,255), bgcolor=(120,120,120))
    biggerarialfont.render_to(background, (150,500), "(4) Exit", fgcolor=(255,255,255), bgcolor=(120,120,120))
    screen.blit(background, (0,0))
    pygame.display.flip()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_1 or event.key == K_KP1:
                    option = 1
                    running = False
                elif event.key == K_2 or event.key == K_KP2:
                    option = 2
                    running = False
                elif event.key == K_3 or event.key == K_KP3:
                    option = 3
                    running = False
                elif event.key == K_4 or event.key == K_KP4 or event.key == K_ESCAPE:
                    option = 4
                    running = False

def instructions():
    # explains the controls and the scoring system
    global option
    background = pygame.image.load("background.png").convert()
    biggerarialfont.render_to(background, (400,50), "INSTRUCTIONS", fgcolor=(255,255,255), bgcolor=(120,120,120))
    smallerarialfont.render_to(background, (350,300), "In Player vs CPU (Arcade), it is Game Over when the CPU reaches 5 points.", fgcolor=(255,255,255), bgcolor=(120,120,120))
    smallerarialfont.render_to(background, (350,350), "In Player vs Player (PVP), the first player to reach 10 points wins.", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (100,200), "Collide with your opponent while above them to gain points.", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (260,600), "(0) Main Menu", fgcolor=(255,255,255), bgcolor=(120,120,120))

    screen.blit(background, (0,0))
    pygame.display.flip()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    option = 4
                    running = False
                elif event.key == K_0 or event.key == K_KP0:
                    option = 0
                    running = False

def gameovercpu():
    # displays GAME OVER screen, allowing to restart match or go to main menu
    global option
    background = pygame.image.load("background.png").convert()
    biggerarialfont.render_to(background, (360,100), "GAME OVER", fgcolor=(255,255,255), bgcolor=(120,120,120))
    if player1points != 1:
        biggerarialfont.render_to(background, (260,200), "You scored " + str(player1points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
    else:
        biggerarialfont.render_to(background, (260,200), "You scored 1 point", fgcolor=(255,255,255), bgcolor=(120,120,120))

    arialfont.render_to(background, (260,450), "(R) Rematch", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (260,500), "(0) Main Menu", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (260,550), "(Esc) Quit", fgcolor=(255,255,255), bgcolor=(120,120,120))

    screen.blit(background, (0,0))
    pygame.display.flip()
    
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    option = 4
                    running = False
                elif event.key == K_0 or event.key == K_KP0:
                    option = 0
                    running = False
                elif event.key == K_r:
                    option = 1
                    running = False

def gameoverpvp():
    # displays GAME OVER screen, allowing to restart match or go to main menu
    global option
    background = pygame.image.load("background.png").convert()
    if player1points == 10:
        biggerarialfont.render_to(background, (300,100), "PLAYER 1 WINS", fgcolor=(255,255,255), bgcolor=(120,120,120))
    elif player2points == 10:
        biggerarialfont.render_to(background, (300,100), "PLAYER 2 WINS", fgcolor=(255,255,255), bgcolor=(120,120,120))
    if player1points != 1:
        arialfont.render_to(background, (250,300), "Player 1 scored " + str(player1points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
    else:
        arialfont.render_to(background, (250,300), "Player 1 scored 1 point", fgcolor=(255,255,255), bgcolor=(120,120,120))
    if player2points != 1:
        arialfont.render_to(background, (250,350), "Player 2 scored " + str(player2points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
    else:
        arialfont.render_to(background, (250,350), "Player 2 scored 1 point", fgcolor=(255,255,255), bgcolor=(120,120,120))

    arialfont.render_to(background, (260,450), "(R) Rematch", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (260,500), "(0) Main Menu", fgcolor=(255,255,255), bgcolor=(120,120,120))
    arialfont.render_to(background, (260,550), "(Esc) Quit", fgcolor=(255,255,255), bgcolor=(120,120,120))

    screen.blit(background, (0,0))
    pygame.display.flip()
    
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    option = 4
                    running = False
                elif event.key == K_0 or event.key == K_KP0:
                    option = 0
                    running = False
                elif event.key == K_r:
                    option = 2
                    running = False

def playervscpu():
    global option
    background = pygame.image.load("background.png").convert()
    player1 = Player1()
    player2 = PlayerCPU()
    global player1points
    global player2points
    player1points = 0
    player2points = 0
    platform1 = Platform1()
    thesprites = pygame.sprite.Group(player1, player2, platform1)
    running = True
    player1.pressed = pygame.key.get_pressed()

    while running:
        # 60 frames per second
        clock.tick(60)
        player1.pressed = pygame.key.get_pressed()

        if player1.pressed[K_a] and (player1.pressed[K_d] == False):
            player1.prevleft = True
        if player1.pressed[K_d] and (player1.pressed[K_a] == False):
            player1.prevright = True
        if player1.pressed[K_a] == False:
            player1.prevleft = False
        if player1.pressed[K_d] == False:
            player1.prevright = False

        if player1.pressed[K_SPACE] == False:
            player1.jumpagain = True
        
        player2.press = 0
        player2.unpress = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    option = 4
                    running = False

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
                    player1points += 1
                elif player1.pos[1] > player2.pos[1]:
                    player1.hurt()
                    player2points += 1

        # updates characters and display            
        thesprites.update()
        arialfont.render_to(background, (80,20), "Player 1 (Green): " + str(player1points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
        arialfont.render_to(background, (720,20), "CPU (Blue): " + str(player2points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
        screen.blit(background, (0,0))
        thesprites.draw(screen)
        pygame.display.flip()

        # ends the game when the CPU scores 5 points
        if player2points >= 5:
            running = False
            gameovercpu()

def playervsplayer():
    global option
    background = pygame.image.load("background.png").convert()
    player1 = Player1()
    player2 = Player2()
    global player1points
    global player2points
    player1points = 0
    player2points = 0
    platform1 = Platform1()
    thesprites = pygame.sprite.Group(player1, player2, platform1)
    running = True
    player1.pressed = pygame.key.get_pressed()

    while running:
        # 60 frames per second
        clock.tick(60)

        player1.pressed = pygame.key.get_pressed()
        player2.pressed = pygame.key.get_pressed()

        # player 1 specific movement
        if player1.pressed[K_a] and (player1.pressed[K_d] == False):
            player1.prevleft = True
        if player1.pressed[K_d] and (player1.pressed[K_a] == False):
            player1.prevright = True
        if player1.pressed[K_a] == False:
            player1.prevleft = False
        if player1.pressed[K_d] == False:
            player1.prevright = False

        if player1.pressed[K_SPACE] == False:
            player1.jumpagain = True

        # player 2 specific movement
        if player2.pressed[K_KP4] and (player2.pressed[K_KP6] == False):
            player2.prevleft = True
        if player2.pressed[K_KP6] and (player2.pressed[K_KP4] == False):
            player2.prevright = True
        if player2.pressed[K_KP4] == False:
            player2.prevleft = False
        if player2.pressed[K_KP6] == False:
            player2.prevright = False

        if player2.pressed[K_KP_ENTER] == False:
            player2.jumpagain = True
        
        for event in pygame.event.get():
            if event.type == QUIT:
                option = 4
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    option = 4
                    running = False

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
                    player1points += 1
                elif player1.pos[1] > player2.pos[1]:
                    player1.hurt()
                    player2points += 1

        # updates characters and display            
        thesprites.update()
        arialfont.render_to(background, (80,20), "Player 1 (Green): " + str(player1points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
        arialfont.render_to(background, (720,20), "Player 2 (Blue): " + str(player2points) + " points", fgcolor=(255,255,255), bgcolor=(120,120,120))
        screen.blit(background, (0,0))
        thesprites.draw(screen)
        pygame.display.flip()

        # ends the game when the either player scores 10 points
        if player1points >= 10 or player2points >= 10:
            running = False
            gameoverpvp()

pygame.init()
screensize = xsize, ysize
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Plat Battle")
arialfont = pygame.freetype.SysFont('Arial', 50)
biggerarialfont = pygame.freetype.SysFont('Arial', 100)
smallerarialfont = pygame.freetype.SysFont('Arial', 25)
player1points = 0
player2points = 0
option = 0
clock = pygame.time.Clock()
gamerunning = True

while gamerunning:
    if option == 0:
        mainmenu()
    elif option == 1:
        playervscpu()
    elif option == 2:
        playervsplayer()
    elif option == 3:
        instructions()
    elif option == 4:
        gamerunning = False
pygame.quit()