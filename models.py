from datetime import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(override=True)  # Load environment variables from .env file

DATABASE_URL = os.getenv(
    "POSTGRES_URL")  # Get the database URL from environment variables


Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)

    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    # def __repr__(self):
    #     return (
    #         f'UserModel(id={self.id}, first_name={self.first_name},'
    #         f'last_name={self.last_name}, birth={self.birth},'
    #         f'created={self.created})'
    #     )


users = [
    UserModel(first_name='Raj', last_name='Vachaparambil', birth=datetime(1987, 7, 2)),
    UserModel(first_name='Jerome', last_name='Kizhakkedath', birth=datetime(1987, 7, 2)),
]

session_maker = sessionmaker(bind=create_engine(DATABASE_URL))


def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()


if __name__ == '__main__':
    # First, let's insert the users into the database
    create_users()
    
    # Then query and print them out
    # with session_maker() as session:
    #     user_records = session.query(UserModel).all()
    #     for user in user_records:
    #         print(user.full_name)
