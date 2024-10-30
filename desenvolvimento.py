import flet as ft
from bancoDados import criar_banco, adicionar_usuario, validar_login

def main(page: ft.Page):
    # Cria o banco de dados e a tabela
    criar_banco()
    
    # Adiciona alguns usuários (remova ou comente se não precisar adicionar sempre)
    adicionar_usuario("usuario1", "senha123")
    adicionar_usuario("usuario2", "senha456")

    # Define as cores dos contêineres
    left_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=page.width / 2,
        height=page.height,
    )

    right_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=page.width / 2,
        height=page.height,
    )

    # Adiciona os contêineres à página
    page.add(
        ft.Row(
            [
                left_container,
                right_container
            ],
            expand=True,  # Permite que os contêineres ocupem a tela toda
        )
    )

    # Define o caminho da imagem
    img_path = "imagens/PSI.png"  
    
    # Cria um contêiner para a imagem
    img_container = ft.Container(
        content=ft.Image(src=img_path),
        alignment=ft.alignment.center,
        padding=20,
    )

    # Adiciona o contêiner da imagem ao contêiner azul
    left_container.content = img_container

    # Define o título da página
    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="black"
        )
    )

    # Adiciona o título e os campos de entrada ao contêiner da direita
    right_container.content = ft.Column(
        controls=[
            ola,
            botao(page)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    # Atualiza a página para refletir todas as adições
    page.update()  

def botao(page: ft.Page):
    # Cria campos de entrada para nome e senha
    entrada_nome = ft.TextField(label="Nome", bgcolor="white")
    entrada_senha = ft.TextField(label="Senha", password=True, bgcolor="white")

    # Cria os botões "Entrar" e "Esqueci Senha"
    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    botao_esqueci_senha = ft.ElevatedButton("Esqueci Senha", on_click=lambda e: funcao_esqueci_senha())

    # Cria um contêiner em linha para os botões "Entrar" e "Esqueci Senha"
    botoes_container = ft.Row(
        controls=[botao_entrar, botao_esqueci_senha],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Cria um contêiner para os campos de entrada e os botões em linha
    entrada_container = ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            botoes_container
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    return entrada_container

def validar_login_ui(page: ft.Page, entrada_nome: ft.TextField, entrada_senha: ft.TextField):
    nome = entrada_nome.value
    senha = entrada_senha.value

    if validar_login(nome, senha):
        page.add(ft.Text("Login bem-sucedido!", color="green"))
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))

    # Atualiza a página para mostrar a mensagem
    page.update()

def funcao_esqueci_senha():
    print("Função 'Esqueci Senha' chamada.")

ft.app(target=main)
