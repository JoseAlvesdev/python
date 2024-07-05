"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorator também são exempolos de Higher Order Functions;
- Decorator tem uma sintaxe própia, usando "@" (Syntack Sugar / Açucar Sintático)


|--------------------------------------------|
|           Function Decorator              |
---------------------------------------------

-------------------------------------------------------
|   |--------------------------------------------|   |
|   |        Function decorada                  |    |
|   --------------------------------------------     |
------------------------------------------------------

# Decorator como funções (Sintaxe não recomendada / Sem Açucar Sintático)

def seja_educado(function):
    def sendo():
        print('Foi um prazer conhecer você!')
        function()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Testando 1

# saudacao()

teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('Vai tormar no seu c* agente FDP.')


raiva_educada = seja_educado(raiva)
raiva_educada()

# Decorator com syntax Sugar (Açucar Sintático)


def seja_educado_mesmo(function):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        function()
        print('Tenha um excelente dia!')
    
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é José')


# Testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir!')


dormir()
"""
"""
---------------------------------------------------------
|   Home    | Serviços  | Produtos  |   Administrativo  |
---------------------------------------------------------

http://wwww.suaempresa.com.br/home

http://wwww.suaempresa.com.br/servicos

http://wwww.suaempresa.com.br/produtos

http://wwww.suaempresa.com.br/admin

# OSB: Não é código funcional (Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')


def home(request):
    return 'Pode acessar home'


def servicos(request):
    return 'Pode acessar serviços'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'


# OBS: Não confunda Decorator com Decorator Function
"""

