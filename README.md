# Auto Trading Bot

echo "UPBIT_ACCESS_KEY=..." >> .env
echo "UPBIT_SECRET_KEY=..." >> .env

python -m venv .venv

echo '.env'  >> .gitignore
echo '.venv' >> .gitignore

ls -la

source .venv/bin/activate

pip install -r requirements.txt

python main.py


