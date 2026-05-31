lista = list()

def add():
    global lista
    tarefa = dict()
    tarefa['titulo'] = str(input('Título: ')).strip()
    tarefa['descricao'] = str(input('Descrição: ')).strip()
    tarefa['data'] = str(input('Data [dd/mm/aa]: ')).strip()
    tarefa['estatus'] = 'Não concluída'
    lista.append(tarefa.copy())
    tarefa.clear()

def exclui(n):
    global lista
    if n - 1 < 0 or n - 1 > len(lista):
        i = 'erro'
    else:
        i = n - 1
    if n != 0:
        lista.pop(i)

def conclui(n):
    global lista
    if n - 1 < 0 or n - 1 > len(lista):
        i = 'erro'
    else:
        i = n - 1
    if n != 0:
        lista[i]['estatus'] = 'Concluído'
        return lista[i]['estatus']

def altera(n):
    global lista
    if n - 1 < 0 or n - 1 > len(lista):
        i = 'erro'
    elif n != 0 and lista != []:
        i = n - 1
        lista[i]['titulo'] = str(input('Título: ')).strip()
        lista[i]['descricao'] = str(input('Descrição: ')).strip()
        lista[i]['data'] = str(input('Data [dd/mm/aa]: ')).strip()
        if lista[i]['estatus'] == 'Conluído':
            lista[i]['estatus'] = 'Não concluída'
    else:
        print('Opção inválida')

def ver(n):
    global lista
    from time import sleep
    if n - 1 < 0 or n - 1 > len(lista):
        i = 'erro'
    else:
        i = n - 1
    if n != 0:
        print('=' * 40)
        print(f'{'Detalhes da tarefa '+f'{n}':^40}')
        print('='*40)
        for k, v in lista[i].items():
            print(f'{k}: {v}')
        sleep(5)



while True:
    c = 0
    print('='*40)
    print(f'{'To Do List':^40}')
    print('='*40)
    print('Tarefas')
    for e in lista:
        c += 1
        print('-'*40)
        print(f'{[c]} -', end = ' ')
        for k, v in e.items():
            if k == 'titulo':
                print(f'{v} |', end = ' ')
            if k == 'estatus':
                print(v)
    print('='*40)
    print(""" Selecione:
        [1] Adicionar tarefa
        [2] Excluir tarefa
        [3] Editar tarefa
        [4] Ver tarefa
        [5] Marcar como concluida
        [6] Parar programa
    """)
    while True:
        try:
            selected = int(input('Selecione: '))
        except:
            print('Comando inválido, por favor selecione uma das opções acima')
        else:
            if 0 < selected < 7:
                print(f'Selecionado: {selected}')
                break
            else:
                print('Seleção inválida')

    if selected == 1:
        add()
    elif selected == 2:
        while True:
            try:
                exclui(int(input('Selecione o número da tarefa a ser excluida ou 0 para retornar ao menu: ')))
            except Exception as error:
                print(f'Opção inválida. {error.__class__}')
            else:
                break
    elif selected == 3:
        while True:
            try:
                altera(int(input('Selecione a tarefa a ser editada ou 0 para retornar ao menu: ')))
            except Exception as error:
                print(f'Opção inválida. {error.__class__}')
            else:
                break
    elif selected == 4:
        while True:
            try:
                ver(int(input('Selecione a terefa para exibir detlahes ou 0 para retornar ao menu: ')))
            except Exception as error:
                print(f'Opção inválida. {error.__class__}')
            else:
                break
    elif selected == 5:
        while True:
            try:
                print(conclui(int(input('Selecione o número da tarefa ou 0 para retornar ao menu: '))))
            except Exception as error:
                print(f'Opção inválida. {error.__class__}')
            else:
                break
    elif selected == 6:
        print('Programa encerrado')
        break 

        