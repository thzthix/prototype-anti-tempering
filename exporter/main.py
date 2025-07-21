import os
from sqlmodel import create_engine, Session, SQLModel
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(DATABASE_URL, echo = True) # SQL 쿼리 출력
def main():
    print("Exporter 모듈 시작")
def get_session():
    with Session(engine) as session:
        yield session
if __name__ == "__main__":
    main()