import os
from kaggle.api.kaggle_api_extended import KaggleApi

def baixar_dataset(api, dataset="rohanrao/formula-1-world-championship-1950-2020", destino="trabalho_kaggle/Domain/Entities/dataset"):
    """
    Baixa o dataset da Formula 1 do Kaggle.
    """
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
        
        print(f"Baixando dataset {dataset} para {destino}...")
        api.dataset_download_files(dataset, path=destino, unzip=True)
        print("Download concluido e arquivos extraidos com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar dataset: {e}")

if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()
    baixar_dataset(api)