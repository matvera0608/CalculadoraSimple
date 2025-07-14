@echo off
chcp 65001

echo Giteo.bat
echo Iniciando subida a GitHub...

:: --- CONFIGURACION DE MENSAJES DE COMMIT ---
:: Define tus mensajes de commit predefinidos aqui
SET "msg1=SIGO MEJORANDO MI CALCULADORA."
SET "msg2=ME ENCANTA MI CALCULADORA."
SET "msg3=ESTE ARCHIVO PARECE UNA CALCULADORA CIENTÍFICA."
SET "msg4=FUNCIONES IMPLEMENTADAS."
SET "msg5=EN PROCESO DE REFACTORIZACIÓN DE CÓDIGO."
SET "msg6=DOCUMENTACIÓN ACTUALIZADA."
SET "msg7=EN MEJORA CONTINUA, PERO YA PARECE UNA APP DE CALCULADORA."
SET "msg8=YA ES APTO PARA JUGAR UN POCO CON LA CALCULADORA."
SET "msg9=NO ES NECESARIO DEPENDER 100%% DEL MOUSE."

:: --- SELECCION DE MENSAJE DE COMMIT ---
echo.
echo --- Selecciona un mensaje de commit ---
echo 1. %msg1%
echo 2. %msg2%
echo 3. %msg3%
echo 4. %msg4%
echo 5. %msg5%
echo 6. %msg6%
echo 7. %msg7%
echo 8. %msg8%
echo 9. %msg9%
echo 10. Ingresar un mensaje personalizado
echo.

:SELECT_COMMIT_MSG
SET /P "opcion=Ingresa el número del mensaje o '10' para uno personalizado u otros números deseados: "

:: Usamos IF/ELSE IF para manejar las opciones numéricas y el salto a personalizado
IF "%opcion%"=="1" (
    SET "COMMIT_MESSAGE=%msg1%"
) ELSE IF "%opcion%"=="2" (
    SET "COMMIT_MESSAGE=%msg2%"
) ELSE IF "%opcion%"=="3" (
    SET "COMMIT_MESSAGE=%msg3%"
) ELSE IF "%opcion%"=="4" (
    SET "COMMIT_MESSAGE=%msg4%"
) ELSE IF "%opcion%"=="5" (
    SET "COMMIT_MESSAGE=%msg5%"
) ELSE IF "%opcion%"=="6" (
    SET "COMMIT_MESSAGE=%msg6%"
) ELSE IF "%opcion%"=="7" (
    SET "COMMIT_MESSAGE=%msg7%"
) ELSE IF "%opcion%"=="8" (
    SET "COMMIT_MESSAGE=%msg8%"
) ELSE IF "%opcion%"=="9" (
    SET "COMMIT_MESSAGE=%msg9%"
) ELSE IF "%opcion%"=="10" (
    GOTO CUSTOM_MESSAGE
) ELSE (
    echo Opción no válida. Por favor, intenta de nuevo.
    GOTO SELECT_COMMIT_MSG
)

GOTO CONTINUE_GIT_OPERATIONS

:CUSTOM_MESSAGE
SET /P "COMMIT_MESSAGE=Commitea tu mensaje: "
IF "%COMMIT_MESSAGE%"=="" (
    echo El mensaje personalizado no puede estar vacío. Volviendo al menú...
    GOTO SELECT_COMMIT_MSG
)

:CONTINUE_GIT_OPERATIONS
echo.
echo Usando el mensaje: "%COMMIT_MESSAGE%"
echo.

git init
git add .
git commit -m "%COMMIT_MESSAGE%"
git branch -M main
git push -u origin main