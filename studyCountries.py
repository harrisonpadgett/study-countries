from PIL import Image
from termcolor import colored
import time
import os
import random
import subprocess


correct = 0
total = 0
percentage = 0
alreadySeen = []
fileLocation = ''


while True:
    randomCountry = random.choice(os.listdir(fileLocation))

    #print(randomCountry)
    fn, fext = os.path.splitext(randomCountry)

    #print("Current Location Name: " + fn)

    if fn in alreadySeen:
        continue

    img = Image.open(fileLocation + str(randomCountry))

    img.show()


    alreadySeen.append(fn)

    response = input("What location is this?: ")
    response = response.lower()

    if response == fn:
        print(colored("Correct!", 'green'))

        correct = correct + 1

    elif response != fn:
        print(colored("Incorrect! " , 'red') + "Correct response is: " + colored(fn, 'white', attrs=['bold']))

    img.close()

    total = total + 1
    #percentage = correct / total

    print("Score: " + str(correct) + " / " + str(total))

    time.sleep(2)

