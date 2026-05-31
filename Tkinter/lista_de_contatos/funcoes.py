info = dict()
contatos = list()
botoes = list()

# ==== Configurações janela de contato ===
def abrir_novo_contato(frame, root):
    import customtkinter as ctk
    add_contato = ctk.CTkToplevel()
    add_contato.title("Novo Contato")
    w = 350
    h = 260
    root.update_idletasks()

    x_frame = root.winfo_x()
    y_frame = root.winfo_y()
    w_frame = root.winfo_width()
    h_frame = root.winfo_height()

    pos_x = x_frame + w_frame // 2 - w // 2
    pos_y = y_frame + h_frame // 2 - h // 2

    add_contato.geometry(f'{w}x{h}+{pos_x}+{pos_y}')
    
    add_contato.grab_set()
    add_contato.focus_force()

    lbl_nome = ctk.CTkLabel(add_contato, text = 'Nome: ', font=('Arial', 14))
    lbl_nome.place(x = 20, y = 20)

    etr_nome = ctk.CTkEntry(add_contato, width=230)
    etr_nome.place(x = 90, y = 20)

    lbl_numero = ctk.CTkLabel(add_contato, text='Telefone: ', font=('Arial', 14))
    lbl_numero.place(x = 20, y = 60)

    etr_numero = ctk.CTkEntry(add_contato, width=230)
    etr_numero.place(x = 90, y = 60)

    lbl_email = ctk.CTkLabel(add_contato, text='E-mail: ', font=('Arial', 14))
    lbl_email.place(x = 20, y = 100)

    etr_email = ctk.CTkEntry(add_contato, width = 230)
    etr_email.place(x = 90, y = 100)

    lbl_endereco = ctk.CTkLabel(add_contato, text='Endereço: ', font=('Arial', 14))
    lbl_endereco.place(x = 20, y = 140)

    etr_endereco = ctk.CTkEntry(add_contato, width=230)
    etr_endereco.place(x=90, y = 140)

    # Botão Adicionar e Cancelar

    btn_add = ctk.CTkButton(add_contato, text='Adicionar', command= lambda: adicionar(etr_nome, etr_numero, etr_email, etr_endereco, add_contato, frame, root))
    btn_add.place(x = 180, y=200)

    btn_cancel = ctk.CTkButton(add_contato, text='Cancelar', fg_color="#F33939", command= add_contato.destroy)
    btn_cancel.place(x=20, y=200)

def adicionar(*etr):
    global info
    global contatos
    print(etr)
    info['nome'] = etr[0].get().strip()
    info['telefone'] = etr[1].get().strip()
    info['email'] = etr[2].get().strip()
    info['endereco'] = etr[3].get().strip()
    contatos.append(info.copy())
    info.clear()
    criar_contato(etr[5], etr[6])
    etr[4].destroy()

def criar_contato(janela, root):
    global botoes
    import customtkinter as ctk
    global contatos
    contato = ctk.CTkButton(janela, text = contatos[-1]['nome'], fg_color="#414141", hover_color="#666666", width=450, anchor= 'w')
    contato.pack(side='top', fill='x', padx=10, pady=5)
    contato.configure(command= lambda n=contatos[-1], c=contato: press(n, c,  janela, root))
    botoes.append(contato)
    print(botoes)

def press(n, c,  janela, root):
    global contatos
    import customtkinter as ctk
    add_contato = ctk.CTkToplevel()
    add_contato.title("Novo Contato")
    w = 350
    h = 260
    root.update_idletasks()

    x_frame = root.winfo_x()
    y_frame = root.winfo_y()
    w_frame = root.winfo_width()
    h_frame = root.winfo_height()

    pos_x = x_frame + w_frame // 2 - w // 2
    pos_y = y_frame + h_frame // 2 - h // 2

    add_contato.geometry(f'{w}x{h}+{pos_x}+{pos_y}')
    add_contato.grab_set()
    add_contato.focus_force()
    

    lbl_nome = ctk.CTkLabel(add_contato, text = 'Nome: ', font=('Arial', 14))
    lbl_nome.place(x = 20, y = 20)

    etr_nome = ctk.CTkEntry(add_contato, width=230, fg_color="#242424")
    etr_nome.place(x = 90, y = 20)
    etr_nome.insert(0, n['nome'])
    etr_nome.configure(state= 'readonly')

    lbl_numero = ctk.CTkLabel(add_contato, text='Telefone: ', font=('Arial', 14))
    lbl_numero.place(x = 20, y = 60)

    etr_numero = ctk.CTkEntry(add_contato, width=230, fg_color="#242424")
    etr_numero.place(x = 90, y = 60)
    etr_numero.insert(0, n['telefone'])
    etr_numero.configure(state= 'readonly')

    lbl_email = ctk.CTkLabel(add_contato, text='E-mail: ', font=('Arial', 14))
    lbl_email.place(x = 20, y = 100)

    etr_email = ctk.CTkEntry(add_contato, width = 230, fg_color="#242424")
    etr_email.place(x = 90, y = 100)
    etr_email.insert(0, n['email'])
    etr_email.configure(state= 'readonly')

    lbl_endereco = ctk.CTkLabel(add_contato, text='Endereço: ', font=('Arial', 14))
    lbl_endereco.place(x = 20, y = 140)

    etr_endereco = ctk.CTkEntry(add_contato, width=230, fg_color="#242424")
    etr_endereco.place(x=90, y = 140)
    etr_endereco.insert(0, n['endereco'])
    etr_endereco.configure(state= 'readonly')

    # Botão Adicionar e Cancelar

    btn_editar = ctk.CTkButton(add_contato, text='Editar')
    btn_editar.place(x = 180, y=200)
    btn_editar.configure(command= lambda: editar(n, c, etr_nome, etr_numero, etr_email, etr_endereco, add_contato, btn_editar, btn_Excluir) )

    btn_Excluir = ctk.CTkButton(add_contato, text='Excluir', fg_color="#F33939", command= lambda: excluir(n, c, add_contato))
    btn_Excluir.place(x=20, y=200)

def editar(n, c, *etr):
    import customtkinter as ctk
    etr[0].configure(state='normal')
    etr[0].configure(fg_color = "#555555")
    etr[1].configure(state='normal')
    etr[1].configure(fg_color = "#555555")
    etr[2].configure(state='normal')
    etr[2].configure(fg_color = "#555555")
    etr[3].configure(state='normal')
    etr[3].configure(fg_color = "#555555")
    etr[5].destroy()
    etr[6].destroy()
    btn_salvar = ctk.CTkButton(etr[4], text='Salvar', command= lambda: salvar(n, c, etr[0], etr[1], etr[2], etr[3], etr[4]))
    btn_salvar.place(x = 180, y=200)
    btn_cancelar = ctk.CTkButton(etr[4], text='Cancelar', fg_color="#F33939", command= etr[4].destroy)
    btn_cancelar.place(x=20, y=200)
    

def salvar(n, c, *etr):
    global contatos
    n['nome'] = etr[0].get()
    n['telefone'] = etr[1].get()
    n['email'] = etr[2].get()
    n['endereco'] = etr[3].get()
    c.configure(text=n['nome'])
    etr[4].destroy()


def excluir(n, contato, add):
    global contatos
    contatos.pop(contatos.index(n))
    contato.destroy()
    add.destroy()


def pesquisar(etr, janela, root):
    global botoes
    global contatos
    nome = etr.get()
    n=0
    c=0
    for contato in contatos:
        if contato['nome'] == nome:
            n = contato
    for b in botoes:
        if b.cget('text') == nome:
            c = b
    if n != 0 and c != 0:
        press(n, c, janela, root)