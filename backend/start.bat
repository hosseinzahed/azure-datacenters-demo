@echo off
REM Start script for the Azure Datacenters API (Windows)

echo Starting Azure Datacenters API...

REM Check if .env file exists
if not exist .env (
    echo Warning: .env file not found. Creating from .env.example...
    copy .env.example .env
    echo Please update .env with your database credentials before running the application.
    exit /b 1
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Start the server
echo Starting server on http://localhost:8000
uvicorn main:app --reload --host 0.0.0.0 --port 8000
