call venv\Scripts\activate.bat
rmdir /S /Q frequency-analysis-exe
python cx.py build
echo DONE
pause >nul