import json
from pathlib import Path


class Livro:
    def __init__(self, id_livro:int, titulo:str, autor:str):
        self.atualizar(titulo, autor)
        self._id_livro = id_livro

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def id(self):
        return self._id_livro

    def descricao(self):
        return f"{self._titulo} | {self._autor} | ID: {self._id_livro}"

    def atualizar(self, titulo:str, autor:str):
        titulo = titulo.strip()
        autor = autor.strip()

        if not titulo:
            raise ValueError("O título deve conter ao menos um caracter.")
        if not autor:
            raise ValueError("O autor deve conter ao menos um caracter.")
        
        self._titulo = titulo
        self._autor = autor

    def para_dict(self):
        return {
            "id": self._id_livro,
            "titulo": self._titulo,
            "autor": self._autor
        }

    @classmethod
    def de_dict(cls, dados_livro:dict):
        return cls(dados_livro["id"], dados_livro["titulo"], dados_livro["autor"])


class CatalogoLivros:
    def __init__(self, repositorio):
        self._repositorio = repositorio
        self._livros = self._repositorio.carregar()
        self._prox_id = max([livro.id for livro in self._livros], default=0)+1

    def adicionar(self, titulo:str, autor:str):
        livro = Livro(self._prox_id, titulo, autor)
        self._prox_id += 1
        self._livros.append(livro)
        self._repositorio.salvar(self._livros)

    def listar(self):
        return sorted(self._livros, key= lambda livro: livro.titulo.casefold())

    def buscar(self, id_livro):
        for livro in self._livros:
            if livro.id == id_livro:
                return livro
        return None

    def buscar_titulo(self, texto:str):
        livros_correspondentes = [livro for livro in self._livros if texto.strip().casefold() in livro.titulo.casefold()]
        return sorted(livros_correspondentes, key= lambda livro: livro.titulo.casefold())


    def editar(self, id_livro, titulo=None, autor=None):
        livro = self.buscar(id_livro)

        if livro is None:
            return False

        if titulo is None:
            titulo = livro.titulo
        if autor is None:
            autor = livro.autor
        
        livro.atualizar(titulo, autor)
        self._repositorio.salvar(self._livros)
        
        return True

    def remover(self, id_livro):
        livro = self.buscar(id_livro)
        if livro is None:
            return False
        self._livros.remove(livro)
        self._repositorio.salvar(self._livros)
        return True


class RepositorioJSON:
    def __init__(self, caminho_repo = None):
        if caminho_repo is None:
            diretorio = Path()
            caminho_repo = diretorio / "livros.json"
            self._caminho_repo = caminho_repo
        else:
            self._caminho_repo = Path(caminho_repo)

    def salvar(self, info):
        caminho = self._caminho_repo

        if not caminho.exists():
            caminho.parent.mkdir(parents=True, exist_ok=True)

        dados = [livro.para_dict() for livro in info]

        with open(caminho, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)

    def carregar(self):
        caminho = self._caminho_repo

        if not caminho.exists():
            return []

        try:
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError as erro:
            raise ValueError("O arquivo de livros contém um JSON inválido.") from erro

        if not isinstance(dados, list):
            raise ValueError("O arquivo de livros deve conter uma lista.")

        try:
            return [Livro.de_dict(livro) for livro in dados]
        except (KeyError, TypeError, ValueError) as erro:
            raise ValueError("O arquivo contém dados de livros inválidos.") from erro





