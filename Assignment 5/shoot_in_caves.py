import pyautogui, time
import pyperclip
from login_in_caves import login

time.sleep(3)

# pyautogui.FAILSAFE = True

print(pyautogui.position())

# list_of_words = {"give", "pluck", "exit2", "catch", "put", "go","read", "enter", "climb", "insert", "pull", "dive", "jump", "grab", "explore", "pick", "wave", "exit1",  "exit3", "exit4" }

# magic_words = {"back"}

list_of_words = {"exit1","exit2","exit3","exit4"}
f2 = open('page2_after_go.txt','w+')


# for word in list_of_words:
# 	pyautogui.click(1212, 690)
# 	pyperclip.copy(word)
# 	pyautogui.keyDown('ctrl')
# 	pyautogui.keyDown('v')
# 	pyautogui.keyUp('v')
# 	pyautogui.keyUp('ctrl')
# 	pyautogui.press('enter')
# 	time.sleep(0.1)
# 	pyautogui.click(1119, 730)
# 	pyautogui.click(1119, 730)
# 	pyautogui.click(1119, 730)
# 	pyautogui.keyDown('ctrl')
# 	pyautogui.keyDown('c')
# 	pyautogui.keyUp('c')
# 	pyautogui.keyUp('ctrl')
# 	text = pyperclip.paste()
# 	f2.write(word+":\n"+text+"\n\n")
# 	if text == word:
# 		break

# login()
# time.sleep(0.1)
# pyautogui.click(693, 437)
# pyautogui.click(1212, 690)
# pyperclip.copy("go")
# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('v')
# pyautogui.keyUp('v')
# pyautogui.keyUp('ctrl')
# pyautogui.press('enter')

for word in list_of_words:
	pyautogui.click(1212, 690)
	pyperclip.copy(word)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.click(1119, 730)
	pyautogui.click(1119, 730)
	pyautogui.click(1119, 730)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(word+":\n"+text+"\n")
	if text == word:
		f2.write("\nFailed\n\n")
		pyautogui.click(1071, 628)
		login()
		time.sleep(1)
		pyautogui.click(701, 443)
		time.sleep(1)
		pyautogui.click(1212, 690)
		pyperclip.copy("go")
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('v')
		pyautogui.keyUp('v')
		pyautogui.keyUp('ctrl')
		pyautogui.press('enter')
		time.sleep(1)

f2.close()