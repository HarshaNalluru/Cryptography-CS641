from utils import *
import itertools
import os
from string import maketrans
import random
import pyautogui, time
import pyperclip

# Abhishek Co-ord : 1187,666  435,664
# Harsha Co-ord : 1187, 691  442, 687

bit_list = get64bits()

password = "ktirlqhtlqijmmhqmgkplijngrluiqlq"
f2 = open('crack_trials_finals.txt','w+')

f3 = open('password_final.txt','w+')

decrypted_password = ''

final = []
flag = 0
while 1:
	for counter in range(0,16):
		flag = 0

		for i in range(0,256):
			decrypted_password = ''
			if counter!=0:
				decrypted_password = final[counter-1]
			decrypted_password += outtab[i/16] + outtab[i%16]

			pyautogui.click(1187, 691)
			pyperclip.copy(decrypted_password)
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('v')
			pyautogui.keyUp('v')
			pyautogui.keyUp('ctrl')
			pyautogui.press('enter')
			time.sleep(0.01)
			pyautogui.click(442, 687)
			pyautogui.click(442, 687)
			pyautogui.click(442, 687)
			pyautogui.keyDown('ctrl')
			pyautogui.keyDown('c')
			pyautogui.keyUp('c')
			pyautogui.keyUp('ctrl')
			text = pyperclip.paste()
			f2.write(decrypted_password+":"+text+"\n\n")

			if password[:(counter+1)*2] == text[:(counter+1)*2]:
				f3.write(decrypted_password+":"+text+"\n\n")
				final.append(decrypted_password)
				flag = 1
				break
	if flag == 1:
		print("Done!")
		break
f2.close()
f3.close()