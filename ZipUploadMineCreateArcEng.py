import os
import time
from datetime import datetime
from zipfile import ZipFile
from mega import Mega

#Foi necessario instalar as bibliotecas a seguir alem das bibliotecas 'normais':

'''
pip install --user --upgrade mega.py
pip install --user --upgrade tenacity
'''

print('********************************************************************')
print('Código que zipa e envia o mundo PedroeLidia da .Minecraft do Create Arcane Engeneering pra Cloud')
print('\nVersionamento:\n')
print('2024/02/16 -> Desenvolvido por Pedro Lucas de Abreu')
print('********************************************************************\n')

def zip_folder(folder_path, zip_name):
    with ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

folder_to_zip = r'C:\Users\miels\curseforge\minecraft\Instances\Create Arcane Engineering\saves\PedroeLidia'
desktop_path = r'C:\Users\miels\OneDrive\Área de Trabalho'

email = input('Insira seu e-mail do MEGA: ')
password = input('Insira sua senha do MEGA: ')

inicio = time.time()

# Obtendo a data atual no formato desejado (YYYYMMDD)
date_today = datetime.now().strftime('%Y%m%d')

print ('\nZipando os arquivos no Desktop')

# Nome do arquivo ZIP com a data atual
output_zip = os.path.join(desktop_path,f'Create_Arc_Eng_PedroeLidia_' + date_today + '.zip')

zip_folder(folder_to_zip, output_zip)

print ('\nArquivo zipado no Desktop')

print ('\nConectando ao mega')

# Autenticação no Mega (substitua 'email' e 'senha' pelos seus dados de login)
mega = Mega()
m = mega.login(email, password)

print ('\nConectado com sucesso ao mega')

# Obter uma lista de todos os arquivos na raiz do Mega
files = m.get_files()

print ('\nEnviando o Arquivo -> Create_Arc_Eng_PedroeLidia_' + date_today + '.zip para o Mega')

# Fazendo o upload do arquivo
m.upload(output_zip)

print('\n********************************************************************\n')
print('OBS: Deletar os arquivos anteriores no MEGA pra não ocupar espaco do MEGA\n')
print('********************************************************************\n')

print ('Upload do arquivo -> Create_Arc_Eng_PedroeLidia_' + date_today + '.zip realizado com sucesso')

fim = time.time()
tempo_total = fim - inicio
tempo_total = round(tempo_total / 60, 2)

print('\n********************************************************************\n')
print("Processo executado com sucesso! Tempo de execucao: " + str(tempo_total) + ' minutos\n')
print('********************************************************************\n')
