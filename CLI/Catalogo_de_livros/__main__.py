from biblioteca import CatalogoLivros, RepositorioJSON
from pathlib import Path
from rich.table import Table
from rich import print
from rich.traceback import install

install()

def pedir_titulo():
    while True:
        titulo = input("Digite o título do livro: ").strip()
        if titulo:
            return titulo
        else:
            print("O título deve conter ao menos um caracter.")

def pedir_autor():
    while True:
        autor = input("Digite o autor do livro: ").strip()
        if autor:
            return autor
        else:
            print("O autor deve conter ao menos um caracter.")

def pedir_id():
    while True:
        try:
            print('='*40)
            res = int(input("Selecione o ID do livro: "))
            print("="*40)
        except ValueError:
            print("Digite somente números inteiros correspondentes a o ID de um livro.")
        else:
            break
    return res


def main():
    diretorio_projeto = Path(__file__).absolute().parent
    caminho_repositorio = diretorio_projeto / "livros.json"
    repositorio = RepositorioJSON(caminho_repositorio)
    catalogo = CatalogoLivros(repositorio)
    while True:
        print("="*30)
        print("BIBLIOTECA".center(30))
        print("="*30)
        print("MENU".center(30))
        print('_'*30)
        print("[1] - Adicionar")
        print("[2] - Listar")
        print("[3] - Buscar por Título")
        print("[4] - Editar")
        print("[5] - Remover")
        print("[6] - Sair")
        print('_'*30)

        while True:
            try:
                res = int(input("Sua opção: "))
            except ValueError:
                print(f"Opção inválida. Digite somente números inteiros.")
            else:
                if res in range(1, 7):
                    break
                else:
                    print("Escolha uma opção entre 1 e 6.")

        if res == 1:
            print('ADICIONAR LIVRO.'.center(30, "="))
            tit = pedir_titulo()
            aut = pedir_autor()
            catalogo.adicionar(tit, aut)
        elif res == 2:
            tabela = Table(title="CATÁLOGO")
            tabela.add_column("ID")
            tabela.add_column("Título")
            tabela.add_column("Autor")
            for livro in catalogo.listar():
                tabela.add_row(f"{livro.id}", f"{livro.titulo}", f"{livro.autor}")
            print(tabela)
        elif res == 3:
            tit = pedir_titulo()
            tabela = Table(title="RESULTADOS")
            tabela.add_column("ID")
            tabela.add_column("Título")
            tabela.add_column("Autor")
            for livro in catalogo.buscar_titulo(tit):
                tabela.add_row(f"{livro.id}", f"{livro.titulo}", f"{livro.autor}")
            print(tabela)
        elif res == 4:
            id_livro = pedir_id()
            livro = catalogo.buscar(id_livro)
            if livro is None:
                print("Livro não encontrado.")
            else:
                print("="*40)
                print("Editar por:")
                print('-'*40)
                print("[1] - Título")
                print("[2] - Autor")
                print("[3] - Título e Autor")
                print("-"*40)
                while True:
                    try:
                        opc = int(input("Sua opção: "))
                    except Exception as e:
                        print("Opção inválida. Digite somente número inteiro correspondente a uma das opções")
                    else:
                        break
                if opc == 1:
                    catalogo.editar(id_livro, titulo=pedir_titulo())
                elif opc == 2:
                    catalogo.editar(id_livro, autor=pedir_autor())
                elif opc == 3:
                    catalogo.editar(id_livro, titulo=pedir_titulo(), autor=pedir_autor())

        elif res == 5:
            id_livro = pedir_id()
            livro = catalogo.buscar(id_livro)
            if livro is None:
                print("Livro não encontrado.")
            else:
                while True:
                    print("="*40)
                    print(f"Tem certeza que deseja [red]remover[/] o livro [blue]{livro.titulo}[/]?", end='')
                    opc = input(" [s/n]: ").strip().lower()
                    print("="*40)
                    if opc in ('s', 'n') and len(opc) > 0:
                        break
                    else:
                        print("Digite 's' para SIM e 'n' para NÃO.")
                if opc == 's':
                    catalogo.remover(id_livro)
                elif opc == 'n':
                    continue
    
        elif res == 6:
            break

if __name__ == "__main__":
    main()