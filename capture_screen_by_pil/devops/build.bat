rem 运行到当前目录下
cd /d "%~dp0"
cd /d "%cd%\"

rem 首先将py文件拷贝一份并将文件名重命名为pyw后缀
copy ../src/capture_screen.py ../src/capture_screen.pyw

rem 执行打包操作并输出编译后的文件
pyinstaller -F -w --noconsole ../src/capture_screen.pyw --distpath=../../../output

pause