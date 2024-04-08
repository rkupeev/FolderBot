from sqlalchemy import String, create_engine

from app.core.settings import get_settings


engine = create_engine(get_settings().database.DATABASE_URL_psycopg)

