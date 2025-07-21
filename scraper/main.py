import os
from sqlmodel import create_engine, SQLModel, Session
from models.Company import Company
from models.LoginWebPage import LoginWebPage

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")


engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created.")

def get_session():
    with Session(engine) as session:
        yield session

def main():
    create_db_and_tables()
    print("Scraper service started. Performing scraping and saving data...")


if __name__ == "__main__":
    main()