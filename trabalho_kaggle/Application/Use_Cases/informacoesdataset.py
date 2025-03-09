from trabalho_kaggle.Domain.Entities.downloaddataset  import carregar_dados

def exibir_informacoes_base():
    """
    Exibe informacoes detalhadas da base de dados da Formula 1.
    """
    try:
        dados = carregar_dados()
        if not dados:
            print("Nenhum dado foi carregado. Verifique o diretorio do dataset.")
            return
        
        print("\n--- Informacoes da Base de Dados de Formula 1 ---\n")
        for nome_arquivo, df in dados.items():
            print(f"Arquivo: {nome_arquivo}")
            print("Resumo estatistico:")
            print(df.describe(), "\n")
            print("Informacoes do DataFrame:")
            print(df.info(), "\n")
        
        print("Informacoes exibidas com sucesso!")
    
    except Exception as e:
        print(f"Erro ao exibir informacoes da base: {e}")

if __name__ == "__main__":
    exibir_informacoes_base()
