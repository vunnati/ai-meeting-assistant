from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String, nullable=False, unique=True)
    hashed_password = mapped_column(String, nullable=False)

# class Meeting(Base):
# __tablename__ = "meetings"

# id = mapped_column(Integer, primary_key = True)
# meeting_title = mapped_column(String, nullable = False)
# meeting_date = mapped_column(String, nullable=False)
# summary = mapped_column(String)
