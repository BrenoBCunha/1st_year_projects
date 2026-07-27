
class Contato:
    def __init__(self, id_contato:int, nome:str, telefone:str, email:str = "", endereco:str = ""):
        self.__id_contato = id_contato
        self.atualizar(nome, telefone, email, endereco)


    @property
    def id(self):
        return self.__id_contato

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @property
    def endereco(self):
        return self.__endereco
    

    def atualizar(self, nome:str, telefone:str, email:str = "", endereco:str = ""):
        import re
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        nome = nome.strip()
        telefone = telefone.strip()
        email = email.strip()
        endereco = endereco.strip()

        telefone = self.normalizar_telefone(telefone)

        if not nome:
            raise ValueError("Nome deve conter ao menos um caracter")

        if not telefone or len(telefone) != 11:
            raise ValueError("Telefone inválido. Siga o formato: (DDD)90000-0000")

        if email and not re.match(padrao, email) and email != "Email não cadastrado.":
            raise ValueError("Email deve seguir o padrão: seuemail@dominio.com")


        self.__nome = nome
        self.__telefone = telefone

        if not email:
            self.__email = "Email não cadastrado."
        else:
            self.__email = email

        if not endereco:
            self.__endereco = "Endereço não cadastrado."
        else:
            self.__endereco = endereco

    def editar(self, nome:str='', telefone:str='', email:str='', endereco:str=''):
        nome = nome.strip()
        telefone = telefone.strip()
        email = email.strip()
        endereco = endereco.strip()

        if not nome:
            nome = self.nome
        if not telefone:
            telefone = self.telefone
        if not email:
            email = self.email
        if not endereco:
            endereco = self.endereco

        self.atualizar(nome, telefone, email, endereco)


    def normalizar_telefone(self, telefone):
        return "".join([char for char in telefone if char.isdigit()])


    def para_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "endereco": self.endereco
        }

    @classmethod
    def de_dict(cls, dado:dict):
        return cls(dado["id"], dado["nome"], dado["telefone"], dado["email"], dado["endereco"])


