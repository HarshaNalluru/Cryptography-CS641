import pyautogui, time
import pyperclip

time.sleep(3)

f = open('inputpars_3.txt','r')
f2 = open('input_output_pairs_xor3_1000.txt','w+')
# j = 0
for line in f:
	# j+=1
	# if j==5:
	# 	break
	ip1,ip2 = line.split(' ')
	ip1 = ip1.strip()
	ip2 = ip2.strip()

	pyautogui.click(1170, 692)
	# for x in ip1:
	# 	pyautogui.press(x)
	pyperclip.copy(ip1)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')
	pyautogui.press('enter')
	time.sleep(0.01)
	pyautogui.click(589, 616)
	pyautogui.doubleClick()
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(ip1+"	"+text+"\n")


	pyautogui.click(1170, 692)
	# for x in ip2:
	# 	pyautogui.press(x)
	pyperclip.copy(ip2)
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('v')
	pyautogui.keyUp('v')
	pyautogui.keyUp('ctrl')
	pyautogui.press('enter')
	time.sleep(0.01)
	pyautogui.click(589, 616)
	pyautogui.doubleClick()
	pyautogui.keyDown('ctrl')
	pyautogui.keyDown('c')
	pyautogui.keyUp('c')
	pyautogui.keyUp('ctrl')
	text = pyperclip.paste()
	f2.write(ip2+"	"+text+"\n")




f.close()
