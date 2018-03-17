import utils
import itertools
import os
from string import maketrans
import random
import pyautogui, time
import pyperclip

bit_list = get64bits()
random_string = bitsToStr(bit_list)

f2 = open('presenting_the_proofs.txt','w+')

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
f2.write(random_string+":\n"+text+"\n")

for i in range(5):
	for j in range(4,len(random_string)):
		random_string[j] = outtab[random.randint(0, 16)]

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
	f2.write(random_string+":\n"+text+"\n")

f2.close()