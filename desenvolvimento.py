import flet as ft
from bancoDados import criar_banco, adicionar_usuario, validar_login

def main(page: ft.Page):
    criar_banco()
    
    # Define os contêineres
    left_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=1000,
        height=1000,
        content=ft.Column(
            controls=[ft.Image(src="PSI.png", width=900, height=800)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    right_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=1000,
        height=1000,
    )

    page.add(
        ft.Row(
            controls=[left_container, right_container],
            expand=True,
        )
    )

    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="black"
        )
    )

    right_container.content = ft.Column(
        controls=[
            ola,
            botao_login(page),
            ft.Row(
                controls=[
                    ft.TextButton("Registrar", on_click=lambda e: mostrar_registro(page))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    page.update()  

def botao_login(page: ft.Page):
    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="black"),  # Ícone de usuário
            ft.TextField(label="Nome", bgcolor="white", width=850)  # Campo de entrada 
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    senha_icon = ft.Icon(name=ft.icons.LOCK, size=20, color="black")
    entrada_senha = ft.Row(
        controls=[
            senha_icon,
            ft.TextField(label="Senha", password=True, bgcolor="white", width=850)  # Campo de entrada 
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    
    return ft.Column(
        controls=[entrada_nome, entrada_senha, ft.Row(controls=[botao_entrar, ft.TextButton("Registrar", on_click=lambda e: mostrar_registro(page))], alignment=ft.MainAxisAlignment.CENTER)],
        alignment=ft.MainAxisAlignment.CENTER
    )

def mostrar_registro(page: ft.Page):
    page.clean()  # Limpa a página para mostrar o formulário de registro

    ola = ft.Text(
        value="Registrar", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="black"
        )
    )

    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="black"),  # Ícone de usuário
            ft.TextField(label="Nome de Usuário", bgcolor="white", width=200)  # Campo de entrada
        ],
        alignment=ft.MainAxisAlignment.START,
    )
    
    entrada_senha = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.LOCK, size=20, color="black"),
            ft.TextField(label="Senha", password=True, bgcolor="white", width=200)  # Campo de entrada 
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: registrar_usuario(page, entrada_nome, entrada_senha))

    page.add(
        ft.Column(
            controls=[ola, entrada_nome, entrada_senha, botao_registrar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()

def registrar_usuario(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value  # Obtém o valor do campo de nome
    senha = entrada_senha.controls[1].value  # Obtém o valor do campo de senha

    adicionar_usuario(nome, senha)  # Tenta adicionar o usuário ao banco de dados
    page.add(ft.Text("Usuário registrado com sucesso!", color="green"))

    # Redefine a página para o formulário de login após o registro
    mostrar_login(page)

def mostrar_login(page: ft.Page):
    page.clean()  # Limpa a página para mostrar o formulário de login novamente

    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="black"
        )
    )

    right_container_content = botao_login(page)
    right_container_content.controls.append(ft.TextButton("Registrar", on_click=lambda e: mostrar_registro(page)))

    page.add(
        ft.Column(
            controls=[ola, right_container_content],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()

def validar_login_ui(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value  # Obtém o valor do campo de nome
    senha = entrada_senha.controls[1].value  # Obtém o valor do campo de senha

    if validar_login(nome, senha):
        page.add(ft.Text("Login bem-sucedido!", color="green"))
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))

    page.update()

def funcao_esqueci_senha():
    print("Função 'Esqueci Senha' chamada.")

ft.app(target=main)