@echo off
set VENV_PY=C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise\.venv\Scripts\python.exe
cd /d C:\Users\nswcl\.gemini\antigravity-ide\scratch\the-floor-that-does-not-rise

echo [RUNNING] 07_run_all_models.py...
%VENV_PY% -u scripts\07_run_all_models.py
if errorlevel 1 goto error

echo [RUNNING] 08_make_tables.py...
%VENV_PY% -u scripts\08_make_tables.py
if errorlevel 1 goto error

echo [RUNNING] 09_make_figures.py...
%VENV_PY% -u scripts\09_make_figures.py
if errorlevel 1 goto error

echo [RUNNING] pytest -q...
%VENV_PY% -m pytest -q
if errorlevel 1 goto error

echo [SUCCESS] All models, tables, figures, and tests completed successfully!
exit /b 0

:error
echo [ERROR] Pipeline failed at step!
exit /b 1
