::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFCtGTRCKPWaGIrof/eX+4f6Unm4SUOcPaoDR37eaM9wj81HsepgA33RTqNkDBh5bai6iYw4zrH1+umuCOImVsACB
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFCtGTRCKPWaGIrof/eX+4f6Unm4SUOcPaoDR37eaM9wj81HsepgA33RTqNkDBh5bai6ZWyF6rHZH1g==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
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