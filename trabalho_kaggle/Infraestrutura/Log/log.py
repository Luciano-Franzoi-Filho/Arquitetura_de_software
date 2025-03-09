import sys
import os
import io

# Função para salvar a saída da execução em arquivos txt
def salvar_log(funcao_nome, mensagens):
    """
    Cria um arquivo de log com base no nome da função e as mensagens geradas.
    """
    log_dir = 'trabalho_kaggle/Infraestrutura/Log' 
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f"{funcao_nome}.txt")
    
    with open(log_file, 'w') as f:
        for mensagem in mensagens:
            f.write(mensagem + "\n")
            
    print(f"Log salvo em {log_file}")

def capturar_saida(func, *args, **kwargs):
    """
    Captura a saída da função passada e a salva em um arquivo.
    """
    mensagens = []
    old_stdout = sys.stdout  
    sys.stdout = io.StringIO() 

    try:
        func(*args, **kwargs)
    except Exception as e:
        sys.stdout.write(f"Erro durante a execução: {e}\n")
    finally:
        mensagens = sys.stdout.getvalue().splitlines()  
        sys.stdout = old_stdout  

    salvar_log(func.__name__, mensagens)
