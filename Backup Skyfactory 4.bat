@echo off
title Backup da Pasta com as configs e o mapa pra um!
echo *****************************************************
echo.
echo [Inicio desse codigo maravilhoso] 
echo.

SET /P ano=[Digite o ano (04 digitos)] - 
SET /P mes=[Digite o mes (02 digitos)] - 
SET /P dia=[Digite o dia (02 digitos)] - 

echo.
echo [Deletando o arquivo anterior...]
Del "C:\Users\Pedro Lucas\OneDrive\Backup-Skyfactory4\"**
echo [Deletado...]

echo.
echo [Iniciando o Backup...]

cd "C:\Program Files\7-Zip"

7z.exe a -tzip "C:\Users\Pedro Lucas\OneDrive\Backup-Skyfactory4\Skyfactory4_Mapa_%ano%_%mes%_%dia%.zip" "C:\Users\Pedro Lucas\curseforge\minecraft\Instances\SkyFactory 4\saves\"**

echo.
echo [Backup Feito.]

echo.
echo *****************************************************
pause