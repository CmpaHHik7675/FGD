from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Іван")
session.add(new_user)
session.commit()

users = session.query(User).all()
print("Користувачі в базі даних:")
for user in users:
    print(f"ID: {user.id}, Name: {user.name}")
