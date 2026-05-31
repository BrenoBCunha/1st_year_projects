import customtkinter as ctk
import funcoes as f

# ==== Configurações de interface ====
root = ctk.CTk()
root.title('Lista de Contatos')
root.geometry('500x600')
ctk.set_appearance_mode("Dark")
root.resizable(width = False, height = False)



# Configuração do Grid principal (2 colunas, 1 linha)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# ==== Frame pincipal (pesquisa e lista) ====
frame_principal = ctk.CTkFrame(root, fg_color="transparent")
frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1) # Permite que a lista expanda

# 1. Sub-frame da Barra de Pesquisa
frame_pesquisa = ctk.CTkFrame(frame_principal, fg_color="transparent")
frame_pesquisa.grid(row=0, column=0, sticky="ew", pady=(0, 20))
frame_pesquisa.grid_columnconfigure(0, weight=1)

entry_pesquisa = ctk.CTkEntry(frame_pesquisa, placeholder_text="Pesquisar por nome ou número...")
entry_pesquisa.grid(row=0, column=0, sticky="ew", padx=(0, 10))

btn_pesquisar = ctk.CTkButton(frame_pesquisa, text="Pesquisar", width=100, command= lambda: f.pesquisar(entry_pesquisa, frame_lista, root))
btn_pesquisar.grid(row=0, column=1)

# 2. Área da Lista de Contatos (Frame com Scroll)
frame_lista = ctk.CTkScrollableFrame(frame_principal, label_text="Meus Contatos")
frame_lista.grid(row=1, column=0, sticky="nsew")

btn_adicionar = ctk.CTkButton(frame_principal, text='+', font=('Arial', 40), width = 50, command= lambda: f.abrir_novo_contato(frame_lista, root))
btn_adicionar.place(x = 390, y = 490)

root.mainloop()