import flet as ft
from teste import main as teste_main  # Importa a função main do arquivo teste.py

def main(page: ft.Page):
    entrada_nome, entrada_senha = teste_main(page)  # Chama a função de login e obtém os campos de entrada

# Inicia a aplicação Flet
print("Iniciando a aplicação Flet...")
ft.app(target=main)
