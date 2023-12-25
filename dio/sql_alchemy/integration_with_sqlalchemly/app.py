from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect 

base = declarative_base()


class User(base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    addres = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'


class Address(base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id =Column(Integer, ForeignKey('user_acount.id'), nullable=False)

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f'Address(id={self.id}, email={self.email_address})'
    

print(User.__tablename__)

# Conexão com o banco de dados
engine = create_engine('sqlite://')

# Criando as classe como tabela no banco de dados
base.metadata.create_all(engine)

#depreciado - será removido em futuro release
#print(engine.table_names())
inspetor_engine = inspect(engine)