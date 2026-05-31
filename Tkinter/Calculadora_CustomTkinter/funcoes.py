resu = 0

def key_press(event, etr):
    k = event.char
    # Permite apenas caracteres válidos no teclado e converte '*' para 'x'
    if k in '0123456789+-/*().c^':
        if k == '*': 
            press('x', etr)
        else: 
            press(k, etr)

def enter_press(event, etr):
    calcular(etr)

def back_press(event, etr):
    delete(etr)

def esc_press(event, etr):
    press('c', etr)    

def delete(etr):
    global resu
    etr.configure(state='normal')
    texto_atual = etr.get()
    
    if resu == 'error':
        resu = 0
        etr.delete(0, 'end')
    elif len(texto_atual) > 0:
        etr.delete(len(texto_atual) - 1, 'end')
        # Zera a variável resu para que o programa saiba que estamos a editar a conta,
        # impedindo que o visor seja limpo indevidamente ao inserir o próximo número.
        resu = 0 
        
    etr.configure(state='readonly')

def pow(etr):
    global resu
    texto_atual = etr.get()
    
    if resu == 'error':
        return
        
    if texto_atual == '':
        press('0', etr)
        press('^', etr)
        press('2', etr)
    # Só insere o '^2' se o último caractere não for um operador
    elif texto_atual[-1] not in 'x/+-.^(':
        press('^', etr)
        press('2', etr)

def raiz(etr):
    from math import sqrt
    global resu
    etr.configure(state='normal')
    
    try:
        # Se não há resultado anterior, calcula a expressão que está no visor primeiro
        if resu == 0 and etr.get() != '':
            valor = eval(etr.get().replace('x', '*').replace('^', '**'))
        else:
            valor = float(resu) if resu != 'error' else 0
            
        resu = sqrt(valor)
        
        # Remove os decimais se for um número inteiro (ex: 3.0 vira 3)
        if isinstance(resu, float) and resu.is_integer():
            resu = int(resu)
            
    except:
        resu = 'error'
        
    etr.delete(0, 'end')
    etr.insert(0, resu)
    etr.configure(state='readonly')

def calcular(etr):
    global resu
    etr.configure(state='normal')
    try:
        expressao = etr.get().replace('x', '*').replace('^', '**')
        if expressao:
            resu = eval(expressao)
            # Converte para inteiro se for exato para ficar visualmente mais limpo
            if isinstance(resu, float) and resu.is_integer():
                resu = int(resu)
        else:
            resu = 0
    except:
        resu = 'error'
        
    etr.delete(0, 'end')
    etr.insert('end', resu)
    etr.configure(state='readonly')

def press(n, etr):
    global resu
    etr.configure(state='normal')
    texto_atual = etr.get()
    
    if n == 'c':
        resu = 0
        etr.delete(0, 'end')
        
    elif resu == 'error':
        resu = 0
        etr.delete(0, 'end')
        # Após um erro, se o utilizador digitar um número ou sinal, inicia no ecrã
        if n.isnumeric() or n in '(-':
            etr.insert('end', n)
            
    elif resu != 0:
        # Se há um resultado no ecrã e o utilizador insere um operador, continua a conta
        if n in 'x/+-.^':
            resu = 0
            etr.insert('end', n)
        # Se insere um número, limpa o visor e começa uma nova conta
        else:
            resu = 0
            etr.delete(0, 'end')
            etr.insert('end', n)
            
    else: # resu == 0
        # Evita a sobreposição de dois operadores (substitui o antigo pelo novo)
        if texto_atual != '' and texto_atual[-1] in 'x/+-.^' and n in 'x/+-.^':
            etr.delete(len(texto_atual) - 1, 'end')
            etr.insert('end', n)
            
        # Regras de início de linha: impede começar com operadores (exceto - e parêntesis)
        elif texto_atual == '' and n in 'x/+.^':
            pass 
            
        # Evita a repetição consecutiva de pontos decimais (..)
        elif n == '.' and texto_atual != '' and texto_atual[-1] == '.':
            pass
            
        # Fluxo normal
        else:
            etr.insert('end', n)
            
    etr.configure(state='readonly')