import customtkinter as ctk
import csv
import os
from random import choice

class JogoPalavra(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Descubra a Palavra Secreta")
        self.geometry("600x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Variáveis do Jogo
        self.palavras = self.carregar_palavras()
        self.sorteada = choice(self.palavras).upper().strip()
        self.contador = 0
        self.tamanho_maximo = 12

        # --- Elementos da Interface ---
        
        # Título principal
        self.lbl_titulo = ctk.CTkLabel(self, text="DESCUBRA A PALAVRA SECRETA", font=("Arial", 24, "bold"))
        self.lbl_titulo.pack(pady=(20, 5))

        # Dica de tamanho
        self.lbl_dica = ctk.CTkLabel(self, text=f"A palavra tem {len(self.sorteada)} letras.", font=("Arial", 14), text_color="gray")
        self.lbl_dica.pack(pady=(0, 10))

        # Legenda de cores
        frame_legenda = ctk.CTkFrame(self, fg_color="transparent")
        frame_legenda.pack(pady=10)
        ctk.CTkLabel(frame_legenda, text="  Letra Certa  ", fg_color="#2ecc71", text_color="black", corner_radius=5).pack(side="left", padx=5)
        ctk.CTkLabel(frame_legenda, text=" Posição Errada ", fg_color="#f1c40f", text_color="black", corner_radius=5).pack(side="left", padx=5)

        # Frame rolável onde as tentativas vão aparecer
        self.frame_tentativas = ctk.CTkScrollableFrame(self, width=500, height=400)
        self.frame_tentativas.pack(pady=10, fill="both", expand=True, padx=20)

        # Entrada de texto e botão
        frame_input = ctk.CTkFrame(self, fg_color="transparent")
        frame_input.pack(pady=20)

        self.entry_palpite = ctk.CTkEntry(frame_input, width=250, font=("Arial", 18), placeholder_text="Digite seu palpite...")
        self.entry_palpite.pack(side="left", padx=10)
        self.entry_palpite.bind("<Return>", self.processar_palpite) # Permite usar o Enter

        self.btn_enviar = ctk.CTkButton(frame_input, text="Enviar", font=("Arial", 16, "bold"), command=self.processar_palpite)
        self.btn_enviar.pack(side="left")

        # Label de avisos e mensagens finais
        self.lbl_aviso = ctk.CTkLabel(self, text="", font=("Arial", 16, "bold"), text_color="#e74c3c")
        self.lbl_aviso.pack(pady=(0, 20))

    def carregar_palavras(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_csv = os.path.join(diretorio_atual, 'palavras.csv')
        palavras = []

        try:
            with open(caminho_csv, 'r', encoding='utf-8') as file:
                leitor = csv.reader(file)
                next(leitor) # Pula cabeçalho
                for linha in leitor:
                    # Assumindo que o CSV tem as palavras na primeira coluna ou em uma lista na linha
                    if linha: 
                        palavras.extend(linha)
        except FileNotFoundError:
            # Palavras de emergência caso o CSV não seja encontrado
            print("Aviso: 'palavras.csv' não encontrado. Usando lista padrão.")
            palavras = ["PYTHON", "DESAFIO", "CODIGO", "TERMINAL", "SISTEMA", "PROGRAMA"]
        
        # Filtra palavras vazias
        return [p for p in palavras if p.strip()]

    def processar_palpite(self, event=None):
        palpite = self.entry_palpite.get().upper().strip()
        
        # Limpa o aviso
        self.lbl_aviso.configure(text="", text_color="#e74c3c")

        if not palpite.isalpha():
            self.lbl_aviso.configure(text="Erro: Digite somente letras!")
            return

        if len(palpite) > self.tamanho_maximo:
            self.lbl_aviso.configure(text=f"A palavra deve ter no máximo {self.tamanho_maximo} letras!")
            return

        # Limpa a caixa de texto
        self.entry_palpite.delete(0, 'end')
        self.contador += 1

        self.exibir_tentativa_grid(palpite)

        if palpite == self.sorteada:
            self.finalizar_jogo(vitoria=True)

    def exibir_tentativa_grid(self, palpite):
        # Frame para a linha da tentativa atual
        frame_linha = ctk.CTkFrame(self.frame_tentativas, fg_color="transparent")
        frame_linha.pack(pady=5)

        # Lógica de verificação tipo Wordle (lida corretamente com letras duplicadas)
        letras_secretas = list(self.sorteada)
        cores = ["#7f8c8d"] * len(palpite) # Padrão: Cinza (Letra não existe)

        # Primeira passagem: Achar as letras na posição exata (VERDE)
        for i in range(min(len(palpite), len(letras_secretas))):
            if palpite[i] == letras_secretas[i]:
                cores[i] = "#2ecc71" # Verde
                letras_secretas[i] = None # Anula para não contar dobrado depois

        # Segunda passagem: Achar letras certas em posições erradas (AMARELO)
        for i in range(len(palpite)):
            if cores[i] == "#2ecc71": # Pula os verdes
                continue
            if palpite[i] in letras_secretas:
                cores[i] = "#f1c40f" # Amarelo
                letras_secretas[letras_secretas.index(palpite[i])] = None

        # Criar os quadradinhos (Labels) na interface
        for i, char in enumerate(palpite):
            lbl_letra = ctk.CTkLabel(
                frame_linha, 
                text=char, 
                width=40, height=40, 
                fg_color=cores[i], 
                text_color="black" if cores[i] != "#7f8c8d" else "white", 
                font=("Arial", 20, "bold"),
                corner_radius=5
            )
            lbl_letra.pack(side="left", padx=3)

    def finalizar_jogo(self, vitoria):
        # Desabilita botões e inputs
        self.entry_palpite.configure(state="disabled")
        self.btn_enviar.configure(state="disabled")

        if vitoria:
            self.lbl_aviso.configure(
                text=f"PARABÉNS! Você encontrou a palavra em {self.contador} tentativas!",
                text_color="#2ecc71"
            )

if __name__ == "__main__":
    app = JogoPalavra()
    app.mainloop()