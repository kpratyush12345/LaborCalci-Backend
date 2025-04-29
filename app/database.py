from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres123_7pmq_user:5J6DErYMJEn7ZDPcqWqdu5Oj56DhW2kS@dpg-d084nbfgi27c7385crig-a.singapore-postgres.render.com/postgres123_7pmq"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
