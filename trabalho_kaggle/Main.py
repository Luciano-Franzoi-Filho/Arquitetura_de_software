from Application.Use_Cases.informacoesdataset import exibir_informacoes_base
from Application.Use_Cases.relatoriosdataset import gerar_relatorio
from Domain.Entities.downloaddataset import baixar_dataset
from Adapters.Repository.autenticadorkaggle import autenticar_kaggle
from Infraestrutura.Log.log import capturar_saida  

def main():
    """
    Ponto de entrada do projeto. Executa autenticação, baixa o dataset e exibe informações.
    """
    print("Iniciando o sistema...")

    api = autenticar_kaggle()
    if not api:
        print("Erro na autenticação. Encerrando...")
        return
    
    capturar_saida(baixar_dataset, api)
    
    capturar_saida(exibir_informacoes_base)

    capturar_saida(gerar_relatorio)
    
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()