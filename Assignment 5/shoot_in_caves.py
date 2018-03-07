import pyautogui, time
import pyperclip

time.sleep(3)

# pyautogui.FAILSAFE = True

print(pyautogui.position())

list_of_words = { "give", "read", "enter", "go", "climb", "put", "insert", "pull", "dive", "jump", "catch", "grab", "explore", "pick", "pluck", "wave", "exit1", "exit2", "exit3", "exit4" }

magic_words = {"back"}

f2 = open('page1.txt','w+')


for word in list_of_words:
	pyautogui.click(1212, 690)
	pyperclip.copy(word)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')
	pyautogui.press('enter')
	time.sleep(0.1)
	pyautogui.click(1119, 730)
	pyautogui.click(1119, 730)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(word+":\n"+text+"\n\n")

f2.close()