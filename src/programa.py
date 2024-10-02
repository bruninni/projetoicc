# Importando as bibliotecas necessárias
import customtkinter as ctk  # Biblioteca para criar interfaces gráficas com Tkinter
from layout import criarBarraTopo, criarTitulo  # Funções personalizadas para criar elementos de layout
from utils import carregarImagem  # Função personalizada para carregar imagens
from tkcalendar import DateEntry  # Para criar campos de data
from tkinter import ttk  # Importa o módulo ttk para usar Treeview e outros widgets
import time  # Biblioteca para controlar o tempo


# Definindo tipos de suíte disponíveis
tipos_suite = ["Standard", "Vip", "Presidencial"]
# Capacidades máximas de hóspedes para cada tipo de suíte
capacidades = [3, 2, 1]  
# Contador de reservas para cada tipo de suíte
reservas = [0, 0, 0]  
# Lista para armazenar os hóspedes cadastrados
hospedes = []  

# Função para verificar se o CPF já está cadastrado
def cpfJaCadastrado(cpf):
    # Itera sobre a lista de hóspedes
    for hospede in hospedes:
        # Se encontrar um hóspede com o mesmo CPF, retorna True
        if hospede["cpf"] == cpf:
            return True
    # Se não encontrar, retorna False
    return False

# Função para verificar a disponibilidade de uma suíte
def verificarDisponibilidade(tipoDeSuite):
    # Obtém o índice do tipo de suíte na lista
    indice_suite = tipos_suite.index(tipoDeSuite)
    # Verifica se o número de reservas atingiu a capacidade
    if reservas[indice_suite] >= capacidades[indice_suite]:
        print(f"Não há vagas disponíveis para a suíte {tipoDeSuite}.")
        return False  # Não está disponível
    else:
        return True  # Está disponível

# Função para validar o CPF
def validar_cpf(cpf):
    # Verifica se o CPF possui 11 dígitos e se são todos números
    return len(cpf) == 11 and cpf.isdigit() 


 
# Função para criar botões principais
def criarBotoesPrincipais(janela):
    # Definindo as funções que serão chamadas ao clicar nos botões
    def check_in():
        # Criar uma nova janela para o cadastro
        janela_cadastro = ctk.CTkToplevel() #Inicia a janela
        janela_cadastro.geometry("400x500") #Define o tamanho
        janela_cadastro.title("Cadastro de Usuário") #Mensagem da janela
        janela_cadastro.resizable(False, False) #Não deixe o usuário redimensionar a janela
          
         # Criar campos de entrada
        label_nome = ctk.CTkLabel(janela_cadastro, text="Nome:")
        label_nome.pack(pady=5)
        entry_nome = ctk.CTkEntry(janela_cadastro, corner_radius=10, width=250)
        entry_nome.pack(pady=5) 
          
        label_cpf = ctk.CTkLabel(janela_cadastro, text="CPF:")
        label_cpf.pack(pady=5)
        entry_cpf = ctk.CTkEntry(janela_cadastro, corner_radius=10, width=250)
        entry_cpf.pack(pady=5)
        
        label_suite = ctk.CTkLabel(janela_cadastro, text="Tipo de Suíte: ")
        label_suite.pack(pady=5)
        suite_escolha = ctk.CTkComboBox(janela_cadastro, values=tipos_suite, corner_radius=10)
        suite_escolha.pack(pady=5)
          
        label_check_in = ctk.CTkLabel(janela_cadastro, text="Data de Check-in: ")
        label_check_in.pack(pady=5)
        entry_check_in = DateEntry(janela_cadastro, width=20, background="darkblue", foreground="white", borderwidth=2, corner_radius=15, state="readonly")
        entry_check_in.pack(pady=5)
          
        label_check_out = ctk.CTkLabel(janela_cadastro, text="Data de Check-Out")
        label_check_out.pack(pady=5)
        entry_check_out = DateEntry(janela_cadastro, width=20, background="darkblue", foreground="white", borderwidth=2, corner_radius=15, state="readonly" )
        entry_check_out.pack(pady=5)
          
        #Mensagem de erro
        label_erro = ctk.CTkLabel(janela_cadastro, text="", text_color="red")
        label_erro.pack(pady=5)
    
        def salvar_dados():
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            suite = suite_escolha.get()
            check_in = entry_check_in.get()
            check_out = entry_check_out.get()
            
            if not validar_cpf(cpf):
                label_erro.configure(text="CPF inválido.", text_color="red")
                return
            
            #Verificando o indice do tipo da suíte
            indice_suite = tipos_suite.index(suite)
            
            #Verificando o CPF duplicado
            if cpfJaCadastrado(cpf):
               label_erro.configure(text="Este CPF já está cadastrado.", text_color="red")
               return
              
        
            if not verificarDisponibilidade(suite):
                label_erro.configure(text="Limite de ocupação atingido para essa suíte.", text_color="red")            # Adiciona o hóspede à lista
            else:
                hospedes.append({
                'nome': nome,
                'cpf': cpf,
                'tipo_suite': suite,
                'checkin': check_in,
                'checkout': check_out
                })
                
                reservas[indice_suite] += 1
                label_erro.configure(text="Usuário cadastrado com sucesso!", text_color="green")
                print(f"Hóspede {nome} cadastrado na suíte {suite}. Vagas ocupadas: {reservas[indice_suite]}/{capacidades[indice_suite]}")

            
            # Mostra os dados no terminal
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Suíte: {suite}")
            print(f"Check-in: {check_in}")
            print(f"Check-out: {check_out}")
                  
                  
        salvar = ctk.CTkButton(janela_cadastro, text="Salvar", command=salvar_dados)
        salvar.pack(pady=5)
    def check_out():
          # Cria uma nova janela para o check-out
        janela_checkout = ctk.CTkToplevel()  # Inicia a nova janela
        janela_checkout.geometry("400x400")  # Define o tamanho da janela
        janela_checkout.title("Check-out")  # Define o título da janela
        janela_checkout.resizable(False, False)  # Impede que o usuário redimensione a janela
        
        # Criação do campo de entrada para CPF
        label_cpf_checkout = ctk.CTkLabel(janela_checkout, text="Informe o CPF do hóspede:")  # Label para o CPF
        label_cpf_checkout.pack(pady=5)  # Adiciona a label na janela
        entry_cpf_checkout = ctk.CTkEntry(janela_checkout, corner_radius=10, width=250)  # Campo de entrada para o CPF
        entry_cpf_checkout.pack(pady=5)  # Adiciona o campo na janela
        
        # Mensagem de erro, inicialmente vazia
        label_erro_checkout = ctk.CTkLabel(janela_checkout, text="", text_color="red")  # Label para exibir mensagens de erro
        label_erro_checkout.pack(pady=5)  # Adiciona a label na janela
        
        # Função que será chamada ao clicar no botão para processar o check-out
        def processar_checkout():
            cpf = entry_cpf_checkout.get()  # Captura o CPF do campo de entrada
            encontrado = False  # Variável para rastrear se o hóspede foi encontrado
            
            # Itera sobre a lista de hóspedes
            for hospede in hospedes:
                if hospede["cpf"] == cpf:  # Se o CPF corresponder, o hóspede foi encontrado
                    reservas[tipos_suite.index(hospede['tipo_suite'])] -= 1  # Decrementa o contador de reservas
                    hospedes.remove(hospede)  # Remove o hóspede da lista
                    label_erro_checkout.configure(text="Check-out realizado com sucesso!", text_color="green")  # Mensagem de sucesso
                    print(f"Check-out do hóspede {hospede['nome']} realizado.")  # Exibe no terminal
                    encontrado = True  # Indica que o hóspede foi encontrado
                    break  # Encerra o loop
            
            # Se o hóspede não foi encontrado, exibe mensagem de erro
            if not encontrado:
                label_erro_checkout.configure(text="CPF não encontrado!", text_color="red")  # Mensagem de erro
                
        # Criação do botão para processar o check-out
        btn_checkout = ctk.CTkButton(janela_checkout, text="Finalizar Check-out", command=processar_checkout)  # Chama a função processar_checkout ao clicar
        btn_checkout.pack(pady=5)  # Adiciona o botão na janela


    def visualizar_suites():
        # Criar uma nova janela para visualizar as suítes
        janela_visualizacao = ctk.CTkToplevel()
        janela_visualizacao.geometry("600x400")
        janela_visualizacao.title("Visualizar Suítes")
    
        # Criar a tabela usando Treeview
        tree = ttk.Treeview(janela_visualizacao, columns=("Nome", "CPF", "Check-in", "Check-out", "Suíte"), show='headings')
    
        # Configurações das colunas
        tree.column("Nome", anchor='center', width=120)
        tree.column("CPF", anchor='center', width=100)
        tree.column("Check-in", anchor='center', width=120)
        tree.column("Check-out", anchor='center', width=120)
        tree.column("Suíte", anchor='center', width=100)
    
        # Cabeçalhos da tabela
        tree.heading("Nome", text="Nome")
        tree.heading("CPF", text="CPF")
        tree.heading("Check-in", text="Data de Check-in")
        tree.heading("Check-out", text="Data de Check-out")
        tree.heading("Suíte", text="Tipo de Suíte")

        # Estilo do cabeçalho
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'), background="#f0f0f0")
    
        # Adicionar um scrollbar
        scrollbar = ttk.Scrollbar(janela_visualizacao, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
    
        tree.pack(expand=True, fill='both')
        
        

        # Adicionar dados à tabela
        for hospede in hospedes:
            tree.insert("", "end", values=(hospede["nome"], hospede["cpf"], hospede["checkin"], hospede["checkout"], hospede["tipo_suite"]))
    
        # Centralizar os dados das linhas
        for col in ("Nome", "CPF", "Check-in", "Check-out", "Suíte"):
            tree.column(col, anchor='center')
            
            
    def filtrar_suites():
        # Criar uma nova janela para filtrar suítes
        janela_filtro = ctk.CTkToplevel()
        janela_filtro.geometry("600x400")
        janela_filtro.title("Filtrar Suítes")

        # Criar campos de entrada
        label_cpf = ctk.CTkLabel(janela_filtro, text="CPF:")
        label_cpf.pack(pady=5)
        entry_cpf = ctk.CTkEntry(janela_filtro, corner_radius=10, width=250)
        entry_cpf.pack(pady=5)

        label_check_in = ctk.CTkLabel(janela_filtro, text="Data de Check-in:")
        label_check_in.pack(pady=5)
        entry_check_in = DateEntry(janela_filtro, width=100, background="darkblue", foreground="white", borderwidth=2, corner_radius=10, state="readonly")
        entry_check_in.pack(pady=5)

        label_check_out = ctk.CTkLabel(janela_filtro, text="Data de Check-out:")
        label_check_out.pack(pady=5)
        entry_check_out = DateEntry(janela_filtro, width=100, background="darkblue", foreground="white", borderwidth=2, corner_radius=10, state="readonly")
        entry_check_out.pack(pady=5)

        # Botão para aplicar o filtro
        btn_filtrar = ctk.CTkButton(janela_filtro, text="Filtrar", command=lambda: aplicar_filtro(entry_cpf.get(), entry_check_in.get(), entry_check_out.get()))
        btn_filtrar.pack(pady=10)
        

        def aplicar_filtro(cpf, check_in, check_out):
                janela_filtro = ctk.CTkToplevel()
                janela_filtro.geometry("600x400")
                janela_filtro.title("Filtrar Suítes")
                janela_filtro.configure(bg="white")

                # Coletar os critérios de filtragem
                cpf = entry_cpf.get().strip()  # Remove espaços em branco
                check_in = entry_check_in.get().strip()  # Remove espaços em branco
                check_out = entry_check_out.get().strip()  # Remove espaços em branco

                resultados = []

                for hospede in hospedes:
                    if (cpf == "" or hospede["cpf"] == cpf) and \
                       (check_in == "" or hospede["checkin"] == check_in) and \
                       (check_out == "" or hospede["checkout"] == check_out):
                        resultados.append(hospede)

                    # Limpar resultados anteriores
                    for widget in janela_filtro.winfo_children():
                        widget.pack_forget()
                        janela_filtro.update()
                        time.sleep(0.1)

            # Exibir resultados
                if resultados:
                    tree = ttk.Treeview(janela_filtro, columns=("Nome", "CPF", "Check-in", "Check-out", "Suíte"), show='headings')
                    tree.column("Nome", anchor='center', width=120)
                    tree.column("CPF", anchor='center', width=100)
                    tree.column("Check-in", anchor='center', width=120)
                    tree.column("Check-out", anchor='center', width=120)
                    tree.column("Suíte", anchor='center', width=100)
                    tree.heading("Nome", text="Nome")
                    tree.heading("CPF", text="CPF")
                    tree.heading("Check-in", text="Data de Check-in")
                    tree.heading("Check-out", text="Data de Check-out")
                    tree.heading("Suíte", text="Tipo de Suíte")

                    scrollbar = ttk.Scrollbar(janela_filtro, orient="vertical", command=tree.yview)
                    tree.configure(yscroll=scrollbar.set)
                    scrollbar.pack(side='right', fill='y')

                    tree.pack(expand=True, fill='both')

                    for hospede in resultados:
                        tree.insert("", "end", values=(hospede["nome"], hospede["cpf"], hospede["checkin"], hospede["checkout"], hospede["tipo_suite"]))

                    label_resultados = ctk.CTkLabel(janela_filtro, text=f"{len(resultados)} resultado(s) encontrado(s).", text_color="green")
                    label_resultados.pack(pady=5)

                else:  
                    label_nenhum_resultado = ctk.CTkLabel(janela_filtro, text="Nenhum resultado encontrado.", text_color="red")
                    label_nenhum_resultado.pack(pady=5)

# Largura e altura dos botões
    btn_width = 180
    btn_height = 150

# Listas de ícones e textos para os botões principais
    textos = [
        "Fazer Check-in",
        "Fazer Check-out",
        "Visualizar Suítes",
        "Consultar Suítes",
    ]

# Chamando a função que carrega as imagens
    icones =  [
        carregarImagem("image/checkin.png"),
        carregarImagem("image/checkout.png"),
        carregarImagem("image/consultar.png"),
        carregarImagem("image/icon_reserva.png")
    ]
    

    # Lista de funções correspondentes aos botões
    funcoes = [
        check_in,
        check_out,
        visualizar_suites,
        filtrar_suites,
    ]
    
    row_index = 2  # Para os botões começarem na linha 2
    col_index = 0  # Para cada botão começar na coluna 0

    # Adicionando os botões manualmente
    for i in range(len(textos)):
        texto = textos[i]
        icone = icones[i]
        funcao = funcoes[i]
        
        if icone:  # Verifica se a imagem foi carregada corretamente
            btn = ctk.CTkButton(
                janela,
                fg_color="#FFFFFF",
                text_color="black",
                text=texto,
                image=icone,
                width=btn_width,
                height=btn_height,
                compound="top",
                command=funcao  # Adiciona a função ao botão
            )
            btn.grid(row=row_index, column=col_index, padx=20, pady=20)
            col_index += 1
            
            if col_index > 1:  # Mover para a próxima linha após 3 botões
                col_index = 0
                row_index += 1

def iniciar_aplicacao():
    ctk.set_appearance_mode("light")  # Define o modo de aparência da interface como claro
    janela = ctk.CTk() #Cria a janela principal
    janela.geometry("590x600") #Define o tamanho
    janela.title("Menu Principal") #Titulo
    janela.resizable(False, False) # A janela fica em um tamanho fixo
    criarBarraTopo(janela, "Usuário") # Cria uma barra no topo da janela
    criarTitulo(janela) # Cria um título na janela
    criarBotoesPrincipais(janela)  # Chama a função que cria os botões principais
    janela.grid_columnconfigure((0, 1, 2), weight=1)
    
    # Inicia o loop da aplicação
    janela.mainloop()  # Mantém a janela aberta até que o usuário a feche


#Chama a função pra iniciar a aplicação
if __name__ == "__main__":
    iniciar_aplicacao() #Executa a função principal