@echo off
title Smart City Backend Server
echo ========================================================
echo   Smart City Simulator - Backend API Server
echo ========================================================
echo Starting server on http://127.0.0.1:8000 ...
echo Documentation:   http://127.0.0.1:8000/docs
echo ========================================================
python -m uvicorn app.main:app --reload --port 8000
pause
