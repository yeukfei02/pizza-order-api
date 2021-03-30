from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

DB_CONFIG = {}

fastapi_env = os.getenv('FASTAPI_ENV')

if fastapi_env == 'development':
    DB_CONFIG = {
        'user': 'donaldwu',
        'pw': '',
        'db': 'donaldwu',
        'host': 'localhost',
        'port': '5432',
    }
else:
    DB_CONFIG = {
        'user': 'donaldwu',
        'pw': 'donaldwu',
        'db': 'donaldwu',
        'host': 'db',
        'port': '5432',
    }

DB_URL = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_CONFIG['user'], DB_CONFIG['pw'], DB_CONFIG['host'], DB_CONFIG['port'], DB_CONFIG['db'])

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()
