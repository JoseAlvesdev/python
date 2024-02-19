import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import sessionmaker

# Conexão com o banco
engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo=True)

# Declarando o mapeamento
Base = declarative_base()


class User(Base):
    __tablename__= 'users' # obrigatorio
    id = Column(Integer, primary_key = True) # obrigatorio
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return (
            f'User(name={self.name}, '
            f'fullname={self.fullname}, '
            f'age={self.age})'
        )

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Criar instancias da class User (tabela)
user = User(name='José', fullname='José Henrique da Silva Alves', age=20)

# Criar uma seção
Session = sessionmaker(bind=engine)

session = Session()

# Adicionar objetos (INSERT)
session.add(user); session.commit()
session.add_all(
    [
        User(name='Matheus', fullname='Matheus Lima', age=24),
        User(name='Felype', fullname='Felype Lima', age=26)
    ]
); session.commit()

print(User.__repr__)