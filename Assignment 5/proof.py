from utils import *
import itertools
import os
from string import maketrans
import random
import pyautogui, time
import pyperclip

bit_list = get64bits()
random_string = bitsToStr(bit_list)

f2 = open('presenting_the_proofs.txt','w+')

# Abhishek Co-ord : 1187,666  435,664
# Harsha Co-ord : 1187, 691  442, 687

pyautogui.click(1187, 691)
pyperclip.copy(random_string)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(442, 687)
pyautogui.click(442, 687)
pyautogui.click(442, 687)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
text = pyperclip.paste()
f2.write(random_string+":"+text+"\n\n")

for i in range(50):
	randomize = ''
	randomize = random_string[0:4]
	for j in range(4,len(random_string)):
		randomize += outtab[random.randint(0, 15)]

	pyautogui.click(1187, 691)
	pyperclip.copy(randomize)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.click(442, 687)
	pyautogui.click(442, 687)
	pyautogui.click(442, 687)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(randomize+":"+text+"\n")

f2.close()