from http import server
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.LoginWebPage import LoginWebPage
from models.Company import Company
from sqlmodel import create_engine, Session, SQLModel

from contextlib import contextmanager
#from MetricsHandler import MetricsHandler
from http.server import HTTPServer
import prometheus_client
from MetricsCollector import MetricsCollector

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(DATABASE_URL, echo = True) # SQL 쿼리 출력
@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
#def main():
    # print("Exporter 모듈 시작")
    # with get_session() as session:
    #     companies = session.exec(select(Company)).all()
    #     for company in companies:
    #         print(f"ID: {company.id}, Name: {company.name}, Active: {company.is_active}")
    #server = HTTPServer(("0.0.0.0", 8000), MetricsHandler)
    #erver = 
    
   # while True:

import time

if __name__ == "__main__":
    print("Server started on port 8000")
    collector = MetricsCollector(engine)
    prometheus_client.REGISTRY.register(collector)
    prometheus_client.start_http_server(8000)
    while True:
        time.sleep(10)
        print("Metrics collected")