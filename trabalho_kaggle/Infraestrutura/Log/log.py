import sys
import os
import io

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
    # Usando StringIO para capturar a saída sem interferir em sys.stdout
    mensagens = []
    old_stdout = sys.stdout  # Salva a saída padrão original
    sys.stdout = io.StringIO()  # Redireciona a saída para um buffer

    try:
        func(*args, **kwargs)
    except Exception as e:
        # Se ocorrer erro durante a execução, salva a mensagem de erro
        sys.stdout.write(f"Erro durante a execução: {e}\n")
    finally:
        # Captura tudo que foi impresso
        mensagens = sys.stdout.getvalue().splitlines()  # Captura a saída gerada
        sys.stdout = old_stdout  # Restaura a saída padrão

    # Salva a saída capturada no arquivo de log
    salvar_log(func.__name__, mensagens)
