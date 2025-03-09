from Adapters.Repository.autenticadorkaggle import autenticar_kaggle

def executar_autenticacao():
    """
    Executa a autenticacao no Kaggle.
    """
    try:
        api = autenticar_kaggle()
        if api:
            print("Autenticacao bem-sucedida no Kaggle!")
        else:
            print("Falha na autenticacao.")
    except Exception as e:
        print(f"Erro ao autenticar: {e}")

if __name__ == "__main__":
    executar_autenticacao()
