# Python 3.11-slim을 기반 이미지로 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# models 모듈 복사 및 설치
COPY models/ ./models
#RUN pip install ./models

# exporter 모듈 복사 및 설치
COPY exporter ./exporter
RUN pip install ./exporter

# 컨테이너 실행 시 실행될 명령어
CMD ["python", "./exporter/main.py"]