from .Application.Use_Cases.informacoesdataset import exibir_informacoes_base
from .Application.Use_Cases.relatoriosdataset import gerar_relatorio
from .Domain.Entities.downloaddataset import baixar_dataset
from .Adapters.Repository.autenticadorkaggle import autenticar_kaggle

def main():
    """
    Ponto de entrada do projeto. Executa autenticação, baixa o dataset e exibe informações.
    """
    print("Iniciando o sistema...")
    
    # Autenticação no Kaggle
    api = autenticar_kaggle()
    if not api:
        print("Erro na autenticação. Encerrando...")
        return
    
    # Baixar dataset
    baixar_dataset(api)
    
    # Exibir informações do dataset
    exibir_informacoes_base()
    
    # Gerar relatório
    gerar_relatorio()
    
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
