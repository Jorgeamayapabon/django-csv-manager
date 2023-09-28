from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

username = config('PSQL_USERNAME')
password = config('PSQL_PASSWORD')
host = config('PSQL_HOST')
port = config('PSQL_PORT')
database = config('PSQL_DB')

database_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url, pool_size=50, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)