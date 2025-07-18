from sqlmodel import SQLModel, Field
class LoginWebPage(SQLModel, table=True):
    __tablename__ = "login_web_page"
    id: int | None = Field(default=None, primary_key=True)
    url: str
    company_id:int = Field(default=None, foreign_key="company.id")

