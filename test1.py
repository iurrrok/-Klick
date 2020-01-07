#Импортирование библиотек

import pyautogui #отвечает за АвтоКликер
import time  #отвечает за Отсчет

#Отсчет(необязателен)

print("Через 6 секунд запустится АвтоКликер!!!")
print(1)
time.sleep(0.50)
print(2)
time.sleep(1)
print(3)
time.sleep(1.50)
print(4)
time.sleep(2)
print(5)
time.sleep(2.50)
print(6)
time.sleep(3)

print("============================")
print("АвтоКликер запустился!")

#Цикл

def multiply(x,y):
	pyautogui.press('f5')
	for test in range(x):
		pyautogui.press('tab',interval=2)
	pyautogui.press('enter')
	time.sleep(10)
	pyautogui.moveTo(500, 610); pyautogui.click()
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'w')

for x in range (21,80):
	multiply(x,1)

print("конец!")
