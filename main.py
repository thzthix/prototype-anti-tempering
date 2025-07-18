#import psycopg2
from config import DB_CONFIG
from sqlmodel import SQLModel, Field, Session, select
from config import engine
from model import Company

if __name__ == "__main__":
    #try:
        #conn = psycopg2.connect(**DB_CONFIG)
        #print("Connected to the database")
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            company = Company(name="교보생명", url="https://www.kyobo.com/dgt/web/dtm/lc/tu/login")
            session.add(company)
            session.commit()

        companies = session.exec(select(Company)).all()
        print("DB에 저장된 고객사 목록:")
        for c in companies:
            print(f"ID: {c.id}, Name: {c.name}, URL: {c.url}") 
        #conn.close()
    #except psycopg2.Error as e:
    #    print("database 연결 실패: ", e)