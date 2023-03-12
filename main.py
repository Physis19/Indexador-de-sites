import time
from os import system, name
from structures import DoublyLinkedList
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.progress import track

console = Console()

websites = DoublyLinkedList()
def clear():
    if name == 'posix':
        system('clear')
    else:
        system('cls')

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

        match option:
            case "1":
                data = console.input('Digite a URL do site: ')
                websites.append(data)
                for i in track(range(3), description= 'Adicionando...'):
                    time.sleep(1)
                console.print(f'O site {data} foi adicionado !')
                time.sleep(3)
                clear()
            case "2":
                data = console.input('Digite a URL do site: ')
                for i in track(range(3), description= 'Removendo...'):
                    time.sleep(1)
                websites.remove(data)
                console.print(f'O site {data} removido !')
                time.sleep(3)
                clear()      
            case "3":
                websites_table = Table(box = box.ROUNDED, show_lines = True, title = 'Lista de sites :keyboard:')
                websites_table.add_column("Index", justify="center", style="cyan", no_wrap=True)
                websites_table.add_column("URL", justify='center', style="magenta")
                
                for i in websites.show_list():
                    websites_table.add_row(f'{i[0]}', f'[link={i[1]}]{i[1]}[/link]')
                console.print(websites_table)
            case "0":
                break
        

menu()
