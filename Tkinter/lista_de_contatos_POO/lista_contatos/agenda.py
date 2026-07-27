from lista_contatos.contato import Contato

class Agenda:
    def __init__(self, repositorio):
        self.__repositorio = repositorio
        self.__contatos = repositorio.carregar()
        self.__prox_id = max([contato.id for contato in self.__contatos], default=0) + 1

    def adicionar(self, nome:str, telefone:str, email:str="", endereco:str=""):
        id_contato = self.__prox_id
        self.__prox_id += 1
        contato = Contato(id_contato, nome, telefone, email, endereco)
        self.__contatos.append(contato)
        self.__repositorio.salvar(self.__contatos)

    def listar(self):
        return sorted(self.__contatos, key=lambda contato: contato.nome.casefold())
    
    def buscar_por_id(self, id_contato):
        for contato in self.__contatos:
            if contato.id == id_contato:
                return contato
        return None
            
    def buscar_por_nome(self, texto):
        resultados = [contato for contato in self.__contatos if texto.casefold() in contato.nome.casefold()]
        return sorted(resultados, key=lambda contato: contato.nome)
    
    def editar(self, id_contato:int, nome:str='', telefone:str='', email:str='', endereco:str=''):
        contato = self.buscar_por_id(id_contato)
        if contato is None:
            return False
        contato.editar(nome, telefone, email, endereco)
        self.__repositorio.salvar(self.__contatos)

    def remover(self, id_contato):
        contato = self.buscar_por_id(id_contato)
        if contato is None:
            return False
        self.__contatos.remove(contato)
        self.__repositorio.salvar(self.__contatos)
