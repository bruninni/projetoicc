import os  # Importa o módulo 'os' para interagir com o sistema de arquivos
from PIL import Image  # Importa a classe 'Image' do módulo PIL (Python Imaging Library) para manipulação de imagens
import customtkinter as tk  # Importa a biblioteca CustomTkinter, que é uma extensão do tkinter para criar interfaces gráficas personalizadas

def carregarImagem(caminhoRelativo, largura=40, altura=40):
    # Define a função 'carregarImagem' que recebe um caminho relativo e as dimensões da imagem (largura e altura)
    
    caminho = os.path.join(os.getcwd(), caminhoRelativo)  # Combina o diretório atual com o caminho relativo fornecido para obter o caminho absoluto da imagem
    if os.path.exists(caminho):  # Verifica se o arquivo de imagem existe no caminho especificado
        # Se a imagem existir, carrega a imagem usando a biblioteca PIL e cria um objeto CTkImage com as dimensões especificadas
        return tk.CTkImage(light_image=Image.open(caminho), size=(largura, altura))
    else:
        # Se a imagem não for encontrada, imprime uma mensagem de erro com o caminho onde foi procurada
        print(f"Imagem não encontrada em => {caminho}")
