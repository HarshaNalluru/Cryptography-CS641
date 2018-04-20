import pyautogui, time
import pyperclip
# from login_in_caves import login

time.sleep(3)

# pyautogui.FAILSAFE = True
print(pyautogui.position())

# list_of_words = {"give", "pluck", "exit2", "catch", "put", "go","read", "enter", "climb", "insert", "pull", "dive", "jump", "grab", "explore", "pick", "wave", "exit1",  "exit3", "exit4" }
# magic_words = {"back"}

list_of_words = {"exit1","exit2","exit3","exit4"}
# f2 = open('page2_after_go.txt','w+')

pyautogui.click(1212, 690)
pyperclip.copy("exit1")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit2")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit4")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit3")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit1")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit4")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)


pyautogui.click(1212, 690)
pyperclip.copy("exit4")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit2")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit2")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)

pyautogui.click(1212, 690)
pyperclip.copy("exit1")
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')
pyautogui.press('enter')
time.sleep(1)
######################################33
# f2.close()