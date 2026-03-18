@echo off
setlocal

if "%~1"=="" (
    echo Usage: release.bat ^<version^> [gtcli-path]
    echo.
    echo Examples:
    echo   release.bat v1.1.0
    echo   release.bat v1.1.0 C:\build\gtcli.exe
    exit /b 1
)

set VERSION=%~1
set GTCLI=%~2
set REPO=going-kr/going-ui-skill
set SKILL_ZIP=going-ui-skill-%VERSION%.zip

echo === Going UI Skill Release %VERSION% ===

:: Build skill zip (exclude binaries, build artifacts, bat, git)
echo Packaging skill files...
powershell -Command "Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '\\\.git\\' -and $_.Extension -notin '.exe','.dll','.bat','.py','.xlsx','.zip' } | Compress-Archive -DestinationPath '%SKILL_ZIP%' -Force"

if not exist "%SKILL_ZIP%" (
    echo Failed to create %SKILL_ZIP%
    exit /b 1
)
echo Created %SKILL_ZIP%

:: Build asset list
set FILES="%SKILL_ZIP%"
if not "%GTCLI%"=="" (
    set FILES=%FILES% "%GTCLI%"
)

:: Create release
echo Creating release...
gh release create %VERSION% %FILES% -R %REPO% --title "Release %VERSION%" --notes "Release %VERSION%"

if %ERRORLEVEL% equ 0 (
    echo.
    echo Done: https://github.com/%REPO%/releases/tag/%VERSION%
) else (
    echo Failed.
)

:: Cleanup
del "%SKILL_ZIP%" 2>nul
