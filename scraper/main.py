import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlmodel import create_engine, SQLModel, Session
from models.Company import Company
from models.LoginWebPage import LoginWebPage
from contextlib import contextmanager
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")


engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created.")

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
    with get_session() as session:
        company = Company(name="교보문고", url="https://mmbr.kyobobook.co.kr/login", is_active=True)
        session.add(company)
        session.commit()
        print("db에 저장되었습니다.")


import time

if __name__ == "__main__":
    main()
    print("컨테이너가 종료되지 않도록 대기 중...")
    while True:
        time.sleep(60)
    