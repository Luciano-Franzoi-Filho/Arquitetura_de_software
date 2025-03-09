import sys
import os

# Função para salvar a saída da execução em um arquivo txt
def salvar_log(funcao_nome, mensagens):
    """
    Cria um arquivo de log com base no nome da função e as mensagens geradas.
    """
    log_dir = 'trabalho_kaggle/Infraestrutura/Log'  # Diretorio de logs
    
    # Cria o diretório de logs se não existir
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Criação do caminho do arquivo de log
    log_file = os.path.join(log_dir, f"{funcao_nome}.txt")
    
    # Grava as mensagens no arquivo de log
    with open(log_file, 'w') as f:
        for mensagem in mensagens:
            f.write(mensagem + "\n")
            
    print(f"Log salvo em {log_file}")

# Função para capturar a saída de uma função
def capturar_saida(func, *args, **kwargs):
    """
    Captura a saída da função passada e a salva em um arquivo.
    """
    # Redireciona a saída padrão para capturar os prints
    mensagens = []
    sys.stdout = sys.__stdout__  # Restabelece a saída padrão
    
    def redirecionar_output(msg):
        mensagens.append(msg)
    
    sys.stdout = redirecionar_output  # Captura a saída das funções chamadas
    
    func(*args, **kwargs)
    
    # Salva a saída capturada no arquivo de log
    salvar_log(func.__name__, mensagens)