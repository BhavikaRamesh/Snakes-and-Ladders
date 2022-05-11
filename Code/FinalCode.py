import pygame
from random import randint
import time


clock=pygame.time.Clock()

pygame.init()
w=1366
h=768

icon=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\ficon1.jpeg")
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
pygame.display.set_caption("Snakes N Ladders")
pygame.display.set_icon(icon)
pygame.display.update()

black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)
off_white = (250, 245, 224, 255)

board= pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\board.jpeg")
dice1=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice1.png")
dice2=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice2.png")
dice3=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice3.png")
dice4=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice4.png")
dice5=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice5.png")
dice6=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\dice6.png")

redgoti=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\redgoti.png")
greengoti=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\greengoti.png")
yellowgoti=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\yellowgoti.png")
menubg=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\ficon2.jpeg")
menubg2=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\ficon1.jpeg")
p=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\menu.jpeg")
intbg1=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\bg1.jpeg")
intbg2=pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\bg1.jpeg")
rule = pygame.image.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\rules.jpeg")
pygame.mixer.music.load("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\music.wav")
snakesound=pygame.mixer.Sound("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\snake.wav")
win=pygame.mixer.Sound("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\win.wav")
lose=pygame.mixer.Sound("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\lose.wav")
ladder=pygame.mixer.Sound("C:\\Users\\Harshini R\\Desktop\\WISE PY103\\ladder.wav")

mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()

def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()

def goti(a):
    l1 = [[232, 690],[315,690],[390,690],[462,690],[536,690],[609,690],[690,690],[760,690],[834,690],[908,690],[982,690],[982,615],[908,615],[834,615],[760,615],[690,615],[609,615],[536,615],[462,615],[390,615],[315,615] , [315,540],[390,540],[462,540],[536,540],[609,540],[690,540],[760,540],[834,540],[908,540],[982,540],[982,467],[908,467],[834,467],[760,467],[690,467],[609,467],[536,467],[462,467],[390,467],[315,467] ,[315,390],[390,390],[462,390],[536,390],[609,390],[690,390],[760,390],[834,390],[908,390],[982,390],[982,315],[908,315],[834,315],[760,315],[690,315],[609,315],[536,315],[462,315],[390,315],[315,315],[315,240],[390,240],[462,240],[536,240],[609,240],[690,240],[760,240],[834,240],[908,240],[982,240],[982,167],[908,167],[834,167],[760,167],[690,167],[609,167],[536,167],[462,167],[390,167],[315,167] ,[315,88],[390,88],[462,88],[536,88],[609,88],[690,88],[760,88],[834,88],[908,88],[982,88],[982,18],[908,18],[834,18],[760,18],[690,18],[609,18],[536,18],[462,18],[390,18],[315,18]]
    l2 = l1[a]
    x=l2[0]
    y=l2[1]
    return x,y
     
def text_objects1(text, font):
    textSurface = font.render(text, True,b_purple)
    return textSurface, textSurface.get_rect()

def ladders(x):
    step = {1:38, 4:14, 9:31, 21:42, 33:84, 51:67, 72:91, 80:99}
    if x in step.keys():
        final_val = step[x]
        return final_val
    else:
        return x

def snakes(x):
    snake = {28:8, 54:34, 62:18,87:36, 95:75, 98:79}
    if x in snake.keys():
        final_val = snake[x]
        return final_val
    else:
        return x

def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        GD.blit(a,(100,500))
        pygame.display.update()    

def button2(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
       
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)  
   
def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
       
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
   
def turn(score,l,s):
   
    a=randint(1,6)#player dice roll
    if a==6:
        six=True
    else:
        six=False
    p=dice(a)
    score+=a
    if score<=100:
        lad=ladders(score) #checking for ladders for player
        if lad!=score:
            l=True
            pygame.mixer.Sound.play(ladder)
            time=pygame.time.get_ticks()
            score=lad
        snk=snakes(score)
        if snk!=score: #checking for snakes for player
            s=True
            pygame.mixer.Sound.play(snakesound)
            score=snk
           
    else: #checks if player score is not grater than 100
        score-=a
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<1500:
            message_display1("Can't move!",650,50,35,black)
            pygame.display.update()
    return score,l,s,six
   

def Quit():
    pygame.quit()
    quit()

def button(text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            if b==1:
                options()
            elif b==5:
                return 5
            elif b==0:
                Quit()
            elif b=="s" or b== 2 or b == 3 or b == 4:
                return b
            elif b==7:
                options()
            else :return True
                               
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
   
def intro():
    time=pygame.time.get_ticks()
   
    while True:
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<500:    
            GD.blit(menubg,(0,0))
            pygame.display.update()
        time=pygame.time.get_ticks()
                 
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
        pygame.display.update()

def main():    
    pygame.mixer.music.play(-1)
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
       
        GD.blit(menubg2,(0,0))
        button("Play",mouse[0],mouse[1],(w/2-100),h/2,200,100,green,b_green,60,1)

        button("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+200,200,100,red,b_red,60,0)

        mouse=pygame.mouse.get_pos()
        if button2("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
            pygame.mixer.music.pause()
        if button2("Unmute Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
            pygame.mixer.music.unpause()
        pygame.display.update()

def options():
   
    flag=True
    while flag==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    Quit()

        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        b1=b2=b5=-1
        GD.blit(rule,(0,0))

        b2=button("Go",mouse[0],mouse[1],(w/2)-150,650,300,50,green,b_green,30,2)
       
        b5 = button("back", mouse[0], mouse[1], 0,650,200,50,red,b_red,30, 5)
        if b5==5:
            main()
        if b1=="s":
            play(21)
        if b2==2:
            play(2)
       
        pygame.display.update()

def play(b):
    b6=-1
    time=3000
    if b6==7:
        options()
    GD.blit(intbg2,(0,0))
    GD.blit(intbg1,(288, 700))
    GD.blit(board,(288, 0))
    xcr=xcy=xcg=xcb=232
    ycr=ycy=ycg=ycb=615
    GD.blit(redgoti,(xcy-75,ycy))
    if 5>b>1 or b==21:
        GD.blit(yellowgoti,(232,690))
    if 5>b>1 or b==21:
        GD.blit(redgoti,(xcy-100,ycy))        
    if 5>b>2 or b==21:
        GD.blit(greengoti,(xcg,ycg))      
    if 5>b>2:
        GD.blit(bluegoti,(xcb,ycb))
    p1="Player 1"
    p1score=0
    if b==21:
        p2="Computer"
        p2score=0
    if 5>b>1:
        p2="Player 2"
        p2score=0
    if 5>b>2:
        p3="Player 3"
        p3score=0
    if 5>b>3:
        p4="Player 4"
        p4score=0
    t=1
    play=True
    while True:
        l=False
        s=False
        time=3000
        GD.blit(intbg2,(0,0))
        GD.blit(intbg2,(288, 700))
        GD.blit(board,(288, 0))
        mouse=pygame.mouse.get_pos()
       
        for event in pygame.event.get():
           
            if event.type==pygame.QUIT:
                Quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()

        if 5>b>1:
            if button1("Player 1",mouse[0],mouse[1],50,700,200,50,red,grey,30):
                if t==1:
                    p1score,l,s,six=turn(p1score,l,s)
                    xcr,ycr=goti(p1score)
                    if not six:
                        t+=1
                    if p1score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 1 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
               
            if button1("Player 2",mouse[0],mouse[1],1125,700,200,50,yellow,grey,30):
                if t==2:
                    p2score,l,s,six=turn(p2score,l,s)
                    xcy,ycy=goti(p2score)
                    if not six:
                        t+=1
                        if b<3:
                            t=1
                   
                    if p2score==100:
                        time=pygame.time.get_ticks()
                        while pygame.time.get_ticks()-time<2000:
                            message_display1("Player 2 Wins",650,50,50,black)
                            pygame.mixer.Sound.play(win)
                            pygame.display.update()
                        break
               
        b6=button("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
        GD.blit(redgoti,(xcr,ycr))
        if 5>b>1 or b==21:
            GD.blit(yellowgoti,(xcy,ycy))
           
           
        if 5>b>2:
            GD.blit(greengoti,(xcg+4,ycg))
           
             
        if 5>b>3:
            GD.blit(bluegoti,(xcb+6,ycb))
           
        if l:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Ladder!",650,50,35,black)
                pygame.display.update()
        if s:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<2000:
                message_display1("There's a Snake!",650,50,35,black)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()
           
intro()    
main()
