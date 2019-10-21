from pygame import *
from random import *
from math import *
from tkinter import *   
import os #all modules

os.environ['SDL_VIDEO_WINDOW_POS'] = '150,100' #blits game in the goven pixels


init()



def playerMove(): #function calling the movement of the players
    #global variables(used for whole game)
    global move,frame,vegetaX,vegetaY,moveG,frameG,gokuX,gokuY,invert,vhb,ghb,ghp,vhp,vhit,ghit,wait,wcheck,waitg,wcheckg,block,blockg,bwait,bwaitg,bcheck,bcheckg,jumpcheck,jumpcheckG,gokuVY,vegetaVY,p1win,p2win,jumpframe,jumpframeG
    keys = key.get_pressed()
    newMove = -1 #move selcted for vegeta
    newMoveG = -1 #everything with a g after is for goku
    
    if wcheck==True:
        wait+=1 #the wait or w variables hault the damge taken
                #for a certain amount of time so that the user cant just keep
                #pressing the attack buttons and the opponent loses health
        
    if wait >=40:
        wait=0
        wcheck=False

    if bcheck==True: 
        bwait+=1
        
    if bwait >=50: #same as the wait, only for block command
        bwait=0
        bcheck=False #checks if persons blocking
        block=False 
        
    if keys[K_p]: #if p pressed
        newMove = PUNCH #newMove is punch
        vegetaY=400 #the y-coordinate of vegeta is always 400
        block=False #not ducking
        jumpcheck=False #hes not jumping
        if vhit == True and wcheck==False: 
            if vhb.colliderect(ghb): #hb=hitbox, v=vegeta
                vhit=False 
                if blockg == True:
                    ghp-=10 #blocking makes you take half the damage
                    if invert == False: #for invert
                        gokuX-=20 #htting makes the other character go back
                        if gokuX < 50:
                            gokuX=50# stops him from going past borders
                    else:
                        gokuX+=20
                        if gokuX >930:
                            gokuX=930 #-for normal
                else:
                    ghp-=15 #same as above only double damage taken since
                            #hes not blocking
                    if invert == False:
                        gokuX-=40
                        if gokuX < 50:
                            gokuX=50
                    else:
                        gokuX+=40
                        if gokuX >930:
                            gokuX=930
                ghb=Rect(gokuX-40,gokuY-50,100,160) #changes variables of goku
                                                    #hb if hes hit
        wcheck=True #waitcheck made true
        
    elif keys[K_o]:
        newMove = KICK #same as punch only vegetas kicking now
        vegetaY=400
        block=False
        jumpcheck=False
        if vhit== True and wcheck==False:
            if vhb.colliderect(ghb):
                vhit=False
                if blockg == True:
                    ghp-=10
                    if invert == False:
                        gokuX-=20
                        if gokuX < 50:
                            gokuX=50
                    else:
                        gokuX+=20
                        if gokuX >930:
                            gokuX=930
                else:
                    ghp-=15
                    if invert == False:
                        gokuX-=40
                        if gokuX < 50:
                            gokuX=50
                    else:
                        gokuX+=40
                        if gokuX >930:
                            gokuX=930
                ghb=Rect(gokuX-40,gokuY-50,100,160)
        wcheck=True
        
    elif keys[K_DOWN]: #block or duck
        jumpcheck=False
        if bcheck == False:
            vhit=True
            block=True #hes blocking now so hell take only half the damage
        bcheck=True
        
        newMove = DOWN
        
    elif keys[K_RIGHT]:
        vhit=True
        block=False
        jumpcheck=False
        if vegetaX < 930:
            if invert == False: #invert makes it opposite
                newMove = RIGHT
                vegetaX +=8 #moving him horizontally
                vegetaY =400 
            else:
                newMove = LEFT #normal
                vegetaX +=8
                vegetaY =400
            vhb=Rect(vegetaX-40,vegetaY-50,100,160) #changes vegetas hb
            
    elif keys[K_LEFT]: #same as right only now hes going left
        vhit=True
        block=False
        jumpcheck=False
        if vegetaX > 50:
            if invert == False:
                newMove = LEFT
                vegetaX -=8
                vegetaY =400
            else:
                newMove = RIGHT
                vegetaX -=8
                vegetaY =400
            vhb=Rect(vegetaX-40,vegetaY-50,100,160)
            
    else:
        jumpcheck=True
        vhit=True
        block=False
        frame = 0 #frame is 0 (hes doing nothing)




        #jump

    if vegetaY==400:
        onground=True #hes on the ground
    elif vegetaY<=400:
        onground=False #hes not

    if keys[K_UP] and onground==True and jumpcheck==True:
        vegetaVY = -17 #goes up
        onground=False # hes not on the ground
        newMove = UP

    if onground==False: 
        newMove = UP
        
    vegetaVY += .7 #slowly goes down(gravity factor)
    vegetaY += vegetaVY 
        
    if vegetaY > 400:
        vegetaY = 400 #cant go past ground
        vegetaVY = 0
        onground=True
    if vegetaY==400: #when hes on ground, hes not doing the jump frames
        jumpframe=0
    vhb=Rect(vegetaX-40,vegetaY-50,100,160)



        

#-----------------------------------------
    #for goku
    #this is all the same as vegeta
    if wcheckg==True:
        waitg+=1
        
    if waitg >=40:
        waitg=0
        wcheckg=False

    if bcheckg==True:
        bwaitg+=1
        
    if bwaitg >=50:
        bwaitg=0
        bcheckg=False
        blockg=False
        
    if keys[K_c]:
        newMoveG = PUNCHG
        gokuY=400
        blockg=False
        jumpcheckG=False
        if ghit == True and wcheckg==False:
            if ghb.colliderect(vhb):
                ghit=False
                if block == True:
                    vhp-=10
                    if invert == False:
                        vegetaX+=20
                        if vegetaX >930:
                            vegetaX=930
                    else:
                        vegetaX-=20
                        if vegetaX <50:
                            vegetaX=50
                else:
                    vhp-=15
                    if invert == False:
                        vegetaX+=40
                        if vegetaX >930:
                            vegetaX=930
                    else:
                        vegetaX-=40
                        if vegetaX <50:
                            vegetaX=50
                vhb=Rect(vegetaX-40,vegetaY-50,100,160)
        wcheckg=True
        
    elif keys[K_v]:
        newMoveG = KICKG
        gokuY=400
        blockg=False
        jumpcheckG=False
        if ghit == True and wcheckg==False:
            if ghb.colliderect(vhb):
                ghit=False
                if block == True:
                    vhp-=10
                    if invert == False:
                        vegetaX+=20
                        if vegetaX >930:
                            vegetaX=930
                    else:
                        vegetaX-=20
                        if vegetaX <50:
                            vegetaX=50
                else:
                    vhp-=15
                    if invert == False:
                        vegetaX+=40
                        if vegetaX >930:
                            vegetaX=930
                    else:
                        vegetaX-=40
                        if vegetaX <50:
                            vegetaX=50
                vhb=Rect(vegetaX-40,vegetaY-50,100,160)
        wcheckg=True
        
    elif keys[K_s]:
        jumpcheckG=False
        if bcheckg == False:
            ghit=True
            blockg=True
        bcheckg=True
        
        newMoveG = DOWNG
        
    elif keys[K_d]:
        ghit=True
        blockg=False
        jumpcheckG=False
        if gokuX < 930:
            if invert == False:
                newMoveG = RIGHTG
                gokuX += 8
                gokuY =400
            else:
                newMoveG = LEFTG
                gokuX += 8
                gokuY =400
            ghb=Rect(gokuX-40,gokuY-50,100,160)
            
    elif keys[K_a]:
        ghit=True
        blockg=False
        jumpcheckG=False
        if gokuX > 50:
            if invert == False:
                newMoveG = LEFTG
                gokuX -= 8
                gokuY =400
            else:
                newMoveG = RIGHTG
                gokuX -= 8
                gokuY =400
            ghb=Rect(gokuX-40,gokuY-50,100,160)
            
    else:
        ghit=True
        blockg=False
        jumpcheckG=True
        frameG = 0


    if gokuY==400:
        ongroundG=True
    elif gokuY<=400:
        ongroundG=False

    if keys[K_w] and ongroundG==True and jumpcheckG==True:
        gokuVY = -17
        ongroundG=False
        newMoveG = UPG

    if ongroundG==False:
        newMoveG = UPG
        
    gokuVY += .7
    gokuY += gokuVY
        
    if gokuY > 400:
        gokuY = 400
        gokuVY = 0
        ongroundG=True
    if gokuY==400:
        jumpframeG=0

    ghb=Rect(gokuX-40,gokuY-50,100,160)




    if invert == False and vegetaX < gokuX:
        invert = True #when vegeta goes past goku both of them are inverted
        return invert
    
    if invert == True and vegetaX > gokuX:
        invert = False #if they are on the right side they are normal
        return invert




#this was taken from the teachers program and it was modified to meet the needs
    #of this proggram

    
    if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        frame = frame + 0.3 # adding 0.2 allows us to slow down the animation
        jumpframe=jumpframe+0.15 # frames for jump
        if frame >= len(pics[move]):
            frame = 7.8
        if jumpframe>=len(pics[move]):
            jumpframe=2
            
    elif newMove != -1:     # a move was selected
        move = newMove      # make that our current move
        frame = 1
        jumpframe=1


        #for goku
    if moveG == newMoveG:     # 0 is a standing pose, so we want to skip over it when we are moving
        frameG = frameG + 0.3 # adding 0.2 allows us to slow down the animation
        jumpframeG = jumpframeG + 0.15
        if frameG >= len(picsG[moveG]):
            frameG = 7.8
        if jumpframeG >= len(picsG[moveG]):
            jumpframeG = 2
            
    elif newMoveG != -1:     # a move was selected
        moveG = newMoveG      # make that our current move
        frameG = 1
        jumpframeG = 1



    if vhp <1:#if vegeta or gokus health is less than one, the other guy wns
        p1win = True
    if ghp <1:
        p2win = True
    
    display.flip()

def makeMove(name,start,end): #taken from teacher and modified
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move

def makeJumpMove(name,start,end): #for jumpingits different
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move

def makeMoveG(nameG,startG,endG): #same as above two only for goku
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    moveG = []
    for i in range(startG,endG+1):
        moveG.append(image.load("%s/%s%03d.png" % (nameG,nameG,i)))
    return moveG

def makeJumpMoveG(nameG,startG,endG): #for gokus jumping
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    moveG = []
    for i in range(startG,endG+1):
        moveG.append(image.load("%s/%s%03d.png" % (nameG,nameG,i)))
    return moveG
    
def drawSceneG(vhp,ghp): #actualdrawing of the scene
    global stage,p1word,p2word #p1/2word is the player1 and player 2 notations
    screen.blit(stage,(0,0)) #the background image
    if move==UP:
        pic = pics[move][int(jumpframe)] #jumpframe list
    else:
        pic = pics[move][int(frame)] #normal list
    if moveG==UPG:
        picG = picsG[moveG][int(jumpframeG)] #jumpframe list for goku
    else:
        picG = picsG[moveG][int(frameG)] #normal list for goku
    if invert == False: #normal images are blitted when invert is false
        screen.blit(transform.scale(pic,(120,190)),(vegetaX-pic.get_width()//2,vegetaY-pic.get_height()//2))          
        screen.blit(transform.scale(picG,(120,190)),(gokuX-picG.get_width()//2,gokuY-picG.get_height()//2))
    if invert == True: #inverted images are blitted when invert is true
        screen.blit(transform.flip((transform.scale(pic,(120,190))),True,False),(vegetaX-pic.get_width()//2,vegetaY-pic.get_height()//2))
        screen.blit(transform.flip((transform.scale(picG,(120,190))),True,False),(gokuX-picG.get_width()//2,gokuY-picG.get_height()//2))

    screen.blit(p1word,(50,10))
    screen.blit(p2word,(790,10))
    if vhp<0:
        vhp=0
    if ghp<0:
        ghp=0
        
    draw.rect(screen,red,p1Rect)
    draw.rect(screen,green,(50,40,ghp,50))
    draw.rect(screen,black,p1Rect,5)
    draw.rect(screen,red,p2Rect) #health bars for the player are drawn
    draw.rect(screen,green,(940,40,-vhp,50))
    draw.rect(screen,black,p2Rect,5)
    display.flip()






mixer.music.load("soundtrack.mp3")
mixer.music.play(-1) #PLAYS SONG

display.set_caption("Mortal Kombat") #caption of program
size=width,height=1000,600
screen=display.set_mode(size)

black=0,0,0
white=255,255,255
green=0,255,0
red=255,0,0
blue=0,0,255#colours

running=True
menud=True #menu display
helpd = False
playd=False
stagesel=False #stage selection
game=False #actual game
p1Rect = Rect(50,40,300,50)
p2Rect = Rect(640,40,300,50)

titlestyle=font.SysFont("Mortal Kombat 4",70)
descriptionstyle=font.SysFont("Mortal Kombat 4",60)
playerstyle=font.SysFont("Mortal Kombat 4",30)
namestyle=font.SysFont("Mortal Kombat 4",50) #all the different sizes of font

menu=image.load("images/menu.jpg")
screen.blit(menu,(0,0)) #background image for main menu
stage1=image.load("stages/stage1.jpg")
stage2=image.load("stages/stage2.jpg")
stage3=image.load("stages/stage3.jpg")
stage4=image.load("stages/stage4.jpg")
stage5=image.load("stages/stage5.jpg") #stages
stage6=image.load("stages/stage6.jpg")




RIGHTG = 0 # These are just the indices of the moves
LEFTG = 1
UPG=2
DOWNG=3
PUNCHG=4
KICKG=5
picsG = []
picsG.append(makeMoveG("gokuss",281,288))      # RIGHT
picsG.append(makeMoveG("gokuss",289,296))    # LEFT
picsG.append(makeJumpMoveG("gokuss",34,42))     # UP      #taken from teachers eXAmPLE AND modified
picsG.append(makeMoveG("gokuss",248,255))    # DOWN
picsG.append(makeMoveG("gokuss",146,153))       #PUNCH
picsG.append(makeMoveG("gokuss",110,117))       #KICK

RIGHT = 0 # These are just the indices of the moves
LEFT = 1
UP=2
DOWN=3
PUNCH=4
KICK=5 #taken from teachers examples and modified
pics = []
pics.append(makeMove("vegetass",289,296))       #RIGHT
pics.append(makeMove("vegetass",281,288))       #LEFT
pics.append(makeJumpMove("vegetass",34,42))         #UP
pics.append(makeMove("vegetass",241,248))       #DOWN
pics.append(makeMove("vegetass",192,199))       #PUNCH
pics.append(makeMove("vegetass",109,116))       #KICK  


#all the global variables are given initial values

frame=0 # current frame within the move
move=0 # current move being performed
vegetaVY=6 
vegetaX, vegetaY = 600,400
vhb=Rect(vegetaX-40,vegetaY-50,100,160)
frameG=0     # current frame within the move
moveG=0      # current move being performed
gokuVY=6
gokuX, gokuY = 200,400 #start position
ghb=Rect(gokuX-40,gokuY-50,100,160)
ghp,vhp=300,300
wait=0
wcheck=False
waitg=0
wcheckg=False
vhit,ghit=True,True
invert=False
block,blockg=False,False
bwait,bwaitg=0,0
bcheck,bcheckg=False,False
jumpcheck,jumpcheckG=True,True
jumpframe,jumpframeG=0,0
vegetaVY,gokuVY=6,6
p1win,p2win=False,False
p1word=playerstyle.render("Player 1",True,red)
p2word=playerstyle.render("Player 2",True,red)
p1winword=titlestyle.render("PLAYER 1 WINS!",True,red)
p2winword=titlestyle.render("PLAYER 2 WINS!",True,red)
myClock = time.Clock() 




while running:
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    if menud == True: #menu display #start screen
        screen.blit(menu,(0,0))

        #all the components of the menu are are drawn using rects and words 
        playRect=Rect(420,190,150,80)
        helpRect = Rect(420,290,150,80)

        title=titlestyle.render("Mortal Kombat",True,red)
        screen.blit(title,(250,5))

        playword=descriptionstyle.render("Play",True,red)
        screen.blit(playword,(420,190))

        helpword=descriptionstyle.render("Help",True,red)
        screen.blit(helpword,(420,290))

        if playRect.collidepoint(mx,my) and mb[0]:
            helpd=False
            menud=False
            playd=True #if play pressed, go to stage selection
            stagesel=True

        if helpRect.collidepoint(mx,my) and mb[0]:
            helpd=True
            menud=False
            playd=False #if help is pressed, go to instructions


        purnoorword=namestyle.render("Purnoor Ghuman",True,red)
        screen.blit(purnoorword,(50,500))

        shahirword=namestyle.render("Shahir Jamil",True,red)
        screen.blit(shahirword,(625,500))   #names of creators     

    
    if helpd == True:  #all the instructions are drawn with word or rectangles and lines 
        screen.blit(menu,(0,0))
        backRect = Rect(800,500,150,80)
        
        backword=descriptionstyle.render("Back",True,red)
        screen.blit(backword,(800,500))

        instr=descriptionstyle.render("Instructions",True,red)
        screen.blit(instr,(325,5))
        
        draw.line(screen,red,(500,100),(500,500),5)

        p1=descriptionstyle.render("Player 1",True,red)
        screen.blit(p1,(150,75))
        p2=descriptionstyle.render("Player 2",True,red)
        screen.blit(p2,(600,75))

        draw.rect(screen,red,(235,150,65,65),2)
        draw.rect(screen,red,(235,215,65,65),2)
        draw.rect(screen,red,(170,215,65,65),2)
        draw.rect(screen,red,(300,215,65,65),2)

        wletter=playerstyle.render("W",True,red)
        screen.blit(wletter,(255,165))
        sletter=playerstyle.render("S",True,red)
        screen.blit(sletter,(255,230))
        aletter=playerstyle.render("A",True,red)
        screen.blit(aletter,(190,230))
        dletter=playerstyle.render("D",True,red)
        screen.blit(dletter,(320,230))
        
        draw.rect(screen,red,(685,150,65,65),2)
        draw.rect(screen,red,(685,215,65,65),2)
        draw.rect(screen,red,(620,215,65,65),2)
        draw.rect(screen,red,(750,215,65,65),2)


        draw.line(screen,red,(717,160),(717,205),3)
        draw.line(screen,red,(717,160),(710,175),3)
        draw.line(screen,red,(717,160),(724,175),3)

        draw.line(screen,red,(717,225),(717,270),3)
        draw.line(screen,red,(717,270),(710,255),3)
        draw.line(screen,red,(717,270),(724,255),3)

        draw.line(screen,red,(630,247),(675,247),3)
        draw.line(screen,red,(630,247),(645,240),3)
        draw.line(screen,red,(630,247),(645,254),3)

        draw.line(screen,red,(760,247),(805,247),3)
        draw.line(screen,red,(805,247),(790,240),3)
        draw.line(screen,red,(805,247),(790,254),3)

        jumpletter=playerstyle.render("Jump",True,red)
        screen.blit(jumpletter,(305,165))
        duckletter=playerstyle.render("Duck",True,red)
        screen.blit(duckletter,(235,280))
        leftletter=playerstyle.render("Left",True,red)
        screen.blit(leftletter,(150,280))
        rightletter=playerstyle.render("Right",True,red)
        screen.blit(rightletter,(320,280))

        screen.blit(jumpletter,(755,165))
        screen.blit(duckletter,(685,280))
        screen.blit(leftletter,(600,280))
        screen.blit(rightletter,(770,280))

        cletter=descriptionstyle.render("C: Punch",True,red)
        screen.blit(cletter,(150,350))
        vletter=descriptionstyle.render("V: Kick",True,red)
        screen.blit(vletter,(150,400))

        oletter=descriptionstyle.render("P: Punch",True,red)
        screen.blit(oletter,(600,350))
        lletter=descriptionstyle.render("O: Kick",True,red)
        screen.blit(lletter,(600,400))
        
        if backRect.collidepoint(mx,my) and mb[0]:
            helpd=False
            menud=True #if back pressed, go back to main menu
            playd=False
            
    if playd == True: #if play screen
        if stagesel == True: #stage selection
            screen.blit(menu,(0,0))
#everything on the stage selction is drawn
            selectSt=descriptionstyle.render("Pick your stage:",True,red)
            screen.blit(selectSt,(265,215))
            
            backRect = Rect(800,500,150,80)
            
            backword=descriptionstyle.render("Back",True,red)
            screen.blit(backword,(800,500))
            stagesel=False

            stageRect1 = Rect(23,50,300,150)
            imgScale1=transform.scale(stage1,(300,150))
            screen.blit(imgScale1,(23,50))
            
            stageRect2 = Rect(346,50,300,150)
            imgScale2=transform.scale(stage2,(300,150))
            screen.blit(imgScale2,(346,50))
            
            stageRect3 = Rect(670,50,300,150)
            imgScale3=transform.scale(stage3,(300,150))
            screen.blit(imgScale3,(670,50))
            
            stageRect4 = Rect(23,300,300,150)
            imgScale4=transform.scale(stage4,(300,150))
            screen.blit(imgScale4,(23,300))
            
            stageRect5 = Rect(346,300,300,150)
            imgScale5=transform.scale(stage5,(300,150))
            screen.blit(imgScale5,(346,300))
            
            stageRect6 = Rect(670,300,300,150)
            imgScale6=transform.scale(stage6,(300,150))
            screen.blit(imgScale6,(670,300))

#highlights the stages when mouse hovers over them
        if stageRect1.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect1,3)     
        elif stageRect2.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect2,3)   
        elif stageRect3.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect3,3)   
        elif stageRect4.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect4,3)   
        elif stageRect5.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect5,3)   
        elif stageRect6.collidepoint(mx,my) and mb[0]==False:
            draw.rect(screen,red,stageRect6,3)
        else: #if pressed they are unhighlighted
            draw.rect(screen,black,stageRect1,3)
            draw.rect(screen,black,stageRect2,3)
            draw.rect(screen,black,stageRect3,3)
            draw.rect(screen,black,stageRect4,3)
            draw.rect(screen,black,stageRect5,3)
            draw.rect(screen,black,stageRect6,3)
            
        
        
        if stageRect1.collidepoint(mx,my) and mb[0]:
            stage=stage1 #if this stage clicked
            screen.blit(transform.scale(stage1,(1000,600)),(0,0)) #stage blitted on all the screen
            game=True #game is started

            #same thing for every stage
        elif stageRect2.collidepoint(mx,my) and mb[0]:
            stage=stage2
            screen.blit(transform.scale(stage2,(1000,600)),(0,0))
            game=True
        elif stageRect3.collidepoint(mx,my) and mb[0]:
            stage=stage3
            screen.blit(transform.scale(stage3,(1000,600)),(0,0))
            game=True
        elif stageRect4.collidepoint(mx,my) and mb[0]:
            stage=stage4
            screen.blit(transform.scale(stage4,(1000,600)),(0,0))
            game=True
        elif stageRect5.collidepoint(mx,my) and mb[0]:
            stage=stage5
            screen.blit(transform.scale(stage5,(1000,600)),(0,0))
            game=True
        elif stageRect6.collidepoint(mx,my) and mb[0]:
            stage=stage6
            screen.blit(transform.scale(stage6,(1000,600)),(0,0))
            game=True

        
        if backRect.collidepoint(mx,my) and mb[0]:
            helpd=False #if back pressed, go back to menu
            menud=True
            playd=False
        

   
            
    while game: #while game true

        for evnt in event.get():  
            if evnt.type == QUIT:
                game = False
                running=False

        playerMove() #calls the function
        drawSceneG(vhp,ghp) #calls the function
        myClock.tick(90) #determines speed of frames 
        while p1win == True: #if player 1 wins
            for evnt in event.get():
                if evnt.type == QUIT: #if x clicked
                    p1win=False
                    game = False #game is stopped
                    running=False 
            screen.blit(p1winword,(200,275)) #this is blitted
            display.flip()

        while p2win == True: #same as player 1 
            for evnt in event.get():
                if evnt.type == QUIT:
                    p2win=False
                    game = False
                    running=False
            screen.blit(p2winword,(200,275))
            display.flip()
        display.flip()
    display.flip()
quit()
