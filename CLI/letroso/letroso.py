from random import choice
import csv
import os

diretorio_atual = os.path.dirname(__file__)
caminho_csv = os.path.join(diretorio_atual, 'palavras.csv') 

with open(caminho_csv, 'r', encoding='utf-8') as file:
    leitor = csv.reader(file)
    next(leitor)
    for linha in leitor:
        palavras = linha


sorteada = []
mostrador = []
verificador = []
contador = 0

for char in choice(palavras).upper():
    sorteada.append(char)


print('='*60)
print(f"{'DESCUBRA A PALAVRA SECRETA':^60}")
print('='*60)
print(f'{'Digite uma pavra e descubra quais letras estão corretas':^60}\n')
print('\033[42m  \033[m - LETRA CORRETA NA POSIÇÃO CORRETA')
print('\033[43m  \033[m - LETRA CORRETA NA POSIÇÃO ERRADA\n')
print('='*60)


while verificador!= sorteada:
    while True:
        try:
            palpite = str(input('Digite uma palavra: ')).upper().strip()
        except Exception as erro:
            print(f'Digite somente palavras. {erro.__class__}')
        else:
            if len(palpite) <= 12:
                break
            else:
                print('A palavra deve ter no máximo 12 letras')
                print('-'*60)
    contador += 1
    mostrador = []
    verificador = [x for x in palpite]

    if len(palpite) <= len(sorteada):
        acertos = list(map(lambda x, y: f'\033[42m {x} \033[m' if x == y else y, sorteada, palpite))

        for x in acertos:
            if x in sorteada and mostrador.count(f'\033[43m {x} \033[m') < sorteada.count(x) and mostrador.count(f'\033[42m {x} \033[m') < sorteada.count(x):
                mostrador.append(f'\033[43m {x} \033[m')
            elif 'm' in x:
                mostrador.append(x)
            else:
                mostrador.append(f'\033[40m {x} \033[m')

    else:
        acertos = list(map(lambda x, y: f'\033[42m {y} \033[m' if x == y else x, palpite, sorteada))

        i = len(sorteada)

        for e in palpite[i:]:
            acertos.append(e)

        for x in acertos:
            if x in sorteada and mostrador.count(f'\033[43m {x} \033[m') < sorteada.count(x) and mostrador.count(f'\033[42m {x} \033[m') < sorteada.count(x):
                mostrador.append(f'\033[43m {x} \033[m')
            elif 'm' in x:
                mostrador.append(x)
            else:
                mostrador.append(f'\033[40m {x} \033[m')
    
    print('-'*60)
    print(f"{''.join(mostrador)}")
    print('-'*60)

print('='*60)
print(f'{'PARABENS!':^60}')
print(f'{f'Você encontrou a palavra em {contador} tentativas!':^60}')
print('='*60)
            
            


    