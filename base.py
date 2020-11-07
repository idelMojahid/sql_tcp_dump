from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'titrit'
DB_USER = 'root'
DB_PWD = 'root'

mysql_con_string = 'mysql+pymysql://'+DB_USER + \
    ':'+DB_PWD+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME

engine = create_engine(mysql_con_string)
Session = sessionmaker(bind=engine)

Base = declarative_base()
