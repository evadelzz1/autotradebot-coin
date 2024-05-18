# Auto Trading Bot

소스코드 다운로드

    git clone https://github.com/evadelzz1/autotradebot-coin.git


python 가상환경 activate 및 필요한 라이브러리 설치

    cd ./autotradebot-coin

    pyenv versions

    pyenv local 3.11.6

    python -m venv .venv

    source .venv/bin/activate

    pip install -r requirements.txt

코드 실행

    echo "UPBIT_ACCESS_KEY=..." >> .env
    echo "UPBIT_SECRET_KEY=..." >> .env

    python ./source/....py

python 가상환경 deactivate

    deactivate

