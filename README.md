# AutoTrading Bot

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

    chmod +x run.sh

    sh ./run.sh

python 가상환경 deactivate

    deactivate

참고.특정문자열 검색 (KEY 저장여부 확인시)

    grep -rni "0x" .

    -r : 하위 디렉토리를 포함하여 디렉토리 내의 모든 파일을 재귀적으로 검색 (--recursive)
    -n : 출력 행과 함께 행 번호 표시 (--line-number)
    -i : 대소문자 구분하지 않음 (-ignore)
