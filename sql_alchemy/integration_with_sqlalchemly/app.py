from sqlalchemy import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

base = declarative_base()


class User(base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    addres = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )


class Address(base):
    id = Column(Integer, primary_key=True, auto_increment=True)
    email_address = Column(String(30), nullable=False)
    user_id =Column(Integer, ForeignKey('user_acount.id'), nullable=False)