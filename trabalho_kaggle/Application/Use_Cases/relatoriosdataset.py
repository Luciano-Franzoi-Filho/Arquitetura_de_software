import pandas as pd
import sweetviz as sv
import dtale
import autoviz.AutoViz_Class as AutoViz
from Domain.Interface.analisedataset import carregar_dados

def gerar_relatorio():
    """
    Gera um relatorio detalhado sobre o dataset da Formula 1 usando Sweetviz, D-Tale e AutoViz.
    """
    try:
        dados = carregar_dados()
        if not dados:
            print("Nenhum dado foi carregado. Verifique o diretorio do dataset.")
            return
        
        print("\n--- Relatório do Dataset de Fórmula 1 ---\n")
        for nome_arquivo, df in dados.items():
            print(f"Arquivo: {nome_arquivo}")
            print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
            print("Colunas:", df.columns.tolist())
            print(df.head(), "\n")
            
            # Gerar relatório com Sweetviz
            print(f"Gerando relatorio Sweetviz para {nome_arquivo}...")
            report = sv.analyze(df)
            report.show_html(f"sweetviz_report_{nome_arquivo}.html")
            
            # Abrir D-Tale para visualização interativa
            print(f"Iniciando interface D-Tale para {nome_arquivo}...")
            dtale.show(df)
            
            # Gerar relatório AutoViz
            print(f"Gerando relatorio AutoViz para {nome_arquivo}...")
            AV = AutoViz.AutoViz_Class()
            AV.AutoViz(filename="", dfte=df)

        print("Relatorios gerados com sucesso!")
    
    except Exception as e:
        print(f"Erro ao gerar relatorio: {e}")

if __name__ == "__main__":
    gerar_relatorio()
