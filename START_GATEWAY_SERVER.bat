@echo off
title DPI-Heal FastAPI Live Gateway Server
color 0A
echo ===============================================================================
echo     LAUNCHING DPI-HEAL FASTAPI SERVER (http://127.0.0.1:8000)
echo ===============================================================================
echo.
echo Opening interactive Swagger API Documentation in your browser...
start http://127.0.0.1:8000/docs
echo.
echo Starting FastAPI with Uvicorn...
echo Press CTRL+C to stop the server anytime.
echo.

py -3.13 main.py --serve
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Trying fallback python launcher...
    python main.py --serve
)

pause
