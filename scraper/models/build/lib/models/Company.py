from sqlmodel import SQLModel, Field, create_engine, Session
class Company(SQLModel, table=True):
    __tablename__ = "company"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    is_active: bool