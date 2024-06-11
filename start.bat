@echo off

REM Navigate to python-backend directory and start the Flask backend
echo Starting Python backend...
cd python-backend
py -m pip install -r requirements.txt
start "Flask Backend" /B py -m app

REM Wait for the backend to start
timeout /t 5 >nul

REM Navigate to electron-frontend directory and start the Electron app
echo Starting Electron frontend...
cd ../electron-frontend
@REM npm install
start "Electron Frontend" /B npm start

REM Wait for the user to terminate the script
pause
