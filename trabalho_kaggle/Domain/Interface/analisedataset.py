import os
import pandas as pd

def carregar_dados(caminho_arquivo="trabalho_kaggle/Domain/Entities/dataset"):
    """
    Carrega os arquivos CSV do dataset da Fórmula 1 para análise.
    """
    try:
        arquivos = [f for f in os.listdir(caminho_arquivo) if f.endswith('.csv')]
        
        if not arquivos:
            raise FileNotFoundError("Nenhum arquivo CSV encontrado no diretorio do dataset.")
        
        dados = {}
        for arquivo in arquivos:
            caminho_completo = os.path.join(caminho_arquivo, arquivo)
            dados[arquivo] = pd.read_csv(caminho_completo)
            print(f"Arquivo carregado: {arquivo}")
        
        print("Todos os arquivos foram carregados com sucesso!")
        return dados
    
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

if __name__ == "__main__":
    dados = carregar_dados()