@echo off	
setlocal enableextensions
echo .
echo            Concourse Package Extractor
echo .
echo .
echo    The contents of the selected package will be
echo    extracted to the 'L' drive of this machine.
echo .
rem
rem Extract the contents of the package.
rem
if exist L:\Prj\CpsPkgCapstone\Compressed goto CPEX_7z
echo *** ERROR: location was not found at L:\Prj\CpsPkgCapstone\Compressed
errlevel 1
goto :CPEX_End

:CPEX_7z
rem
rem    Ask user for the total number of processors to perform extraction
rem
set /p nbrprcr="How many processors would you like to use to perform the extract? "

@echo Started: %date% %time%
echo --- Removing previous install of CpsPkg ---
call cmd /c F:\USERS\Zilli\Capstone\RemovePreviousExtract.bat Extract 2> nul
echo --- Extracting ---
python Extract.py L:\Prj\CpsPkgCapstone\Compressed %nbrprcr%
@echo Ended: %date% %time%
goto :CPEX_End

:CPEX_End
endlocal