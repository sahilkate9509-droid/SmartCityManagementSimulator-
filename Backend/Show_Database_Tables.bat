@echo off
title Smart City Database Viewer
cd /d "%~dp0"
echo ========================================================
echo   Smart City Simulator - Database Viewer
echo ========================================================
echo Extracting latest tables from smartcity.db ...
python export_html.py
if exist database_report.html (
    echo Opening Database Report in your web browser...
    start database_report.html
) else (
    echo Falling back to terminal inspector...
    python view_db.py
    pause
)
