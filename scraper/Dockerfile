# Python 3.11-slim을 기반 이미지로 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# models 모듈 복사 및 설치
COPY models/ ./models
#RUN pip install ./models

# scraper 모듈 복사 및 설치
COPY scraper ./scraper
RUN pip install ./scraper

COPY scraper/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# 컨테이너 실행 시 실행될 명령어
CMD ["python", "./scraper/main.py"]
