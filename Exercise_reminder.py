from pygame import mixer
from datetime import datetime
from time import time

def musicplay(file, stopped):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
         User_input = input()
         if User_input == stopped:
            mixer.music.stop()
            break

def log_now(msg):
    with open("messagestore.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 6
    exsecs = 13
    eyessecs = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musicplay('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musicplay('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musicplay('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")