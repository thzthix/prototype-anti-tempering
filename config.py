# config.py
from sqlmodel import create_engine, SQLModel
from typing import Dict

# 현재 PostgreSQL 연결 정보 (딕셔너리 형태)
DB_CONFIG: Dict[str, any] = {
    "host": "localhost",
    "port": 5432,
    "user": "proto",
    "password": "type",
    "database": "prototype",
}

# SQLModel을 위한 데이터베이스 URL 생성
# PostgreSQL 연결 형식: "postgresql://user:password@host:port/database"
DATABASE_URL = (
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# SQLModel 엔진 생성
# echo=True는 SQL 쿼리를 콘솔에 출력하여 디버깅에 도움을 줍니다.
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
