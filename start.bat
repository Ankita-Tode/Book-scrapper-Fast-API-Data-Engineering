@echo off
REM Activate virtual environment
call .venv\Scripts\activate

REM Run FastAPI with uvicorn
python -m uvicorn main:app --reload

pause