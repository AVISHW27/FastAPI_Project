from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAlchemyDatabaseURL = "sqlite:///./blog.db"
#engine = create_engine("sqlite:///blog.db", echo=True)
engine = create_engine(SQLAlchemyDatabaseURL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()



# Is code mein SQLAlchemy (ORM) ka use karke Database Connection (Database Engine) setup kiya ja raha hai. 
# Simple words mein: yeh aapki FastAPI application ko SQLite Database (blog.db) se connect karne ke liye Zameen/Foundation taiyar kar raha hai.