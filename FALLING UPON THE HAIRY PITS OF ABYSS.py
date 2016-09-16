#######Sprite Sheet Image Example Start#############

import pygame, sys
import pygame, math
from pygame.locals import *
from random import randrange
#initialize pygame
pygame.init()


m1 = pygame.mixer.Sound('morgan1.ogg')
m2 = pygame.mixer.Sound('morgan2.ogg')
m3 = pygame.mixer.Sound('morgan3.ogg')
m4 = pygame.mixer.Sound('morgan4.ogg')
m5 = pygame.mixer.Sound('morgan5.ogg')
m6 = pygame.mixer.Sound('morgan6.ogg')
m7 = pygame.mixer.Sound('morgan7.ogg')

song1 = pygame.mixer.Sound('pulloff.ogg')
song2 = pygame.mixer.Sound('dontstop.ogg')
song3 = pygame.mixer.Sound('01 Ultralight Beam.ogg')
song4 = pygame.mixer.Sound('cottoneyejoe.ogg')
song5 = pygame.mixer.Sound('fresh.ogg')
song6 = pygame.mixer.Sound('never.ogg')
song7 = pygame.mixer.Sound('bod.ogg')


mo0 = pygame.mixer.Sound('m0.ogg')
mo1 = pygame.mixer.Sound('m1.ogg')
mo2 = pygame.mixer.Sound('m2.ogg')
mo3 = pygame.mixer.Sound('m3.ogg')
mo4 = pygame.mixer.Sound('m4.ogg')
mo5 = pygame.mixer.Sound('m5.ogg')
mo6 = pygame.mixer.Sound('m6.ogg')


mon = mo0

nobody = pygame.mixer.Sound('span.ogg')

biggy = pygame.mixer.Sound('relationss.ogg')


yosh = pygame.mixer.Sound('yoshi.ogg')

playday = song1
playday.play()

oh = pygame.mixer.Sound('bluer.ogg')

#####################################
class SpriteSheetImage(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    #X property
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)

    #Y property
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
        

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

#############################################
wid = 1000
hei = 800
screen = pygame.display.set_mode((wid,hei))
pygame.display.set_caption("JUMBOS LOVELY FANTASY TIME")
##############################################

#####################
#TOASTA#

toaster = pygame.sprite.Group()
toasto = 50, 500
toast = SpriteSheetImage(screen)
toast.load("toaster.png",300,200,1) #hashtag
toast.position = toasto
toaster.add(toast)

####STAY INSIDE ER####
boxer = pygame.sprite.Group()
boxo = 350, 500
box = SpriteSheetImage(screen)
box.load("black box.png",10,200,1) #hashtag
box.position = boxo
boxer.add(toast)
###############


yer = 600

rogord = SpriteSheetImage(screen)
rogord.load("waffsp.png",100,100,5) #hashtag
rogordo = 100,yer - 10
rogord.position = rogordo
undies = pygame.sprite.Group()
undies.add(rogord)
rogord.first_frame = 0
rogord.last_frame = 0

yodel = yer + 30

rollero = wid,yodel
roller = SpriteSheetImage(screen)
roller.load("sausageroll.png",74,80,5) #hashtag
roller.position = rollero
funkybunch = pygame.sprite.Group()
funkybunch.add(roller)
roller.first_frame = 0
roller.last_frame = 4

###BASIC ENEMIES WITH LOOKS THAT KILL (LIKE ME)###
roller1o = wid + 255, yodel
roller1 = SpriteSheetImage(screen)
roller1.load("sausageroll.png",74,80,5) #hashtag
roller1.position = roller1o
funkybunch.add(roller1)
roller1.first_frame = 0
roller1.last_frame = 4

roller2o = wid + 750, yodel
roller2 = SpriteSheetImage(screen)
roller2.load("sausageroll.png",74,80,5) #hashtag
roller2.position = roller2o
funkybunch.add(roller2)
roller2.first_frame = 0
roller2.last_frame = 4

eggberto = 200, yodel
eggbert = SpriteSheetImage(screen)
eggbert.load("egger.png",89,97,1) #hashtag
eggbert.position = eggberto
funkybunch.add(eggbert)

eggbeardo = 675, yodel
eggbeard = SpriteSheetImage(screen)
eggbeard.load("egger.png",89,97,1) #hashtag
eggbeard.position = eggbeardo
funkybunch.add(eggbeard)


jerkyjerk = pygame.sprite.Group()
puddleo = 260, yodel + 45
puddle = SpriteSheetImage(screen)
puddle.load("syrup puddle.png",425,60,1) #hashtag
puddle.position = puddleo
jerkyjerk.add(puddle)

yoshio = -300, yer - 25
yoshi = SpriteSheetImage(screen)
yoshi.load("yoshi.png",150,100,4) #hashtag
yoshi.position = yoshio
funkybunch.add(yoshi)

pano = randrange(0, wid - 100), -250
pan = SpriteSheetImage(screen)
pan.load("pancake.png",210,160,1) #hashtag
pan.position = pano
funkybunch.add(pan)

pan1o = randrange(0, wid - 100), -250
pan1 = SpriteSheetImage(screen)
pan1.load("pancake.png",210,160,1) #hashtag
pan1.position = pano
funkybunch.add(pan1)
###################



####MENU####
menu = pygame.sprite.Group()
meno = 0, 0
men = SpriteSheetImage(screen)
men.load("start.png",wid,hei,2) #hashtag
men.position = meno
menu.add(men)

men.first_frame = 0
men.last_frame = 0
men.frame = 0
###########




###############################################


#BACON#
roy = 300
bacon = pygame.sprite.Group()
ropeyo = 200, roy
ropey = SpriteSheetImage(screen)
ropey.load("baconfull.png",600,299,3) #hashtag
ropey.position = ropeyo
bacon.add(ropey)

#ENEMIES THAT DONT KILL BUT GOOD TO LOOK AT#



joy = 127
syrpro = 255,joy
syrpr = SpriteSheetImage(screen)
syrpr.load("syrPour.png",425,600,2) #hashtag
syrpr.position = syrpro
bacon.add(syrpr)
#######

##############
#DAT BUTTA DO#

canyoubelieve = pygame.sprite.Group()
butto = 300, yodel + 30
butt = SpriteSheetImage(screen)
butt.load("butter.png",100,55,1) #hashtag
butt.position = butto
canyoubelieve.add(butt)

butt1o = 550, yodel + 30
butt1 = SpriteSheetImage(screen)
butt1.load("butter.png",100,55,1) #hashtag
butt1.position = butt1o
canyoubelieve.add(butt1)






#################
#BACKGROUND#
backy = pygame.sprite.Group()
backo = 0,0
back = SpriteSheetImage(screen)
back.load("background.png",wid,hei,1) #hashtag
back.position = backo
backy.add(back)
back.first_frame = 0
back.last_frame = 0
back.frame = 0

##back2 = SpriteSheetImage(screen)
##back2.load("back2.png",wid,hei,1) #hashtag
##back2.position = backo
##backy.add(back2)


##########
####EASTER TIME####
easter = pygame.sprite.Group()
billo = 0,0
bill = SpriteSheetImage(screen)
bill.load("bigbill.png",wid,591,1) #hashtag
bill.position = billo
easter.add(bill)

spanisho = 250,0
spanish = SpriteSheetImage(screen)
spanish.load("expectations.png",480,357,1) #you know what to do here
spanish.position = spanisho
easter.add(spanish)

ricko = 450,400
rick = SpriteSheetImage(screen)
rick.load("ricky.png",158,131,5) #you know what to do here
rick.position = spanisho
easter.add(rick)


bill.Y = 10000
spanish.Y = 10000
rick.Y = 10000

################

# Define some colors
WHITE = ( 255, 255, 255)
BLACK = (0,0,0)
RED = ( 255, 0, 0)
red = (255,0,0)
angels = (255,100,100)
green = (0,255,0)
blue = (0,0,255)
pandaman = (0,0, 160)
jumbo = (255,255,255)
darkgray = (100,100,100)
gray = (152,152,152)
lightgray = (200,200,200)
black = (0,0,0)
janesh = (47,47,47)
flippidyflop = (125,125,255)
fergaderk = (75,200,200)
#


#TEXTY TEXT MESSAGES#
jswift = pygame.font.Font(None,25)
dd = jswift.render("",True, black)
cc = jswift.render("",True, angels)
bb = jswift.render("",True, angels)
####

##SQUARES FOR ATTATCHING TO THEM BACON TREES##
class Square(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((height,width)) #size of square
        self.image = self.image.convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = randrange(1,10)
#how to change all squares     
    def update(self):
        self.rect.centerx = self.rect.centerx
        self.rect.centery = self.rect.centery + self.dy
        
        if self.rect.centery > hei:
            self.dy = 0 - self.dy
        
        if self.rect.centery <0:
            self.dy = 0 - self.dy

leftpancake = pygame.sprite.Group()

muchsquare = Square(WHITE,100,200)
muchsquare.rect.centerx = 275
muchsquare.rect.centery = 500
leftpancake.add(muchsquare) #adds to group


rightpancake = pygame.sprite.Group()

muchsquare1 = Square(WHITE,100,200)
muchsquare1.rect.centerx = 700
muchsquare1.rect.centery = 500
rightpancake.add(muchsquare1)


####################################


tango = 10
xs = 0
ys = 0
clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()
markymark = randrange(0,10)
jump = False
dude = 1.0
roomie = 0
roomer = True
johnny = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

roges = 2
dying = False
atat = False
rer = True
sooper = False
hard = False
impos = False

succulentx = -8
aa = jswift.render(" ",True, angels)

yoko = 5
ysp = 0

hi = 0

#markymark = funkybunch

while True:
    leftpancake.draw(screen)
    rightpancake.draw(screen)

    backy.update(ticks,10)
    backy.draw(screen)

    easter.update(ticks,10)
    easter.draw(screen)

    
        
    
    if dying == True:
        back.first_frame = 1
        back.last_frame = 1
        back.frame = 1
        
    else:
        back.first_frame = 0
        back.last_frame = 0
        back.frame = 0
        
        

    
    
##    rogord.Y = rogord.Y + ysp
    
    #GROUP DECLARATIONS#
    
##    pygame.draw.line(screen,red,(0,hei - 40), (wid,hei - 40),100)
    

    bacon.update(ticks,50)
    bacon.draw(screen)
    
    
    jerkyjerk.update(ticks,10)
    jerkyjerk.draw(screen)
    
    
    

    canyoubelieve.update(ticks,10)
    canyoubelieve.draw(screen)

    
    
    undies.update(ticks,10)
    undies.draw(screen)

    funkybunch.update(ticks,10)
    funkybunch.draw(screen)

    toaster.update(ticks,10)
    toaster.draw(screen)

    boxer.update(ticks,10)
    boxer.draw(screen)

    menu.update(ticks,10)
    menu.draw(screen)

    if(hard == True and roomie > 0):
        yoshi.X = yoshi.X + 6
        if(yoshi.X > wid):
            yoshi.position = yoshio
        if(yoshi.X % 150 == 0):
            yosh.play()

    if(impos == True and roomie > 0):
        pan.Y = pan.Y + 10
        pan1.Y = pan1.Y + 7
        if(pan.Y > hei):
            pan.Y = -175
            pan.X = randrange(0,wid - 100)
        if(pan1.Y > hei):
            pan1.Y = -175
            pan1.X = randrange(0,wid - 100)
    
    if( hi < roomie):
        hi = roomie
    #  #

    if (rogord.Y == yer):
        atat = False
        rer = True
    
    if(roges <0):
        screen.fill(BLACK)
        rogord.Y = 1000

    ##TEXTY TEXT##
    screen.blit(dd, (25,25))
    screen.blit(cc, (25,75))
    screen.blit(bb, (25,125))
    screen.blit(aa, (25,175))

    if(men.frame == 5):
        dd = jswift.render("SCORE: " + str(roomie),True, WHITE)
        cc = jswift.render("Lives: " + str(roges),True, angels)
        bb = jswift.render("",True,WHITE)
        aa = jswift.render(" ",True, WHITE)
    if(roomie == 0 and men.frame == 5):
        bb = jswift.render("ESCAPE THE FORCEFIELD OF THE TOASTER (JUMP)",True,WHITE)
    if(roomie == 29):
        bb = jswift.render("LAST LEVEL RIGHT HERE",True,WHITE)
    if(roomie == 30):
        bb = jswift.render("I LIED...",True,WHITE)
    
    if(roges < 0):
        bb = jswift.render("YOU DEAD",True,WHITE)
        aa = jswift.render("Press G to reset",True, WHITE)
        dd = jswift.render("SCORE: " + str(roomie),True, WHITE)
        cc = jswift.render("HIGH SCORE: " + str(hi),True, angels)
    ##  ##

    #######################################
    #randomness of holy roller sausages
    if(roomer == True):
        a = randrange(0,2)
        if(a == 1):
            roller.position = rollero
        else:
            roller.Y = 10000
        b = randrange(0,3)
        if(b == 1):
            roller1.position = roller1o
        else:
            roller1.Y = 10000
        c = randrange(0,3)
        if(c == 1):
            roller2.position = roller2o
        else:
            roller2.Y = 10000
        d = randrange(0,3)
        if(d == 1):
            eggbert.position = eggberto
        else:
            eggbert.Y = 10000
        e = randrange(0,2)
        if(e == 1):
            eggbeard.position = eggbeardo
        else:
            eggbeard.Y = 10000
        f = randrange(0,2)
        if(roomie == 17 or roomie == 21):
            f = 0
        if(f == 1):
            syrpr.position = syrpro
            puddle.position = puddleo
            e = randrange(0,2)
            if(e == 0):
                ropey.position = ropeyo
                butt.Y = 14010
                butt1.Y = 10000
            else:
                ropey.Y = 10000
                butt.position = butto
                butt1.position = butt1o
        else:
            syrpr.Y = 10000
            puddle.Y = 10000
            ropey.Y = 10000
            butt.Y = 14010
            butt1.Y = 10000
        yoshi.position = yoshio
        pan.Y = -250
        pan.X = randrange(0,wid - 100)
        pan1.Y = -250
        pan1.X = randrange(0,wid - 100)
        if(roomie == 17):
            bill.position = billo
            biggy.play()
        elif(roomie == 21):
            nobody.play()
            spanish.position = spanisho
        elif(roomie == 30):
            rick.position = ricko
            playday.stop()
            playday = song6
            playday.play()
        else:
            spanish.Y = 10000
            bill.Y = 10000
            rick.Y = 10000

        if(randrange(0,3) == 2):
            i = randrange(0,6)
            if(i == 0):
                mon = mo0
            if(i == 1):
                mon = mo1
            if(i == 2):
                mon = mo2
            if(i == 3):
                mon = mo3
            if(i == 4):
                mon = mo4
            if(i == 5):
                mon = mo5
            if(i == 6):
                mon = mo6
            mon.play()
            
        
    roller.X = roller.X + succulentx
    roller1.X = roller1.X + succulentx
    roller2.X = roller2.X + succulentx

    if(roller.X < -90):
        roller.X = wid + 10
    if(roller1.X < -90):
        roller1.X = wid + 10
    if(roller2.X < -90):
        roller2.X = wid + 10
    #####################################

    ##########################################
    #ROGORD CONTROLS
    if johnny == 0:
        rogord.X = rogord.X + xs
    if(rogord.X < -10):
        rogord.X = -10
    elif(rogord.X > wid - 75):
        roomie = roomie + 1
        roomer = True
        rogord.X = -10
    else:
        roomer = False

    ##JUMPING TIME##
    if johnny == 0:
        if jump == True:
            if(atat == True):
                atat = False
                while(rogord.Y < int((dude * dude * 32 - 300 * dude) / 2.5)):
                    dude = dude + .3
            if(dude < 10):
                rogord.Y = int((dude * dude * 32 - 300 * dude) / 2.5) + yer
                dude = dude + .3
            if(dude >= 10):
                rogord.Y = yer
                dude = 1
                jump = False

        

    #############################################

            
    #COLLISION

    asfd = pygame.sprite.groupcollide(jerkyjerk,undies,False,False).keys() #sausage + eggs
    for serfgt in asfd:
            dying = True

    fergyee = pygame.sprite.groupcollide(canyoubelieve,undies,False,False).keys() #sausage + eggs
    for fdssd in fergyee:
            if(sooper == False):
                dying = False
    
    woh = pygame.sprite.groupcollide(undies,funkybunch,False,False).keys() #sausage + eggs
    for sdfkla in woh:
            if(rogord.X < wid - 100) and (rogord.X > 5):
                dying = True
                sooper = True

    ttt = pygame.sprite.groupcollide(undies,boxer,False,False).keys() #sausage + eggs
    for tt in ttt:
            if (rogord.X <  box.X):
                rogord.X = rogord.X - 10
            if (rogord.X > box.X - 10):
                rogord.X = rogord.X + 10
            

    
    
    loveme = pygame.sprite.groupcollide(undies,leftpancake,False,False).keys()
    for fdklsa in loveme :
        if(rer == True):
            if(ropey.frame < 3 or ropey.frame > 14):
                if(f == 1 and e == 0):
                    atat = True
                    jump = False
                    rer = False
    loveme = pygame.sprite.groupcollide(undies,rightpancake,False,False).keys()
    for fdklsa in loveme :
        if(rer == True):
            if(ropey.frame > 6 or ropey.frame < 10):
                if(f == 1 and e == 0):
                    atat = True
                    jump = False
                    rer = False
    if(roomie == 0):                
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        
        roller.Y = 10000
    
        roller1.Y = 10000
    
        roller2.Y = 10000
    
        eggbert.Y = 10000
    
        eggbeard.Y = 10000
    
        syrpr.Y = 10000
        puddle.Y = 10000
        ropey.Y = 10000
        butt.Y = 14010
        butt1.Y = 10000
        toast.position = toasto
        box.position = boxo
    else:
        toast.Y = 12100
        box.Y = 16545

    if(roomie == 30):                
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        
        roller.Y = 10000
    
        roller1.Y = 10000
    
        roller2.Y = 10000
    
        eggbert.Y = 10000
    
        eggbeard.Y = 10000
    
        syrpr.Y = 10000
        puddle.Y = 10000
        ropey.Y = 10000
        butt.Y = 14010
        butt1.Y = 10000
        
    

    ####################################DEATH
    jumbotron = randrange(0,6)

##    if atat == True:
##        dying = False
    if dying == True and johnny == 0:
        mon.stop()
        roges = roges - 1
        if(roges >= 0):
            if(jumbotron == 0):
                m1.play()
            if(jumbotron == 1):
                m2.play()
            if(jumbotron == 2):
                m3.play()
            if(jumbotron == 3):
                m4.play()
            if(jumbotron == 4):
                m5.play()
            if(jumbotron == 5):
                m6.play()
            if(jumbotron == 6):
                m7.play()
        if(roges < 0):
            oh.play()
            
    if dying == True:
        johnny = johnny + 1
        tango = 0
        rogord.frame = 0
        rogord.Y = yer
        jump = False
        

    if johnny == 150:
        dying = False
        
        rogord.X = -10
        tango = 10
        johnny = 0
        sooper = False
        pan.X = randrange(0,wid - 100)
        pan1.Y = -200
        pan1.X = randrange(0,wid - 100)
        pan.Y = -200
        yoshi.position = yoshio
        if(a == 1):
            roller.position = rollero
        else:
            roller.Y = 10000
        if(b == 1):
            roller1.position = roller1o
        else:
            roller1.Y = 10000
        if(c == 1):
            roller2.position = roller2o
        else:
            roller2.Y = 10000
        if(d == 1):
            eggbert.position = eggberto
        else:
            eggbert.Y = 10000
        if(e == 1):
            eggbeard.position = eggbeardo
        else:
            eggbeard.Y = 10000
        if(f == 1):
            syrpr.position = syrpro
            puddle.position = puddleo
            #ADD BUTTER AND STUFF DELCARATION
            if(e == 0):
                ropey.position = ropeyo
        else:
            syrpr.Y = 10000
            puddle.Y = 10000
            ropey.Y = 10000

    #########################
    ##### 




    
    ######################
    #JUMPER
    if(atat == True):
        xs = 0
        if ropey.frame == 0:
            rogord.X= 255
            rogord.Y = 425
        if ropey.frame == 1:
            rogord.X= 285
            rogord.Y = 465
        if ropey.frame == 2:
            rogord.X= 355
            rogord.Y = 505
        if ropey.frame == 3:
            rogord.X= 445
            rogord.Y = 515
        if ropey.frame == 4:
            rogord.X= 485
            rogord.Y = 515
        if ropey.frame == 5:
            rogord.X= 605
            rogord.Y = 495
        if ropey.frame == 6:
            rogord.X= 685
            rogord.Y = 415
        if ropey.frame == 7:
            rogord.X= 725
            rogord.Y = 355
        if ropey.frame == 8:
            rogord.X= 735
            rogord.Y = 360
        if ropey.frame == 9:
            rogord.X= 715
            rogord.Y = 360
        if ropey.frame == 10:
            rogord.X= 705
            rogord.Y = 370
        if ropey.frame == 11:
            rogord.X= 685
            rogord.Y = 415
        if ropey.frame == 12:
            rogord.X= 605
            rogord.Y = 505
        if ropey.frame == 13:
            rogord.X= 455
            rogord.Y = 530
        if ropey.frame == 14:
            rogord.X= 385
            rogord.Y = 520
        if ropey.frame == 15:
            rogord.X= 315
            rogord.Y = 495
        if ropey.frame == 16:
            rogord.X= 245
            rogord.Y = 435
        if ropey.frame == 17:
            rogord.X= 205
            rogord.Y = 395
    ########
    
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rogord.frame = 0
                rogord.first_frame = 0
                rogord.last_frame = 4
                xs = tango
            if event.key == pygame.K_LEFT:
                rogord.frame = 5
                rogord.first_frame = 5
                rogord.last_frame = 9
                xs = -tango
##            if event.key == pygame.K_UP:
##                rogord.frame = 5
##                rogord.first_frame = 5
##                rogord.last_frame = 9
##                ysp = -yoko
##            if event.key == pygame.K_DOWN:
##                rogord.frame = 5
##                rogord.first_frame = 5
##                rogord.last_frame = 9
##                ysp = yoko
            if event.key == pygame.K_SPACE: #JUMP BUTTON
                jump = True
                
            if event.key == pygame.K_g:
                tango = 10
                xs = 0
                ys = 0
                clock = pygame.time.Clock()
                ticks = pygame.time.get_ticks()
                markymark = randrange(0,10)
                jump = False
                dude = 1.0
                roomie = 0
                roomer = True
                men.position = meno
                men.frame = 0
                men.first_frame = 0
                men.last_frame = 0
                
                johnny = 0
                a = 0
                b = 0
                c = 0
                d = 0
                e = 0
                f = 0
                g = 0
                h = 0
                i = 0
                rogord.position = rogordo
                roges = 2
                dying = False
                atat = False
                rer = True
                sooper = False
                oh.stop()

                succulentx = -8
                aa = jswift.render(" ",True, angels)

                yoko = 5
                ysp = 0
            if event.key == pygame.K_v:
                
                roges = 7
            if event.key == pygame.K_o:
                roomie = 15
            if event.key == pygame.K_i:
                roomie = 28
            if event.key == pygame.K_q:
                if(men.frame == 4):
                    men.frame = men.frame + 1
                    men.first_frame = men.frame
                    men.last_frame = men.frame
                hard = False
                impos = False
            if event.key == pygame.K_w:
                if(men.frame == 4):
                    men.frame = men.frame + 1
                    men.first_frame = men.frame
                    men.last_frame = men.frame
                hard = True
                impos = False
            if event.key == pygame.K_e:
                if(men.frame == 4):
                    men.frame = men.frame + 1
                    men.first_frame = men.frame
                    men.last_frame = men.frame
                hard = True
                impos = True
            if event.key == pygame.K_p:
                rogord.Y = 100
            if event.key == pygame.K_1:
                playday.stop()
                playday = song1
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_2:
                playday.stop()
                playday = song2
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_3:
                playday.stop()
                playday = song3
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_4:
                playday.stop()
                playday = song4
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_5:
                playday.stop()
                playday = song5
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_6:
                playday.stop()
                playday = song6
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_7:
                playday.stop()
                playday = song7
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_8:
                playday.stop()
                playday = oh
                playday.play()
                men.Y = 10000
            if event.key == pygame.K_a:
                
                if(men.frame < 5):
                    men.frame = men.frame + 1
                    men.first_frame = men.frame
                    men.last_frame = men.frame
                else:
                    men.Y = 10000
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rogord.first_frame = 0
                rogord.last_frame = 0
                rogord.frame = 0
                xs = 0
            if event.key == pygame.K_LEFT:
                rogord.frame = 5
                rogord.first_frame = 5
                rogord.last_frame = 5
                xs = 0
            if event.key == pygame.K_UP:
                rogord.frame = 5
                rogord.first_frame = 5
                rogord.last_frame = 5
                ysp = 0
            if event.key == pygame.K_DOWN:
                rogord.frame = 5
                rogord.first_frame = 5
                rogord.last_frame = 5
                ysp = 0
                
                
    pygame.display.update()
    ticks = pygame.time.get_ticks()
    clock.tick(20)
