from sqlalchemy import create_engine
from sqlalchemy import text


DATABASE_URL = "postgresql+psycopg://unnati@localhost:5432/ai_meeting_assistant"
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.scalar())