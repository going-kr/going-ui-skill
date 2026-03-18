@echo off
setlocal

set MSG=%~1
if "%MSG%"=="" set MSG=Update skill docs

cd /d "%~dp0"

git add -A
git commit -m "%MSG%"
git push

if %ERRORLEVEL% equ 0 (
    echo Done.
) else (
    echo Failed.
)
