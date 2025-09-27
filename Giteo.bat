@echo off
chcp 65001
echo Giteo.bat
echo Iniciando subida a GitHub...
echo ESTA HERRAMIENTA ES COMPATIBLE CON TODOS LOS LENGUAJES DE PROGRAMACIÓN: Pyhton, JavaScript, Java, C# Y ENTRE OTROS.

:: --- VARIABLES DE MENSAJES DE COMMIT ---

SET "msg1=El primer programa hecho por mi."
SET "msg2=Cambios realizados en los archivos de trabajo."
SET "msg3=Mejoras y ajustes pequeños."
SET "msg4=Progreso en desarrollo."
SET "msg5=Correcciones y optimización del código."
SET "msg6=Archivos actualizados para la entrega."
SET "msg7=Subida del contenido actualizado."
SET "msg8=Se implementó muchos detalles y ajustes."
SET "msg9=Es súper útil esta herramienta de automatización, no es necesario escribir código uno por uno."


:: --- SELECCION DE LENGUAJE ---
echo.
echo --- Qué lenguajes de programación querés crear un .gitignore ---
echo 1. Python
echo 2. JavaScript (Node.js)
echo 3. C# (Visual Studio)
echo 4. Java
echo 5. Otro / Ninguno
echo.

:SELECT_LANGUAGE
SET /P "leng_prog_opcion=Ingresa el numero del lenguaje que estas usando: "

IF "%leng_prog_opcion%"=="1" (
    CALL :CREATE_GITIGNORE "python"
) ELSE IF "%leng_prog_opcion%"=="2" (
    CALL :CREATE_GITIGNORE "javascript"
) ELSE IF "%leng_prog_opcion%"=="3" (
    CALL :CREATE_GITIGNORE "csharp"
) ELSE IF "%leng_prog_opcion%"=="4" (
    CALL :CREATE_GITIGNORE "java"
) ELSE IF "%leng_prog_opcion%"=="5" (
    echo No se creara un archivo .gitignore.
) ELSE (
    echo Opcion no valida. Por favor, intenta de nuevo.
    GOTO SELECT_LANGUAGE
)

GOTO SELECT_COMMIT_MSG

:: --- FUNCION PARA CREAR .GITIGNORE ---
:CREATE_GITIGNORE
    IF EXIST .gitignore (
        echo El archivo .gitignore ya existe. No se sobrescribira.
        GOTO :EOF
    )
    SET "LANG_TYPE=%~1"
    IF "%LANG_TYPE%"=="python" (
        echo # Python >> .gitignore
        echo __pycache__/ >> .gitignore
        echo *.pyc >> .gitignore
        echo .venv/ >> .gitignore
    ) ELSE IF "%LANG_TYPE%"=="javascript" (
        echo # Node.js >> .gitignore
        echo node_modules/ >> .gitignore
        echo .env >> .gitignore
    ) ELSE IF "%LANG_TYPE%"=="csharp" (
        echo # C# >> .gitignore
        echo bin/ >> .gitignore
        echo obj/ >> .gitignore
    ) ELSE IF "%LANG_TYPE%"=="java" (
        echo # Java >> .gitignore
        echo *.class >> .gitignore
        echo *.log >> .gitignore
        echo /bin/ >> .gitignore
        echo /target/ >> .gitignore
        echo .project >> .gitignore
        echo .classpath >> .gitignore
    )
    echo Archivo .gitignore creado exitosamente para el lenguaje %LANG_TYPE%.
    GOTO :EOF

:SELECT_COMMIT_MSG
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
echo 10. Ingresa un mensaje a tu gusto
echo.
SET /P "opcion=Ingresa el número del mensaje o '10' para uno personalizado u otros números deseados: "

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

IF "!COMMIT_MESSAGE!"=="" ( 
    echo El mensaje personalizado no puede estar vacío.
    Volviendo al menú...
    GOTO SELECT_COMMIT_MSG
)

:CONTINUE_GIT_OPERATIONS
echo.
echo Usando el mensaje: "%COMMIT_MESSAGE%"
echo.

:: **** VERIFICACIÓN DE INTERNET ****
CALL :CHECK_INTERNET
IF %INTERNET_STATUS% NEQ 0 (
    echo.
    echo ERROR: No se detectó la conexión a Internet.
    echo No se puede gitear sin conexión.
    echo.
    pause
    GOTO END_SCRIPT
)
echo.
echo Conexión a Internet detectada. Continuado con el giteo
echo.
:: --- SECCIÓN PARA INICIAR O ACTUALIZAR REPOSITORIO ---
IF NOT EXIST ".git" (
    echo Inicializando nuevo repositorio...
    git init
    git add .
    git commit -m "%COMMIT_MESSAGE%"
    git branch -M main
    :: AGREGA ESTA LÍNEA SOLO LA PRIMERA VEZ
    SET /P "URL=Ingresa la URL del repositorio de GitHub: "
    git remote add origin %URL%
) ELSE (
    echo Repositorio ya inicializado.
    echo esta sección es para agregar en el repositorio correspondiente
    git add .
    git commit -m "%COMMIT_MESSAGE%"
	rem esta sección es para dar control al pull
    git pull --rebase
)

echo Intentando subir cambios a GitHub...
git push -u origin main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Hubo un CONFLICTO DE FUSION.
    echo Git ha detenido la operacion.
    echo.
    echo Por favor, sigue estos pasos para resolverlo:
    echo 1. Abre el editor de codigo y resuelve los conflictos.
    echo 2. Una vez resueltos, usa la terminal para ejecutar:
    echo    git add .
    echo    git rebase --continue
    echo.
    echo Si quieres cancelar el rebase, usa:
    echo git rebase --abort
    echo.
    pause
    GOTO END_SCRIPT
)
echo.
echo ¡Giteo completado exitosamente!
pause

:CHECK_INTERNET
    ping -n 1 8.8.8.8 -w 1000 >NUL
    IF %ERRORLEVEL% EQU 0 (
        SET "INTERNET_STATUS=0"
    ) ELSE (
        SET "INTERNET_STATUS=1"
    )
    GOTO :EOF

:END_SCRIPT