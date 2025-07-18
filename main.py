import psycopg2
from config import DB_CONFIG

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to the database")
        conn.close()
    except psycopg2.Error as e:
        print("database 연결 실패: ", e)