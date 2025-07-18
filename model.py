from sqlmodel import SQLModel, Field, create_engine, Session
class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    url: str