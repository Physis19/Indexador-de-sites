from structures import DoublyLinkedList
from rich.console import Console
from rich.panel import Panel
from rich import print

console = Console()

websites = DoublyLinkedList()
def menu():
    while True:
        console.print(Panel.fit('''[bold]

 ________     ___    ___ ___  ________          
|\   __  \   |\  \  /  /|\  \|\_____  \         
\ \  \|\  \  \ \  \/  / | \  \|____|\  \        
 \ \  \\\  \  \ \    / / \ \  \    \ \__\       
  \ \  \\\  \  /     \/   \ \  \    \|__|       
   \ \_______\/  /\   \    \ \__\       ___     
    \|_______/__/ /\ __\    \|__|      |\__\    
             |__|/ \|__|               \|__|    
                                                
 [/bold]                                               
[bold cyan]1.[/bold cyan] [bold green]Adicionar um novo site [/bold green]          [bold cyan]2.[/bold cyan][bold green] Deletar um site[/bold green]              
[bold cyan]3.[/bold cyan] [bold green]Ver todos os sites[/bold green]               [bold cyan]0.[/bold cyan] [bold green]Sair do programa[/bold green]
 ''', title="[bold green]Oxi?[/bold green]"))
        option = console.input('Digite o número da opção desejada: ')

        if option == "1":
            data = console.input('Digite a URL do site: ')
            websites.append(data)
            console.print(f'O site {data} foi adicionado !')
        elif option == "2":
            data = console.input('Digite a URL do site: ')
            websites.remove(data)
            console.print(f'O site {data} removido !')      
        elif option == "3":
            print(websites)
        elif option == "0":
            break
        

menu()
