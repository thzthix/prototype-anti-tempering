import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlmodel import create_engine, Session, SQLModel
import prometheus_client
from MetricsCollector import MetricsCollector
from MetricsHandler import MetricsHandler

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(DATABASE_URL, echo=True)

if __name__ == "__main__":
    print("Prometheus Exporter 시작 - 포트 8000")
    
    custom_registry = prometheus_client.CollectorRegistry()
    
    collector = MetricsCollector(engine)
    custom_registry.register(collector)
    prometheus_client.start_http_server(8000, registry=custom_registry)
    
    
    # 컨테이너가 계속 실행되도록 유지
    while True:
        time.sleep(60)
        print("Exporter 실행 중...")