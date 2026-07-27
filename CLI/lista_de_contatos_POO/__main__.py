from rich import print
from rich.table import Table
from rich.traceback import install
from lista_contatos.agenda import Agenda
from lista_contatos.repositorio import RepositorioJson
from pathlib import Path

install()

def pedir_nome():
    while True:
        print("-"*40)
        nome = input("Digite o nome do contato: ").strip()
   
        if not nome:
            print("Nome deve possuir ao menos um caracter.")
        else:
            break
    return nome

def pedir_telefone():
    while True:
        print('-'*40)
        telefone = input("Digite o telefone do contato [(DDD)8888-8888]: ").strip()
    
        if not telefone:
            print("Telefone deve possuir ao menos um caracter.")
        else:
            break
    return telefone

def pedir_email():
    print("-"*40)
    email = input("Digite o email do contato [email@dominio.com] - aperte Enter para deixar em branco: ").strip()
       
    return email

def pedir_endereco():
    print("-"*40)
    endereco = input("Digite o endereço do contato - aperte Enter para deixar em branco: ")
  
    return endereco

def pedir_id():
    while True:
        try:
            print("-"*40)
            id_contato = int(input("Digite o ID do contato: "))
        except ValueError:
            print("Digite somente numeros inteiros.")
        else:
            break

    return id_contato

def main():
    diretorio_atual = Path(__file__).absolute().parent
    caminho_json = diretorio_atual / "dados" / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    while True:
        print("="*40)
        print("AGENDA DE CONTATOS".center(40))
        print("="*40)
        print("MENU".center(40, "_"))
        print("[1] - Adicionar Contato")
        print("[2] - Listar Contatos")
        print("[3] - Buscar Contato")
        print("[4] - Editar Contato")
        print("[5] - Remover Contato")
        print("[6] - Sair")

        while True:
            try:
                print("-"*40)
                opc = int(input("Digite sua opção: "))
            except ValueError:
                print("Digite somente valores inteiros entre 1 e 6")
            else:
                if opc not in (1, 2, 3, 4, 5, 6):
                    print("Digite somente números inteiros entre 1 e 6")
                else:
                    break

        if opc == 1:
            while True:
                nome = pedir_nome()
                telefone = pedir_telefone()
                email = pedir_email()
                endereco = pedir_endereco()
                try:
                    agenda.adicionar(nome, telefone, email, endereco)
                except ValueError:
                    print("[red]-[/]"*40)
                    print("[red]Algo deu errado. Preencha corretamente os campos acima.[/]")
                    print("[red]-[/]"*40)
                else:
                    break

        elif opc == 2:
            lista = Table(title="Lista de Contatos")
            lista.add_column("ID")
            lista.add_column("Nome")
            lista.add_column("Telefone")
            lista.add_column("Email")
            lista.add_column("Endereço")

            for contato in agenda.listar():
                lista.add_row(f"{contato.id}", f"{contato.nome}", f"{contato.telefone}", f"{contato.email}", f"{contato.endereco}")

            print(lista)
            
        elif opc == 3:
            resultado = Table()
            resultado.add_column("ID")
            resultado.add_column("Nome")
            resultado.add_column("Telefone")
            resultado.add_column("Email")
            resultado.add_column("Endereço")

            nome = pedir_nome()

            for contato in agenda.buscar_por_nome(nome):
                resultado.add_row(f"{contato.id}", f"{contato.nome}", f"{contato.telefone}", f"{contato.email}", f"{contato.endereco}")

            print(resultado)

        elif opc == 4:
            while True:
                id_contato = pedir_id()
                contato = agenda.buscar_por_id(id_contato)
                if not contato:
                    print('-'*40)
                    print("Contato não encontrado.")
                    print("-"*40)
                break
            if contato:    
                print("-"*40)
                print("Editar por".center(40))
                print("-"*40)
                print("[1] - Nome")
                print("[2] - Telefone")
                print("[3] - Email")
                print("[4] - Endereco")
                print("[5] - Todos os dados")
                while True:
                    try:
                        print("-"*40)
                        opc2 = int(input("Digite sua opção: "))
                    except ValueError:
                        print("Digite somente valores inteiros entre 1 e 5.")
                    else:
                        if opc2 not in (1, 2, 3, 4, 5):
                            print("Digite somente valores inteiros entre 1 e 5.")
                        else:
                            break
                if opc2 == 1:
                    nome = pedir_nome()
                    agenda.editar(id_contato, nome)
                if opc2 == 2:
                    telefone = pedir_telefone()
                    agenda.editar(id_contato, telefone)
                if opc2 == 3:
                    email = pedir_email()
                    agenda.editar(id_contato, email)
                if opc2 == 4:
                    endereco = pedir_endereco
                    agenda.editar(id_contato, endereco)
                if opc2 == 5:
                    nome = pedir_nome()
                    telefone = pedir_telefone()
                    email = pedir_email()
                    endereco = pedir_endereco()
                    agenda.editar(id_contato, nome, telefone, email, endereco)

        elif opc == 5:
            while True:
                id_contato = pedir_id()
                contato = agenda.buscar_por_id(id_contato)
                if not contato:
                    print('-'*40)
                    print("Contato não encontrado.")
                    print("-"*40)
                break
            if contato: 
                print("[red]EXCLUIR[/]".center(48, "="))
                print(f"Tem certeza que deseja [red]excluir[/] o contato de [green]{contato.nome}[/]? ", end='')
                while True:
                    res = str(input("[s/n]: ")).strip()
                    if not res or res not in ("s", "n"):
                        print("Digite s para SIM e n para NÃO.")
                    else:
                        break
                if res == "s":
                    agenda.remover(id_contato)
                         
        elif opc == 6:
            break

if __name__ == "__main__":
    main()