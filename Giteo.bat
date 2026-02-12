@echo off
chcp 65001
SETLOCAL ENABLEDELAYEDEXPANSION
SET MAX_INTENTOS=5
SET INTENTO=0
SET INTENTO_DE_PUSHEO=1
SET COMMIT_MESSAGE=Mejorando mi calculadora
echo .........................................................................
echo Giteo v2.3 pro
echo Iniciando subida a GitHub...
echo ESTA HERRAMIENTA ES COMPATIBLE CON TODOS LOS LENGUAJES DE PROGRAMACIÓN:
echo Python, JavaScript, Java, C# Y ENTRE OTROS.
REM color 0A es para texto verde
REM color 0B es para texto azul claro
REM color 0C es para texto rojo
REM color 0E es para texto amarillo

REM 🚀 --- FLUJO PRINCIPAL --- BORRÉ PORQUE HABIA CIERTAS DUPLICACIONE
CALL :SELECT_LANGUAGE
IF NOT EXIST .gitignore CALL :CREATE_GITIGNORE

GOTO REINTENTAR_CONEXION

EXIT /B

:REINTENTAR_CONEXION
    CALL :CHECK_INTERNET
    IF %INTERNET_STATUS% EQU 0 (
        GOTO INICIAR_O_ACTUALIZAR
    ) ELSE (
            IF !INTENTO! LSS !MAX_INTENTOS! (
                color 0E
                SET /A INTENTO+=1
                echo ERROR: No se detectó la conexión a Internet. Reintentando en 5 segundos... (Intento !INTENTO! de !MAX_INTENTOS!)
                timeout /t 5 /nobreak > NUL
                GOTO REINTENTAR_CONEXION
            ) ELSE (
                color 0C
                echo.
                echo No se puede gitear sin conexión. El proceso está abortado
                echo.
                GOTO END_SCRIPT
            ) 
    )

CALL :INICIAR_O_ACTUALIZAR
CALL :CHECK_INTERNET
CALL :INICIAR_O_ACTUALIZAR
EXIT /B
:: ................................
:: FUNCIONES PRINCIPALES
:: ................................

:SELECT_LANGUAGE
    echo.
    echo --- Qué lenguajes de programación querés crear un .gitignore ---
    echo 1. Python
    echo 2. JavaScript (Node.js)
    echo 3. C# (Visual Studio)
    echo 4. Java
    echo 5. Otro / Ninguno
    echo.


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
    GOTO :EOF

echo .........................................................................

:CREATE_GITIGNORE
    SET "LANG_TYPE=%~1"
    IF EXIST .gitignore (
        echo El archivo .gitignore ya existe. No se sobrescribira.
        GOTO :EOF
    )
    
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


:CHECK_INTERNET
    ping -n 1 8.8.8.8 -w 1000 >NUL
    IF %ERRORLEVEL% EQU 0 (
        color 0A
        SET "INTERNET_STATUS=0"
        echo Conexión a Internet detectada. Continuado con el giteo
    ) ELSE (
        SET "INTERNET_STATUS=1"
        echo ERROR: No se detectó la conexión a Internet.
    )
    echo Intentando verificar conexión a Internet...


echo .........................................................................

:INICIAR_O_ACTUALIZAR
    echo.
    IF NOT EXIST ".git" (
        color 0B
        echo Inicializando nuevo repositorio...
        git init
        git add .
        git commit -m "%COMMIT_MESSAGE%"
        git branch -M main
        SET /P "URL=Ingresa la URL del repositorio de GitHub: "
        git remote add origin %URL%
    ) ELSE (
        echo 📁 Repositorio detectado. Preparando cambios...
        git add .
        git commit -m "%COMMIT_MESSAGE%"
        git branch -M main
        GOTO PUSHEO_INICIAL

    IF %INTERNET_STATUS% EQU 0 (
    GOTO :EOF
    ) ELSE (
        IF !INTENTO! LSS !MAX_INTENTOS! (
            color 0E
            SET /A INTENTO+=1
            echo ERROR: No se detectó la conexión a Internet. Reintentando en 5 segundos... (Intento !INTENTO! de !MAX_INTENTOS!)
            timeout /t 5 /nobreak > NUL
            GOTO CHECK_INTERNET
        ) 
        ELSE (
            color 0C
            echo.
            echo No se puede gitear sin conexión. El proceso está abortado
            echo.
            GOTO END_SCRIPT
        ) 

    )
    GOTO :EOF

echo .........................................................................

:PUSHEO_INICIAL
    echo.
    echo Intentando subir cambios a GitHub...
    echo.
    git push -u origin main
    IF %ERRORLEVEL% NEQ 0 GOTO FALLO_DE_PUSHEO
    GOTO PUSHEO_EXITOSO


:FALLO_DE_PUSHEO
    color 0C
    echo ⚠️  Error en la subida (Rejected o temporal).
    IF !INTENTO_DE_PUSHEO! LEQ 5 (
        echo Intentando sincronizar y reintentar... (Intento !INTENTO_DE_PUSHEO! de 5)

        REM ----------------------------------------------------
        REM PASO 1: INTENTAR CONFIGURAR TRACKING SI ES NECESARIO
        REM Solo intentamos esto en el primer fallo (Intento 1)
        IF !INTENTO_DE_PUSHEO! EQU 1 (
            git branch --set-upstream-to=origin/main main
        )
        git pull origin main --no-rebase
        REM ----------------------------------------------------

        git pull --rebase

        IF %ERRORLEVEL% NEQ 0 GOTO CONFLICTO
        echo Rebase exitoso. Reintentando subida...
        git push -u origin main
        IF %ERRORLEVEL% EQU 0 GOTO PUSHEO_EXITOSO
        SET /A INTENTO_DE_PUSHEO+=1
        timeout /t 2 /nobreak >NUL
        GOTO PUSHEO_INICIAL
    ) ELSE (
        echo 🚫 Falló tras 5 intentos de sincronización.
        GOTO CONFLICTO
    )


:CONFLICTO
    color 0C
    echo.
    echo ❌ ERROR DE MERGE DETECTADO
    echo Para resolverlo:
    echo 1️⃣ Abre tu editor y corrige los archivos.
    echo 2️⃣ Ejecuta: git add .
    echo 3️⃣ Ejecuta: git commit -m "Merge resuelto manualmente"
    echo 4️⃣ Luego intenta el push o corre el script de nuevo.


:PUSHEO_EXITOSO
    color 0A
    echo .........................................................................
    echo ¡Giteo completado exitosamente, cambios subidos a GitHub correctamente!
    GOTO END_SCRIPT

:END_SCRIPT
    echo .........................................................................
    echo Proceso Giteo finalizado.
    timeout /t 1 >NUL
    EXIT /B