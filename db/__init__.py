from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


conn = 'sqlite:///weather.db?check_same_thread=false'
engine = create_engine(conn)


Base = declarative_base()



Session = sessionmaker(bind=engine)
session = Session()