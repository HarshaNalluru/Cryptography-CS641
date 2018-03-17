def login():
	import pyautogui, time
	import pyperclip

	# time.sleep(3)

	# pyautogui.FAILSAFE = True

	print(pyautogui.position())

	username = "Descrifardo"
	password = "nj3d6isdf"

	# Enters username
	pyautogui.click(1066, 594)
	pyperclip.copy(username)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')

	# Enters password
	pyautogui.click(1063, 632)
	pyperclip.copy(password)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')

	pyautogui.keyDown('tab')
	pyautogui.keyUp('tab')

	# Clicks ENter
	pyautogui.press('enter')

if __name__ == '__main__':
   login()