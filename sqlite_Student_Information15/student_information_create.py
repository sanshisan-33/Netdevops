from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlachemy_sqlite3.db?check_same_thread=False', )
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class UserHomeWork(Base):
    __tablename__ = 'user_homework'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(64), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    homework_account = Column(Integer, nullable=False)
    last_update_time = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.__class__.__name__}(学员姓名：{self.student_name} | 学员年龄：{self.age} | " \
               f"{self.homework_account} | 最后更新时间：{self.last_update_time})"


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)

    homework_dict = [
        {'student_name': '张三', 'age': 37, 'homework_account': 1},
        {'student_name': '李四', 'age': 33, 'homework_account': 5},
        {'student_name': '王五', 'age': 32, 'homework_account': 10},
    ]

    for homework in homework_dict:
        homework_obj = UserHomeWork(**homework)
        session.add(homework_obj)

    session.commit()
    while True:
        print("请输入查询选项：")
        print("输入 1：查询整个数据库")
        print("输入 2：根据学员姓名查询")
        print("输入 3：根据学员年龄查询")
        print("输入 4：根据作业数量查询")
        print("输入 5：删除数据库内所有数据")
        print("输入 0：退出")

        choice = input("请输入查询选项：")

        if choice == '1':
            results = session.query(UserHomeWork).all()
            for result in results:
                print(result)
        elif choice == '2':
            name = input("请输入学员姓名：")
            results = session.query(UserHomeWork).filter_by(student_name=name).all()
            for result in results:
                print(result)
        elif choice == '3':
            age = int(input("搜索大于输入年龄的学员，请输入学员年龄: "))
            results = session.query(UserHomeWork).filter(UserHomeWork.age > age).all()
            for result in results:
                print(result)
        elif choice == '4':
            account = int(input("搜索大于输入作业数的学员,请输入作业数量:"))
            results = session.query(UserHomeWork).filter(UserHomeWork.homework_account > account).all()
            for result in results:
                print(result)
        # elif choice == '5':
        #     confirm = input("确定要删除数据库内所有数据吗？(y/n): ")
        #     if confirm.lower() == 'y':
        #         session.query(UserHomeWork).delete()
        #         session.commit()
        #         print("数据库内所有数据已删除。")
        elif choice == '0':
            break
        else:
            print("无效的输入，请重新输入！")
