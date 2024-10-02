# Importa o módulo subprocess, que permite executar comandos do sistema operacional
import subprocess
# Importa o módulo sys, que fornece acesso a algumas variáveis e funções específicas do interpretador Python
import sys

# Lista de bibliotecas necessárias para o funcionamento do programa
bibliotecas = ["customtkinter", "Pillow", "tkcalendar"]

def verificar_e_instalar(bibliotecas):
    # Função que verifica se as bibliotecas na lista estão instaladas e, se não, tenta instalá-las
    for biblioteca in bibliotecas:
        try:
            # Tenta importar a biblioteca. Se a importação for bem-sucedida, significa que a biblioteca já está instalada
            __import__(biblioteca)
            print(f"{biblioteca} já está instalada.")
        except ImportError:
            # Se a biblioteca não estiver instalada, um erro de importação ocorrerá
            print(f"{biblioteca} não está instalada. Instalando...")
            # Usa subprocess para executar o comando de instalação do pip no terminal
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
            # Informa que a instalação foi bem-sucedida
            print(f"{biblioteca} instalada com sucesso.")

# Chama a função que verifica e instala as bibliotecas necessárias
verificar_e_instalar(bibliotecas)
