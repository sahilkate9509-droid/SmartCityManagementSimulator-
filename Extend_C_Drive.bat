@echo off
setlocal enabledelayedexpansion

:: Check for administrative permissions
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [INFO] Requesting administrator privileges...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process cmd -ArgumentList '/k \"\"%~f0\" admin\"' -Verb RunAs"
    exit /b
)

title Extend C: Drive - Automatic Partition Optimizer
color 0A

echo ======================================================================
echo                  EXTENDING C: DRIVE INTO FREE SPACE
echo ======================================================================
echo.
echo Step 1/5: Checking Windows Recovery (WinRE)...
reagentc /info
echo.

echo Step 2/5: Disabling WinRE to safely preserve recovery image on C:...
reagentc /disable
echo.

echo Step 3/5: Preparing diskpart instructions...
set DP_SCRIPT=%TEMP%\extend_c_diskpart.txt
(
echo select disk 0
echo select partition 4
echo delete partition override
echo select volume c
echo extend
) > "%DP_SCRIPT%"

echo Step 4/5: Deleting blocking recovery partition and extending C: drive...
diskpart /s "%DP_SCRIPT%"
del "%DP_SCRIPT%" 2>nul
echo.

echo Step 5/5: Re-enabling Windows Recovery (WinRE)...
reagentc /enable
reagentc /info
echo.

echo ======================================================================
echo                          SUCCESS!
echo ======================================================================
echo.
echo Current partition status:
powershell -NoProfile -Command "Get-Partition -DiskNumber 0 | Where-Object DriveLetter -eq 'C' | Select-Object DiskNumber, PartitionNumber, DriveLetter, @{N='Size (GB)';E={[math]::Round($_.Size/1GB, 2)}} | Format-Table -AutoSize"
echo.
echo Your C: drive has now been successfully expanded!
echo You can close this window now.
pause
