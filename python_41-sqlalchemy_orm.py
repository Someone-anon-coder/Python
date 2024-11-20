from sqlalchemy import create_engine

engine = create_engine('sqlite:///Database/example_alchemy.db', echo=True)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.age}')>"

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

user = User(name='Someone', age=100)
session.add(user)
session.commit()

user = User(name='Someone Else', age=84)
session.add(user)
session.commit()


users = session.query(User).all()
for user in users:
    print(user)

user = session.query(User).filter_by(id=1).first()
print(user)


user1 = session.query(User).filter_by(name="Someone").first()
user1.age = 101
session.commit()

session.delete(session.query(User).filter_by(name="Someone Else").first())
session.commit()


users = session.query(User).all()
for user in users:
    print(user)

session.close()