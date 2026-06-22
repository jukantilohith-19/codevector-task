from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)