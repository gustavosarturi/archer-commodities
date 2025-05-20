@echo off
echo Ativando ambiente virtual...
call .venv\Scripts\activate.bat

echo Instalando dependências...
pip install -r requirements.txt

echo Iniciando Streamlit...
streamlit run app.py

pause
