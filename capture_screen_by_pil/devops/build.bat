cd /d "%~dp0"
cd /d "%cd%\"


pyinstaller -F -w --noconsole ../src/capture_screen.pyw --distpath=../../../output
pause