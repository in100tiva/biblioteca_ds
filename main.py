
from rich.console import Console
from rich.table import Table
from library import Library, User, Book

console = Console()

def display_menu(library):
    table = Table(title="Menu de Opções", show_header=True, header_style="bold magenta")
    table.add_column("Opção", style="dim", width=12)
    table.add_column("Descrição")

    menu = [
        ("1", "Adicionar livro"),
        ("2", "Listar livros"),
        ("3", "Adicionar usuário"),
        ("4", "Listar usuários"),
        ("5", "Alugar livro"),
        ("6", "Devolver livro"),
        ("7", "Salvar dados"),
        ("8", "Carregar dados"),
        ("9", "Sair")
    ]

    # Condicionalmente adicionar opções de menu
    if library.books:
        menu.insert(1, ("2", "Remover livro"))

    if library.users:
        menu.insert(5, ("5", "Remover usuário"))

    for item in menu:
        if item[0]:
            table.add_row(*item)

    console.print(table)

def main():
    library = Library()

    while True:
        display_menu(library)
        choice = console.input("[bold cyan]Escolha uma opção: [/bold cyan]")

        if choice == "1":
            title = console.input("Título do livro: ")
            author = console.input("Autor do livro: ")
            library.add_book(Book(title, author))
            console.print(f"[bold green]Livro '{title}' adicionado com sucesso.[/bold green]")

        elif choice == "2" and library.books:
            title = console.input("Título do livro a remover: ")
            book_to_remove = next((book for book in library.books if book.title == title), None)
            if book_to_remove:
                library.remove_book(book_to_remove)
                console.print(f"[bold green]Livro '{title}' removido com sucesso.[/bold green]")
            else:
                console.print(f"[bold red]Livro '{title}' não encontrado.[/bold red]")

        elif choice == "3":
            console.print("[bold magenta]\nLivros disponíveis:[/bold magenta]")
            for book in library.books:
                console.print(f"{book}")

        elif choice == "4":
            name = console.input("Nome do usuário: ")
            library.add_user(User(name))
            console.print(f"[bold green]Usuário '{name}' adicionado com sucesso.[/bold green]")

        elif choice == "5" and library.users:
            name = console.input("Nome do usuário a remover: ")
            user_to_remove = next((user for user in library.users if user.name == name), None)
            if user_to_remove:
                library.remove_user(user_to_remove)
                console.print(f"[bold green]Usuário '{name}' removido com sucesso.[/bold green]")
            else:
                console.print(f"[bold red]Usuário '{name}' não encontrado.[/bold red]")

        elif choice == "6":
            console.print("[bold magenta]\nUsuários registrados:[/bold magenta]")
            for user in library.users:
                console.print(f"{user}")

        elif choice == "7":
            user_name = console.input("Nome do usuário: ")
            book_title = console.input("Título do livro: ")
            user = next((user for user in library.users if user.name == user_name), None)
            book = next((book for book in library.books if book.title == book_title), None)
            if user and book:
                library.rent_book(user, book)
                console.print(f"[bold green]{user.name} alugou {book.title}. Previsão de entrega: {book.return_date.strftime('%d/%m/%Y')}[/bold green]")
            else:
                console.print("[bold red]Usuário ou livro não encontrado.[/bold red]")

        elif choice == "8":
            user_name = console.input("Nome do usuário: ")
            book_title = console.input("Título do livro: ")
            user = next((user for user in library.users if user.name == user_name), None)
            book = next((book for book in user.rented_books if book.title == book_title), None) if user else None
            if user and book:
                library.return_book(user, book)
                console.print(f"[bold green]{user.name} devolveu {book.title}.[/bold green]")
            else:
                console.print("[bold red]Usuário ou livro não encontrado.[/bold red]")

        elif choice == "9":
            filename = console.input("Nome do arquivo para salvar os dados: ")
            save_data(library, filename)
            console.print(f"[bold green]Dados salvos em '{filename}'.[/bold green]")

        elif choice == "10":
            filename = console.input("Nome do arquivo para carregar os dados: ")
            load_data(library, filename)
            console.print(f"[bold green]Dados carregados de '{filename}'.[/bold green]")

        elif choice == "11":
            console.print("[bold yellow]Saindo...[/bold yellow]")
            break

        else:
            console.print("[bold red]Opção inválida. Tente novamente.[/bold red]")

if __name__ == "__main__":
    main()
