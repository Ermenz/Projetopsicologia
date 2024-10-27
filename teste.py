import flet as ft

def main(page: ft.Page):
    # Define a cor de fundo da página
    page.bgcolor = "lightblue"  

    # Define o título da página
    ola = ft.Text(
        value="Login", 
        size=30,  # Tamanho do texto
        style=ft.TextStyle(
            font_family="Times New Roman",  # Define a fonte
            weight=ft.FontWeight.BOLD,  # Negrito
            color="darkblue"  # Cor do texto
        )
    )
    
    # Adiciona o título à página
    page.controls.append(ola)

    # Chama a função para adicionar os campos de entrada e o botão
    botao(page)

    # Define o caminho da imagem
    img_path = "imagens/PSI.png"  
    
    # Cria um container para a imagem
    container = ft.Container(
        content=ft.Image(src=img_path),
        alignment=ft.alignment.center,  # Alinha o conteúdo ao centro
        padding=20,  # Adiciona um espaço ao redor da imagem
    )
     
    # Adiciona o container à página
    page.add(container)

    # Atualiza a página para refletir todas as adições
    page.update()  

def botao(possibilidade: ft.Page):
    # Cria campos de entrada para nome e senha
    entrada_nome = ft.TextField(label="Nome", width=200, bgcolor="white")  # Campo de entrada para nome
    entrada_senha = ft.TextField(label="Senha", password=True, width=200, bgcolor="white")  # Campo de entrada para senha

    # Cria um botão "Entrar"
    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login(possibilidade, entrada_nome, entrada_senha))

    # Cria um contêiner para os campos de entrada e o botão
    entrada_container = ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            botao_entrar  # Botão "Entrar"
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os campos
    )

    # Adiciona o contêiner à página
    possibilidade.add(entrada_container)

def validar_login(page: ft.Page, entrada_nome: ft.TextField, entrada_senha: ft.TextField):
    # Obtém os valores dos campos de entrada
    nome = entrada_nome.value
    senha = entrada_senha.value

    # Valida o login
    if nome == "Evandro" and senha == "1234":
        page.add(ft.Text("Login bem-sucedido!", color="green", size=20))
    else:
        page.add(ft.Text("Login falhou. Tente novamente.", color="red", size=20))
    
    # Atualiza a página para mostrar a mensagem
    page.update()

# Inicia a aplicação Flet
print("Iniciando a aplicação Flet...")
ft.app(target=main)
