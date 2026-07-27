from lista_contatos.contato import Contato
import json
from pathlib import Path

class RepositorioJson:
    def __init__(self, caminho_repo:str = None):
        if caminho_repo is None:
            diretorio = Path()
            caminho_repo = diretorio / "dados" / "contatos.json"
            self.__caminho_repo = caminho_repo
        else:
            self.__caminho_repo = Path(caminho_repo)

    @property
    def caminho_repo(self):
        return self.__caminho_repo
    
    def salvar(self, dados):
        caminho = self.__caminho_repo

        dados = [contato.para_dict() for contato in dados]

        if not caminho.exists():
            caminho.parent.mkdir(parents=True, exist_ok=True)

        with open(caminho, 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)

    def carregar(self):
        caminho = self.__caminho_repo

        if not caminho.exists():
            return []
        
        try:
            with open(caminho, 'r', encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError:
            raise ValueError("O arquivo possui um json inválido.")
        
        if not isinstance(dados, list):
            raise ValueError("O arquivo de contatos deve conter uma lista.")
        
        try:
            contatos = [Contato.de_dict(dado) for dado in dados]
        except (KeyError, TypeError, ValueError):
            raise ValueError("O arquivo de contatos contém dados inválidos.")
        
        return contatos