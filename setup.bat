pushd "%~dp0"

"C:\Python27\python" setup.py py2exe 

copy /y "dist\GenerateTestCode.exe" "GenerateTestCode.exe"
copy /y "dist\library.zip" "library.zip"
copy /y "dist\python27.dll" "python27.dll"

pause