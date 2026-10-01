@echo off
title DPI-Heal Autonomous Self-Healing Swarm Simulation
color 0B
echo ===============================================================================
echo     PROJECT DPI-HEAL: AUTONOMOUS SELF-HEALING MIDDLEWARE SWARM
echo     Digital Public Infrastructure (UPI / OCEN / DigiLocker Rail Protector)
echo ===============================================================================
echo.
echo Starting simulation...
echo.

py -3.13 main.py --simulate
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Trying fallback python launcher...
    python main.py --simulate
)

echo.
echo ===============================================================================
echo Simulation finished.
echo ===============================================================================
echo.
pause
