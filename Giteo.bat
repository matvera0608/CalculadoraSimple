chcp 65001
@echo off
echo Giteo.bat
echo Iniciando subida a GitHub...

git init
git add .
git commit -m "Mejora CONTINUA, PERO MUY COSTOSAMENTE"
git branch -M main
rem git remote add origin https://github.com/matvera0608/CalculadoraSimple
git push -u origin main

pause
