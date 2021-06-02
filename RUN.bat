if exist smdv-env\ (
  echo Yes
) else (
  pip install virtualenv
  virtualenv smdv-env
  CALL smdv-env/Scripts/activate.bat
  pip install -r requirements.txt
)
CALL smdv-env/Scripts/activate.bat
start pythonw.exe main.pyw
exit