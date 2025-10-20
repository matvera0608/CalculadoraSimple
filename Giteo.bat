@echo off
chcp 65001
setlocal enabledelayedexpansion
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
SET "msg10=Este programa está de lujo."
SET "msg11=En arreglos."
SET "msg12=Arreglado problema de optimización"
SET "msg13=Ajustes de formato y linting."
SET "msg14=Realizando actualización de dependencias."
SET "msg15=Actualización del README con pasos de instalación."
SET "msg16=Primer commit con estructura base."
SET "msg17=Respaldo completado exitosamente."


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
echo 10. %msg10%
echo 11. %msg11%
echo 12. %msg12%
echo 13. %msg13%
echo 14. %msg14%
echo 15. %msg15%
echo 16. %msg16%
echo 17. %msg17%
echo 18. Ingresa un mensaje a tu gusto
echo.
SET /P "opcion=Ingresa el número del mensaje o '18' para uno personalizado u otros números deseados: "

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
    SET "COMMIT_MESSAGE=%msg10%"
) ELSE IF "%opcion%"=="11" (
    SET "COMMIT_MESSAGE=%msg11%"
) ELSE IF "%opcion%"=="12" (
    SET "COMMIT_MESSAGE=%msg12%"
) ELSE IF "%opcion%"=="13" (
    SET "COMMIT_MESSAGE=%msg13%"
) ELSE IF "%opcion%"=="14" (
    SET "COMMIT_MESSAGE=%msg14%"
) ELSE IF "%opcion%"=="15" (
    SET "COMMIT_MESSAGE=%msg15%"
) ELSE IF "%opcion%"=="16" (
    SET "COMMIT_MESSAGE=%msg16%"
) ELSE IF "%opcion%"=="17" (
    SET "COMMIT_MESSAGE=%msg17%"
) ELSE IF "%opcion%"=="18" (
    GOTO CUSTOM_MESSAGE
) ELSE (
    color 0C
    echo Opción no válida. Por favor, intenta de nuevo.
    GOTO SELECT_COMMIT_MSG
)

GOTO CONTINUE_GIT_OPERATIONS

:CUSTOM_MESSAGE
SET /P "COMMIT_MESSAGE=Commitea tu mensaje: "

IF "!COMMIT_MESSAGE!"=="" ( 
    color 0C
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
    color 0C
    echo ERROR: No se detectó la conexión a Internet.
    echo No se puede gitear sin conexión.
    echo.
    pause
    GOTO END_SCRIPT
)
echo.
echo Conexión a Internet detectada. Continuado con el giteo
echo.

@REM :FULL_BACKUP
@REM echo.
@REM echo --- Subida completa forzada ---
@REM echo Agregando todos los archivos, incluso nuevos o ignorados...
@REM git add .
@REM git status
@REM pause
@REM git commit -m "%COMMIT_MESSAGE%"
@REM git push -u origin main
@REM echo.
@REM echo ¡Respaldo completo realizado!
@REM GOTO END_SCRIPT

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
    echo Repositorio ya inicializado
    echo esta sección es para agregar en el repositorio correspondiente
    git add .
    git commit -m "%COMMIT_MESSAGE%"
    git push -u origin main
)
echo Intentando subir cambios a GitHub
:: --- MANEJO DE ERROR REJECTED (La clave para la automatización) ---
@REM IF %ERRORLEVEL% NEQ 0 (
@REM     echo.
@REM     echo ERROR: Falló la subida (Rejected). Tu rama no está actualizada.
@REM     echo Intentando sincronizar y subir de nuevo...
    
@REM     :: AUTOMATIZACIÓN: Usar git pull --rebase para sincronizar
@REM     git pull --rebase 
    
@REM     IF %ERRORLEVEL% NEQ 0 (
@REM         color 0C REM Cambiar color a rojo para indicar error
@REM         echo.
@REM         :: CONFLICTO REAL (Detener y mostrar pasos manuales)
@REM         echo.
@REM         echo ERROR: No se pudo hacer el pull/rebase. Hubo un conflicto de fusion.
@REM         echo.
@REM         echo Por favor, sigue estos pasos para resolverlo:
@REM         echo 1. Abre el editor de codigo y resuelve los conflictos.
@REM         echo 2. Una vez resueltos, usa la terminal para ejecutar:
@REM         echo    git add .
@REM         echo    git rebase --continue
@REM         echo.
@REM         echo Si quieres cancelar el rebase, usa:
@REM         echo git rebase --abort
@REM         echo.
@REM         pause
@REM         GOTO END_SCRIPT
@REM     ) ELSE (
@REM         :: Rebase exitoso, reintentar push
@REM         echo Rebase exitoso. Reintentando la subida...
@REM     )
@REM )
git push -u origin main
color 0A
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