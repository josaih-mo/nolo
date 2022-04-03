IF EXIST "C:\Python*" ( GOTO :eof )
ELSE (
   echo You need Python to use this!
   exit /B
)


:eof
py nolo.py
END && EXIT
