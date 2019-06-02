'''
This is educational purpose reflex game.

Red led turn on in a random time and Player 1 or Player 2 should click on their button. Greem led on player 1 or 2 side will turn on depending which one was faster :)
'''

from gpiozero import LED, Button
from time import sleep
from random import randint
from signal import pause

led = LED(17)

led1 = LED(27)
btn1 = Button(22)

led2 = LED(23)
btn2 = Button(24)

def reStartGame():
	led.off()
	sleep(randint(2, 13))
	led.on()

def button1Click():
	led1.blink(0.3, 0.2, 2)
	reStartGame()

def button2Click():
	led2.blink(0.3, 0.2, 2)
	reStartGame()

btn1.when_pressed = button1Click
btn2.when_pressed = button2Click

reStartGame()
print("Game just started")
pause()