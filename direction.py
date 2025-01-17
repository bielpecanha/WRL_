import os

def folder():
    # Obtém o diretório onde o script principal está localizado
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir)

def pasta_bd():
    # Define o caminho para o banco de dados relativo ao diretório base
    return os.path.join(folder(), "dados_bd")

def pasta_site():
    # Define o caminho para a pasta SITE relativo ao diretório base
    return os.path.join(folder(), "SITE")

