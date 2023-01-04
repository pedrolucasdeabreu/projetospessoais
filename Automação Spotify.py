import pyautogui
import time

banda = input('\nEscreva o nome do cantor ou da banda que você deseja ouvir: ')
alexa = input('\nGostaria de ouvir na alexa?\nS para sim ou N para não: ')

print (f'\nVou tocar This is {banda} no Spotify pra você')

time.sleep(5)

pyautogui.PAUSE = (2)
pyautogui.press ("win")
time.sleep(2)
pyautogui.write ("Spotify")
time.sleep(2)
pyautogui.click(x=172,y=513)
time.sleep(1)
pyautogui.click(x=91,y=106)
time.sleep(1)
pyautogui.click(x=512,y=35)
pyautogui.write("This is " + banda)
pyautogui.press ("enter")
pyautogui.click(x=403, y=568)
pyautogui.click(x=321, y=391)

if (alexa == 'S') or (alexa == 's'):
    pyautogui.click(x=1731, y=986)
    time.sleep(8)
    pyautogui.click(x=1710, y=933)
    print(f'\nTocando This is {banda} na Alexa do Pedro, aproveite!')
else:
    print(f'\nTocando This is {banda}, aproveite!')