from structures import DoublyLinkedList

from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()

websites = DoublyLinkedList()
def menu():
    while True:
        console.print(Panel("Seja bem vindo ao buscador Oxi ?, escolha alguma das opções abaixo!", title="[bold green]Oxi?[/bold green]"))
        console.print("1. Adicionar um novo site")
        console.print("2. Deletar um site")
        console.print("3. Ver todos os sites")
        console.print('4. Remover algum site')
        console.print('0. Sair do programa\n')
        option = console.input('Digite o número da opção desejada: ')

        if option == "1":
            data = console.input('Digite a URL do site: ')
            websites.append(data)
            console.print(f'O site {data} foi adicionado !')
        elif option == "2":
            pass
        elif option == "3":
            print(websites)
        elif option == "4":
            pass
        elif option == "0":
            break
        

menu()