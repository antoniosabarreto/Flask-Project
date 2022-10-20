import os
import random, string


class Config:
    CSRF_ENABLED = True  # Habilita o uso de criptografia nas sessões do Flask
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'  # Será usada para criar chaves criptográficas em
    # alguns momentos
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') # Caminho em que os
    # arquivos de template ficarão no prjeto
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))# Pasta raiz do projeto. Será usada quando quisermos salvar
    # arquivos
    APP = None #Constante que receberá a propriedade do app. Inicia com valor nulo.
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/test.db'.format(ROOT_DIR)



'''
Usaremos algums constantes com valores distintos para cada ambiente, conforme especificado nas classes a seguir.
1. TESTING:  Constante que habilita o ambiente de teste no Flask. Com ela, alguns recursos de warning e 
erros ficam habilitados para exibição.
2. DEBUG: Essa constante habilita/desabilita os debugs que o pytjon exibe o console durante a execução.
3. IP_HOST: Usaremos essa constante pra informar o IP da máquina em que estamos executando o projeto.
4. PORT_HOST: A porta em que a aplicação web executrá.
5. URL_MAIN: Essa constante une o endereço IP com a porta para gerar o endereço principal da aplicação.
6. app_config:  Possui 3 configurações e será usada para detreminar qual configuração estamos usando.
7. app_active: Ela receberá um dos três valores presentes em app_config: 'development', 'testing' ou 'production'.
'''


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/'.format(IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'  # Substituir pelo ip da máquina de testes, caso queira fazer testes em produção
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/'.format(IP_HOST, PORT_HOST)


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'  # Substituir pelo ip da máquina de testes, caso queira colocar a aplicação em produção
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/'.format(IP_HOST, PORT_HOST)


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')