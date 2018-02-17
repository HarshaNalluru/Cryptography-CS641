import pyautogui, time
import pyperclip

time.sleep(3)

f = open('inputpairs.txt','r')
f2 = open('input_output_pairs.txt','w+')
for line in f:
	ip1,ip2 = line.split('	')
	ip1 = ip1.strip()

	pyautogui.click(1170, 692)
	for x in ip1:
		pyautogui.press(x)
	pyautogui.press('enter')
	time.sleep(0.2)
	pyautogui.click(589, 616)
	pyautogui.doubleClick()
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(ip1+"	"+text+"\n")


	pyautogui.click(1170, 692)
	for x in ip2:
		pyautogui.press(x)
	pyautogui.press('enter')
	time.sleep(0.2)
	pyautogui.click(589, 616)
	pyautogui.doubleClick()
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(ip2+"	"+text+"\n")




f.close()
