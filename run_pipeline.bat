@echo off

REM === Detect if env312 is already activated ===
REM Check if the PATH contains "env312\Scripts"
echo %PATH% | findstr /I "env312\Scripts" >nul
if %ERRORLEVEL%==0 (
    echo (env312 already activated)
) else (
    echo Activating env312...
    call env312\Scripts\activate
)

echo.
echo === Step 1: Extract PDFs ===
python utilities\convert_pdfs.py

echo.
echo === Step 2: Clean generated .txt files ===
python utilities\clean_existing_output.py

echo.
echo === Step 3: Validate cleaned files ===
python utilities\validate_clean_output.py

echo.
echo === All done! ===
pause
"@ | Out-File -Encoding ascii run_pipeline.bat
