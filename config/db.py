from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from CSVManager.CSVManager import settings

username: str = settings.PSQL_USERNAME
password: str = settings.PSQL_PASSWORD
host: str = settings.PSQL_HOST
port: str = settings.PSQL_PORT
database: str = settings.PSQL_DB

database_url: str = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url, pool_size=50, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)