#import psycopg2
from config import DB_CONFIG
from sqlmodel import SQLModel, Field, Session, select
from config import create_db_and_tables, engine
from Models.Company import Company
from Models.LoginWebPage import LoginWebPage

if __name__ == "__main__":
    #try:
        #conn = psycopg2.connect(**DB_CONFIG)
        #print("Connected to the database")
        create_db_and_tables()
        with Session(engine) as session:
            company_1 = Company(name="교보생명", is_active=True)
            company_2 = Company(name="교보문고", is_active=True)
        
            session.add(company_1)
            session.add(company_2)
            session.commit()
            session.refresh(company_1)
            session.refresh(company_2)
            company_1_id = company_1.id
            company_2_id = company_2.id
            company_1_web_page = LoginWebPage(url="https://www.kyobo.com/dgt/web/dtm/lc/tu/login", company_id=company_1.id)
            company_2_web_page = LoginWebPage(url="https://mmbr.kyobobook.co.kr/login", company_id=company_2.id)
            session.add(company_1_web_page)
            session.add(company_2_web_page)
            session.commit()
        with Session(engine) as session:
            company_1_web_page = session.exec(select(LoginWebPage).where(LoginWebPage.company_id == company_1_id)).first()
            company_2_web_page = session.exec(select(LoginWebPage).where(LoginWebPage.company_id == company_2_id)).first()
            print(f"company_1_web_page: {company_1_web_page.url}")
            print(f"company_2_web_page: {company_2_web_page.url}")
