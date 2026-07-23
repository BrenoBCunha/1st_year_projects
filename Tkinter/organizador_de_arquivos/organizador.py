import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path

caminho = ''
estado = False

def organizar(caminho):
    mapa_extensoes = {
        '.jpeg': 'imagem', '.png': 'imagem', '.jpg': 'imagem', '.gif': 'imagem', '.svg': 'imagem', '.webp': 'imagem', '.tif': 'imagem', '.tiff': 'imagem', '.cr2': 'imagem', '.nef': 'imagem',
        '.pdf': 'PDF',
        '.doc': 'documentos', '.docx': 'documentos', '.odt': 'documentos', '.txt': 'documentos', '.rtf': 'documentos', '.xlsx': 'documentos', '.xls': 'documentos', '.pptx': 'docuemntos', '.ppt': 'documentos',
        '.mp4': 'videos', '.mov': 'videos', '.avi': 'videos', '.wmv': 'videos', '.webm': 'videos',
        '.mp3': 'audios',
        '.exe': 'executaveis',
        '.zip': 'compactado', '.rar': 'compactado', '.7z': 'compactado', '.tar': 'compactado' 
    }

    diretorio = caminho

    try:
        for arquivo in diretorio.iterdir():
            if arquivo.is_file():
                tipo = arquivo.suffix.lower()
                if tipo in mapa_extensoes:
                    pasta_destino = diretorio / mapa_extensoes[tipo]
                    pasta_destino.mkdir(exist_ok=True)
                    destino_final = pasta_destino / arquivo.name
                    if not destino_final.exists():
                        arquivo.rename(destino_final)
                else:
                    pasta_destino = diretorio / 'outros'
                    pasta_destino.mkdir(exist_ok=True)
                    destino_final = pasta_destino / arquivo.name
                    if not destino_final.exists():
                        arquivo.rename(destino_final)
        
        remover_duplicados(caminho)

        mensagem = 'Pasta organizada com sucesso!'
        msg_lbl.config(text=mensagem)
        msg_lbl.config(fg='green')
    except FileNotFoundError:
        mensagem = 'Arquivo não encontrado'
        msg_lbl.config(text=mensagem)
        msg_lbl.config(fg='red')
        
def remover_duplicados(caminho):
    from pathlib import Path
    global estado
    diretorio = caminho
    pastas = ['imagem', 'PDF', 'documentos', 'videos', 'audios', 'executaveis', 'compactado']
    if estado:
        for pasta in diretorio.iterdir():
            if pasta.stem in pastas:
                for arquivo in pasta.glob('*(*).*'):
                    destino = diretorio / 'lixeira'
                    destino.mkdir(exist_ok=True)
                    destino_final = destino / arquivo.name
                    if not destino_final.exists():
                        arquivo.rename(destino_final)
                        
def buscar():
    global caminho
    pasta = filedialog.askdirectory()
    caminho = Path(pasta)
    frame.delete(0, 'end')
    frame.insert(0, caminho)

def alerta():
    global estado
    if not estado:
        messagebox.showinfo('Alerta', 'Esta aplicação não é capaz de ler arquivos individualmente. Arquivos com mesmo nome e mesma extensão serão deletados mantendo-se apenas o mais recente. Tem certeza que deseja continuar?')
        estado = True
    else:
        estado = False

root = tk.Tk()
root.title('Organizador')
root.geometry('400x200')

titulo_lbl = tk.Label(root, text='Selecione a pasta que deseja organizar: ')
titulo_lbl.place(x=20, y=10)

frame = tk.Entry(root, width=50)
frame.place(x = 20, y = 43)

bus_btn = tk.Button(root, text='Explorar', command=lambda: buscar())
bus_btn.place(x = 330, y=40)

rd_chb = tk.Checkbutton(root, text='Remover arquivos duplicados', command=lambda: alerta(), variable=estado)
rd_chb.place(x=20, y=70)

org_btn = tk.Button(root, text='Organizar', command=lambda: organizar(caminho))
org_btn.place(x = 170, y = 110)

msg_lbl = tk.Label(root, text='')
msg_lbl.place(x=120, y = 140)

root.mainloop()