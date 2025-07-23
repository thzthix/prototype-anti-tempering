import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlmodel import create_engine, SQLModel, Session
from models.Company import Company
from models.LoginWebPage import LoginWebPage
from contextlib import contextmanager
from apscheduler.schedulers.background import BackgroundScheduler
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")


engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created.")

def insert_test_data():
    with get_session() as session:
        company = Company(name="교보문고"+str(time.time()), url="https://mmbr.kyobobook.co.kr/login", is_active=True)
        session.add(company)
        session.commit()
        session.refresh(company)
        print(f"Company 저장: {company.id}, {company.name}")
        # LoginWebPage 데이터 생성
        login_page = LoginWebPage(url="https://mmbr.kyobobook.co.kr/login", company_id=company.id)
        session.add(login_page)
        session.commit()
        print("========================================Scrapper 데이터 삽입==========================================\n")
        print(f"LoginWebPage 저장: {login_page.id}, {login_page.url}, company_id={login_page.company_id}")
        print("db에 저장되었습니다.")

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def main():
    create_db_and_tables()
    print("Scraper service started. Performing scraping and saving data...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(insert_test_data, 'interval', seconds=60)
    scheduler.start()
    try:
        while True:
            time.sleep(30)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


import time

if __name__ == "__main__":
    main()
    print("컨테이너가 종료되지 않도록 대기 중...")
    while True:
        time.sleep(60)
    