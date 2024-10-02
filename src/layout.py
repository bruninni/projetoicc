from utils import carregarImagem
import customtkinter as tk


from utils import carregarImagem  # Importa a função 'carregarImagem' do módulo 'utils'
import customtkinter as tk  # Importa a biblioteca CustomTkinter como 'tk'

# Função para deslogar o usuário e fechar a janela
def logout(janela):
    print("Usuário deslogado!")  # Imprime mensagem de deslogamento no console
    janela.destroy()  # Fecha a janela principal da aplicação

# Função para criar a barra superior da interface
def criarBarraTopo(janela, nome_usuario="usuário"):
    # Cria um frame para a barra superior com altura de 50 pixels, cor de fundo e cantos arredondados
    barra_topo = tk.CTkFrame(janela, height=50, fg_color="#66A0F8", corner_radius=0)
    
    # Posiciona a barra na grade, ocupando a linha 0 e todas as colunas
    barra_topo.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Saudação ao usuário, mostrando o nome dele
    label_saudacao = tk.CTkLabel(
        barra_topo,  # O rótulo será adicionado à barra superior
        text=f"Olá, {nome_usuario}",  # Mensagem de saudação formatada com o nome do usuário
        font=tk.CTkFont(size=16),  # Define a fonte do texto com tamanho 16
        text_color="white"  # Define a cor do texto como branco
    )
    
    # Posiciona o rótulo na barra superior
    label_saudacao.grid(row=0, column=1, padx=(0, 5), pady=10, sticky="e")

    # Botão para sair da aplicação
    btn_sair = tk.CTkButton(
        barra_topo,  # O botão será adicionado à barra superior
        text="Sair",  # Texto exibido no botão
        width=50,  # Largura do botão
        fg_color="red",  # Cor de fundo do botão
        text_color="white",  # Cor do texto do botão
        command=lambda: logout(janela)  # Define a função 'logout' como comando ao clicar no botão
    )
    
    # Posiciona o botão na barra superior
    btn_sair.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="e")

    # Configuração das colunas dentro da barra para ajustar o layout
    barra_topo.grid_columnconfigure(0, weight=0)  # Coluna 0 para ícone de casa (não expansível)
    barra_topo.grid_columnconfigure(1, weight=1)  # Coluna 1 para saudação (expansível para ocupar o espaço disponível)
    barra_topo.grid_columnconfigure(2, weight=0)  # Coluna 2 para o botão de sair (não expansível)


def criarTitulo(janela):
    # Define a função 'criarTitulo' que recebe um parâmetro 'janela', que é a janela onde o título será adicionado
    
    # Cria um rótulo (label) utilizando o CustomTkinter
    label_titulo = tk.CTkLabel(
        janela,  # A janela onde o rótulo será adicionado
        text="Menu Principal",  # O texto que será exibido no rótulo
        font=tk.CTkFont(size=30, weight="bold"),  # Define a fonte do texto, com tamanho 30 e negrito
        text_color="#66A0F8"  # Define a cor do texto utilizando um código hexadecimal
    )
    
    # Posiciona o rótulo na grade (grid) da janela
    label_titulo.grid(
        row=1,  # Define que o rótulo será colocado na linha 1
        column=0,  # Define que o rótulo será colocado na coluna 0
        columnspan=3,  # O rótulo ocupa 3 colunas, centralizando-se na janela
        pady=20,  # Adiciona um espaçamento vertical de 20 pixels acima e abaixo do rótulo
        sticky="n"  # Alinha o rótulo na parte superior (norte) da célula da grade
    )



        

        