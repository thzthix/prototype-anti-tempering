import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.LoginWebPage import LoginWebPage
from sqlmodel import create_engine, Session, SQLModel
from models.Company import Company
from sqlmodel import select
from contextlib import contextmanager
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
def main():
    print("Exporter 모듈 시작")
    with get_session() as session:
        companies = session.exec(select(Company)).all()
        for company in companies:
            print(f"ID: {company.id}, Name: {company.name}, Active: {company.is_active}")

import time

if __name__ == "__main__":
    main()
    print("컨테이너가 종료되지 않도록 대기 중...")
    while True:
        with get_session() as session:
            companies = session.exec(select(Company)).all()
            for company in companies:
                print("========================================Exporter 데이터 읽기==========================================\n")
                print(f"ID: {company.id}, Name: {company.name}, Active: {company.is_active}")
                web_pages = session.exec(select(LoginWebPage).where(LoginWebPage.company_id == company.id)).all()
                for web_page in web_pages:
                    print(f"WebPage: {web_page.id}, URL: {web_page.url}, Company ID: {web_page.company_id}")
        time.sleep(10)