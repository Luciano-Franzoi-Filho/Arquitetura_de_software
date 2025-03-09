import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

def autenticar_kaggle():
    """
    Autentica no Kaggle usando o arquivo de credenciais localizado na pasta padrao ~/.kaggle/kaggle.json.
    """
    try:
        # Verifica se o arquivo de credenciais existe
        credenciais_path = os.path.expanduser("~/.kaggle/kaggle.json")
        if not os.path.exists(credenciais_path):
            raise FileNotFoundError("Arquivo kaggle.json nao encontrado na pasta ~/.kaggle. Certifique-se de que ele esta la.")
        
        os.chmod(credenciais_path, 0o600)
        
        # Inicializa a API do Kaggle
        api = KaggleApi()
        api.authenticate()
        print("Autenticacao no Kaggle realizada com sucesso!")
        return api
    
    except Exception as e:
        print(f"Erro na autenticacao do Kaggle: {e}")
        return None

if __name__ == "__main__":
    autenticar_kaggle()
