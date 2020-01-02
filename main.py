import pygame
import os
import csv
import pandas as pd
import Tkinter as tk
import subprocess

#---Global Variables---#
line = 0

#---- Colours -----#
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

#Get the value in the tkinter text box and set it to the global 'line' variable
def getInputNumber():
    global line
    line=int(e1.get())
    master.quit()
    photos(line)

#Open the file explorer with the current file
def openFileExp(num):
    df = pd.read_csv('data2.csv', usecols=[0,1], header=0,skiprows=line+num-6, nrows=1)
    path = str(df.iloc[0][0])
    path = path  + "\\"+ str(df.iloc[0][1])
    subprocess.Popen(r'explorer /select,'+path)


#Used to jump to a specific line in the excel file
#Just starts up the tkinter window
def enterLine():
    tk.mainloop()

#Open a csv file and read the first two columns, check to see if they are valid
#if so open the photos and place them in the correct positions
def photos(lineNum):
    gameDisplay.fill(black)
    tmp = 0
    nextLine = 0
    for x in range(0,6):
        invalid = 0
        df = pd.read_csv('data.csv', usecols=[0,1], header=0,skiprows=lineNum+nextLine, nrows=1)
        path = str(df.iloc[0][0])+"\\" + str(df.iloc[0][1])
        useless, fileExtension = os.path.splitext(str(df.iloc[0][1]))
        fileExtension = fileExtension.strip()
        if((fileExtension.lower() != '.jpg')):
            if(fileExtension.lower() != '.png'):
                print ("Invalid file")
                print ("Invalid file")
                invalid=1
                font = pygame.font.Font('freesansbold.ttf', 32)
        else:
            image = pygame.image.load(path)
            img = pygame.transform.scale(image, (400, 250))
            font = pygame.font.Font('freesansbold.ttf', 13)
        if(nextLine%2 == 0):
            if(invalid == 1):
                text = font.render('Invalid', True, green, blue)
                textRect = text.get_rect()
                textRect.center = (200, (270*tmp)+75)
                gameDisplay.blit(text, textRect)
            else:
                text = font.render(str(df.iloc[0][1]), True, white, red)
                gameDisplay.blit(img, (0, 270*tmp))
                gameDisplay.blit(text, (0,(270*tmp)+250))
        else:
            if(invalid == 1):
                text = font.render('Invalid', True, green, blue)
                textRect = text.get_rect()
                textRect.center = (450+(200), (270*tmp)+75)
                gameDisplay.blit(text, textRect)
                tmp = tmp + 1
            else:
                text = font.render(str(df.iloc[0][1]), True, white, red)
                gameDisplay.blit(img, (450, 270*tmp))
                gameDisplay.blit(text, (450,(270*tmp)+250))
                tmp = tmp + 1
        nextLine = nextLine + 1
    print "returning"
    return


#_________ Set up Tkinter window __________#
master = tk.Tk()
tk.Label(master,
         text="Row Number:").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
tk.Button(master,
          text='Show', command=getInputNumber).grid(row=1,
                                                       column=0,
                                                       sticky=tk.W,
                                                       pady=4)

#__________ Set up Pygame window __________#
pygame.init()
display_width = 900
display_height = (250*3)+ 60
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pierre\'s Picture Compare')
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
crashed = False


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                photos(line)
                line=line+6
            elif event.key == pygame.K_ESCAPE:
                crashed = True
            elif event.key == pygame.K_SPACE:
                enterLine()
            elif event.key == pygame.K_1:
                openFileExp(0)
            elif event.key == pygame.K_2:
                openFileExp(1)
            elif event.key == pygame.K_3:
                openFileExp(2)
            elif event.key == pygame.K_4:
                openFileExp(3)
            elif event.key == pygame.K_5:
                openFileExp(4)
            elif event.key == pygame.K_6:
                openFileExp(5)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
