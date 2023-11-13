import os

# Verificar o sistema operacional
sistema_operacional = os.name

# Comando para desligar o sistema
comando_desligar = ""

# Verificar o sistema operacional e definir o comando adequado
if sistema_operacional == "posix":  # Para sistemas baseados em Unix (Linux, macOS)
    comando_desligar = "shutdown -h now"
elif sistema_operacional == "nt":  # Para sistemas Windows
    comando_desligar = "shutdown /s /t 1"
else:
    print("Sistema operacional não suportado para desligamento.")
    exit()

# Executar o comando de desligamento
os.system(comando_desligar)
