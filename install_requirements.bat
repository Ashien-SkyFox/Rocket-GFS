@echo off
setlocal

REM Run this file from the project root to install all Python dependencies.

pushd "%~dp0"

echo Installing project requirements...
echo.

where py >nul 2>&1
if %errorlevel%==0 (
    call :try_install "py -3"
    if not errorlevel 1 goto :done

    call :try_install "py -3.13"
    if not errorlevel 1 goto :done

    call :try_install "py -3.12"
    if not errorlevel 1 goto :done

    call :try_install "py -3.11"
    if not errorlevel 1 goto :done
) else (
    where python >nul 2>&1
    if %errorlevel%==0 (
        call :try_install "python"
        if not errorlevel 1 goto :done
    )
)

echo.
echo Installation failed for all detected Python versions.
echo Please install Python 3.12 and run this script again.
popd
pause
exit /b 1

:try_install
set "PY_CMD=%~1"
%PY_CMD% --version >nul 2>&1
if %errorlevel% neq 0 (
    goto :eof
)

echo Using: %PY_CMD%
%PY_CMD% --version

echo.
echo Installing wheel support...
%PY_CMD% -m pip install --upgrade pip wheel
if %errorlevel% neq 0 (
    echo Failed to prepare pip/wheel for %PY_CMD%.
    echo.
    exit /b 1
)

echo.
echo Installing requirements (wheel-only)...
%PY_CMD% -m pip install --only-binary=:all: -r requirements.txt
if %errorlevel% neq 0 (
    echo Requirements install failed for %PY_CMD%.
    echo Trying next available Python version...
    echo.
    exit /b 1
)

exit /b 0

:done
echo.
echo Done.
popd
pause
