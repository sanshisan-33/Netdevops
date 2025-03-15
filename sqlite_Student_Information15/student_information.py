from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker


engine= create_engine('sqlite:///sqlachemy_sqlite3.db?check_same_thread=False',)
Base = declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class UserHomeWork(Base):
    __tablename__='user_homework'
    id=Column(Integer,primary_key=True)
    student_name=Column(String(64),nullable=False,index=True)
    age=Column(Integer,nullable=False)
    homework_account=Column(Integer,nullable=False)
    last_update_time=Column(DateTime(timezone='Asia/Chongqing'),default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.homework_account} | 最后更新时间：{self}"