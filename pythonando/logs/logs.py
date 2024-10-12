"""
CRITICAL: Erro grave que pode quebrar a sua aplicação, Ex.: dados de login, cartão de crédito, vazados..

ERROR: Erro que não faz a sua aplicação quebrar más, que precisa ser tratado, Ex.: usurio fez um
requisição HTTP ao banco de dados e não teve retorno.

WARNING: Não necessariamente é um erro más pode gerar estragos futuramente.

INFO: Formas de enviar informações, por exemplo: Usuario logou, usuàrio deslogou do sistema.

DEBUG: Geralmente utilizado só no desenvolvimento.

1ª - Importar levels

2ª - Importar a funcao basicConfig
  Configurar parâmetros
    - level: A partir deste nivel de gravidade as menssagens serão armazenadas.
    - filename: Onde irá ser armazenado Ex.: 'app.log'
    - filemode: Modo de abertura do arquivo 'a' (modulo de leitura e escrita de arquivos)

3ª - Importar as classes handlers
  Diz o modo como vai operar os seus logs por arquivo pelo console..., e também posso usar mais de um handler.
  - Tambem posso definir que no modo file_handler, receberei logs só a partir do level WARNING

  Ex.:
  file_handler = FileHandler('logs.log', 'a')
  file_handler.setLevel(WARNING)

  Ex.:
  stream_handler = StreamHandler()
  stream_handler.setLevel(DEBUG)

  - Posso adiconar filtros entendendo da Classe Filter

  Ex.:
  class Filtro(Filter):

    def filter(self, record):
        if 'cartão' in record.msg:
            record.msg = 'Vazou a senha do cartão'
            return True

  Adiconando filtro.: file_handler.addFilter(Filtro())

https://youtu.be/ZEoc1aSovfw?si=ZAo7NmMUmOaIsN4y
parei em: 12:59
"""

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import basicConfig
from logging import critical, error, warning, info, debug
from logging import FileHandler, StreamHandler, Filter


class Filtro(Filter):

    def filter(self, record):
        if 'cartão' in record.msg:
            record.msg = 'Vazou a senha do cartão'
            return True


file_handler = FileHandler('logs.log', 'a')
file_handler.setLevel(WARNING)
file_handler.addFilter(Filtro())

stream_handler = StreamHandler()





LOGS: dict[str, int | str] = {
    "level": DEBUG,
    "format": '%(levelname)s: %(asctime)s: %(message)s',
    "handlers": [file_handler, stream_handler]
}

basicConfig(**LOGS)

try:
    x: int = int(input('Digite um número: '))
    y = 10 / x
except ZeroDivisionError:
    warning('Tentou dividir por zero')

critical('Cartão 123456')