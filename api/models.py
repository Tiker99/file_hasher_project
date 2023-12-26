import os

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class FileData(Base):
    __tablename__ = "files"
    id = Column(String, primary_key=True)
    md5_hash = Column(String)


DB_USERNAME = 'boston'
DB_PASS = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = 'postgres'
DB_NAME = 'boston'

connection_string = f"postgresql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
