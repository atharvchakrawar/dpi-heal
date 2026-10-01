@echo off
title DPI-Heal Pytest Test Suite
color 0E
echo ===============================================================================
echo     RUNNING DPI-HEAL VERIFICATION AND INVARIANT TEST SUITE
echo ===============================================================================
echo.

py -3.13 main.py --test
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Trying fallback pytest launcher...
    pytest -v
)

echo.
pause
