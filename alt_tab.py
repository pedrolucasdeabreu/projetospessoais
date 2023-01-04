import pyautogui
import time
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
sg.set_options(font=("Courier New", 10))
layout = [
    [sg.Text('Escreva de quantos em quantos segundos o código irá dar Alt+Tab')],
    [sg.Text('Em quantos segundos?:'), sg.Input(key='segundos', size=(20, 1))],
    [sg.Button('Começar')]
]

# Janela
janela = sg.Window('Alt+Tab Maroto by Pedritow', layout)
# Execução

eventos, valores = janela.read()

tempo = int(valores['segundos'])

janela.Close()

while True:
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Começar':
        if tempo < 0:
            print('\nQuantidade de segundos inválida!\nFechando o código!')
            time.sleep(5)
            break
    if tempo > 0:
        number = 0
        cont_tempo = 0
        while number != -100:
            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')
            time.sleep(tempo)
            cont_tempo = cont_tempo + tempo
            number = number+1
            print(f'\nRepetindo o código pela {number} vez')
            if cont_tempo < 60:
                print(f'Você já está a {cont_tempo:.0f} segundo(s) parado')
            if cont_tempo >= 60 and cont_tempo <= 3600:
                print(f'Você já está a {cont_tempo/60:.0f} minuto(s) e {cont_tempo%60} segudnos parado')
            if cont_tempo >= 3600:
                print(f'Você já está a {cont_tempo/3600:.0f} hora(s), {(cont_tempo%3600)/60:.0f} minutos e {((cont_tempo%3600)%60)/60:.0f} segudnos parado')
    else:
        print('\nVocê optou por sair!\nFechando o código!')
        time.sleep(5)
        break