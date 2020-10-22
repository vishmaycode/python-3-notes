# healthy programming
#
# 9am - 5am
# water - water.mp3 - 3.5 liters - input done to close generate log of it
# eyes - eyes.mp3 -  30 mins - input done to close - generate log of it
# physical activity - physical.mp3  - 45 mins - input done generate log of it
#
# rules
# -pygame module to play audio

from time import sleep
import pygame
import datetime

pygame.init()
pygame.mixer.init()

# print("Seperate time and minutes with \' : \' and use 2 characters")
# print("Enter the inital start time:-")
# x = input()
# starth = x[0:2]
# startm = x[3:5]
# print("Enter the stop start time:-")
# x = input()
# stoph = x[0:2]
# stopm = x[3:5]

stoph = 23
starth = 9

while 1:
    if int(stoph) <= datetime.datetime.now().hour:  # and int(stopm) <= datetime.datetime.now().minute:
        continue
    elif int(starth) >= datetime.datetime.now().hour:  # and int(startm) >= datetime.datetime.now().minute:
        continue
    else:
        if 45 == datetime.datetime.now().minute and (9 == datetime.datetime.now().hour or 12 == datetime.datetime.now().hour or 15 == datetime.datetime.now().hour):
            print("PHYSICAL EXERCISE")
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            done = input("Enter done if u did it\n:-")
            while done != 'done':
                sleep(5)
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input(":-")
        if 15 == datetime.datetime.now().minute and (11 == datetime.datetime.now().hour or 4 == datetime.datetime.now().hour):
            print("PHYSICAL EXERCISE")
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            done = input("Enter done if u did it\n:-")
            while done != 'done':
                sleep(5)
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input(":-")
        if 00 == datetime.datetime.now().minute or 30 == datetime.datetime.now().minute: # eye exercise in 30 mins
            if 12 == datetime.datetime.now().hour:
                print("PHYSICAL AND EYE EXERCISE AND DRINK WATER")
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input("Enter done if u did it\n:-")
                while done != 'done':
                    sleep(5)
                    pygame.mixer.music.load("alarm.mp3")
                    pygame.mixer.music.play()
                    done = input(":-")
            elif 30 == datetime.datetime.now().minute and (
                    10 == datetime.datetime.now().hour or 13 == datetime.datetime.now().hour or 16 == datetime.datetime.now().hour):
                print("PHYSICAL AND EYE EXERCISE")
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input("Enter done if u did it\n:-")
                while done != 'done':
                    sleep(5)
                    pygame.mixer.music.load("alarm.mp3")
                    pygame.mixer.music.play()
                    done = input(":-")
            elif 10 == datetime.datetime.now().hour or 11 == datetime.datetime.now().hour or 13 == datetime.datetime.now().hour or 14 == datetime.datetime.now().hour or 15 == datetime.datetime.now().hour or 16 == datetime.datetime.now().hour:
                print("PHYSICAL AND EYE EXERCISE AND DRINK WATER")
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input("Enter done if u did it\n:-")
                while done != 'done':
                    sleep(5)
                    pygame.mixer.music.load("alarm.mp3")
                    pygame.mixer.music.play()
                    done = input(":-")
            else:
                print("EYE EXERCISE")
                pygame.mixer.music.load("alarm.mp3")
                pygame.mixer.music.play()
                done = input("Enter done if u did it\n:-")
                while done != 'done':
                    sleep(5)
                    pygame.mixer.music.load("alarm.mp3")
                    pygame.mixer.music.play()
                    done = input(":-")
    sleep(60)
