
#Script by Hovered Cube


import pyttsx3
import os
import pyautogui
import random as rn
import time
import getpass

username = str(getpass.getuser())
ai = pyttsx3.init()
ai.say('Hello'+username+'! welcomeback!')
ai.runAndWait()
time.sleep(100)


def warn0():
    sentences = {
        0: 'bro!!! its been 20 freaking minutes!',
        1: 'its been 30 minutes! now take rest',
        2: 'hey bro. it is exactly 30 minutes that you are staring at the screen. take a rest.'
    }
    return sentences[rn.randint(0, 2)]


def warn1():
    sentences = {
        0: 'your eyes are fucked up. please take a rest, and get fucking away from me.',
        1: 'think of your eyes. you dont want to loose them,do you?',
        2: 'did you know that siting more than 30 minutes will have alot of fucking bad consquenses?'
    }
    return sentences[rn.randint(0, 2)]


def warn2():
    sentences = {
        0: 'hey! im talking to you. dont you undrestand?',
        1: 'bro, stop being a fucking stubborn.',
        2: 'im serious. get some rest please.'
    }
    return sentences[rn.randint(0, 2)]


def warn3():
    sentences = {
        0: 'dont you want me to shutdown the pc? do you?',
        1: 'get the fuck away or i will shutdown myself.',
        2: 'hey, you still here? well im going to shutdown the pc then'
    }
    return sentences[rn.randint(0, 2)]


def warner(warningNumber):
    if warningNumber == 1:
        ai.say(warn0())
        ai.runAndWait()
        pyautogui.hotkey('winleft', 'm')

    if warningNumber == 2:
        ai.runAndWait()
        ai.say(warn1())
        pyautogui.hotkey('winleft', 'm')

    if warningNumber == 3:
        ai.runAndWait()
        ai.say(warn2())
        pyautogui.hotkey('winleft', 'm')

    if warningNumber == 4:
        ai.runAndWait()
        ai.say(warn3())
        pyautogui.hotkey('winleft', 'm')

    if warningNumber == 5:
        ai.runAndWait()
        ai.say(warn3())
        pyautogui.hotkey('winleft', 'm')

    if warningNumber == 6:
        ai.runAndWait()
        ai.say(warn3())
        pyautogui.hotkey('win', 'm')

    if warningNumber == 7:
        pyautogui.alert("your pc will be shutdown in 6 seconds")
        time.sleep(6)
        os.system('shutdown /s')


while True:
    warningNumber = 0
    secondsPassedWithoutMovement = 0
    while True:
        position1 = pyautogui.position()
        time.sleep(1)
        if pyautogui.position() != position1:
            warningNumber += 1
            warner(warningNumber)
        secondsPassedWithoutMovement += 1
        if secondsPassedWithoutMovement == 300:  # => 5min
            break
