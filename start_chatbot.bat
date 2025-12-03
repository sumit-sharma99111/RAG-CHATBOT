@echo off
title RBI RAG Chatbot Launcher

echo 🧠 Checking for any running Streamlit processes...
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo 🚀 Starting RBI RAG Chatbot...
cd /d D:\RBI_RAG_Project

call .venv\Scripts\activate

echo 🌐 Launching Streamlit interface...
python -m streamlit run streamlit_app.py

pause


