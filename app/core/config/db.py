from typing import Generator
from sqlmodel import create_engine, Session

# Thay thế bằng chuỗi kết nối PostgreSQL của bạn
# Format: postgresql://user:password@host:port/dbname
DATABASE_URL = "postgresql://postgres:password@localhost:5432/my_database"

# echo=True để hiển thị log các câu truy vấn SQL (Nên đặt False khi lên Production)
engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
