from lista_contatos.contato import Contato
import pytest

def test_cria_contato_sem_email_sem_endereco():
    contato = Contato(1, "Breno", "(82)98888-5555")
    assert contato.nome == "Breno"
    assert contato.telefone == "82988885555"

def test_levanta_erro_ao_criar_contato_sem_nome_ou_email():
    with pytest.raises(ValueError):
        contato = Contato(1, "", "82988885555")
    with pytest.raises(ValueError):
        contato = Contato(1, "Breno", "")

def test_levanta_erro_ao_criar_contato_com_telefone_invalido():
    with pytest.raises(ValueError):
        contato = Contato(1, "Breno", "8888-5555")

def test_cria_contato_com_email_e_endereco():
    contato = Contato(1, "Breno", "82988885555", "seuemail@dominio.com", "rua de um lugar")
    assert contato.nome == "Breno"
    assert contato.telefone == "82988885555"
    assert contato.email == "seuemail@dominio.com"
    assert contato.endereco == "rua de um lugar"

def test_levanta_erro_ao_criar_contato_com_email_invalido():
    with pytest.raises(ValueError):
        contato = Contato(1, "Breno", "82988885555", "email@gmail")

def test_editar_atualiza_o_atributo_corretamente():
    contato = Contato(1, "Breno", "82988885555", "email@dominio.com", "endereco")

    assert contato.nome == "Breno"
    assert contato.telefone == "82988885555"

    contato.editar("Ellie")

    assert contato.nome == "Ellie"
    assert contato.telefone == "82988885555"

    contato.editar(telefone="82977775555")

    assert contato.nome == "Ellie"
    assert contato.telefone == "82977775555"

def test_para_dict_retorna_um_dicionario_valido():
    contato = Contato(1, "Breno", "82988885555", "email@dominio.com", "endereco")

    assert contato.para_dict() == {
        "id": 1,
        "nome": "Breno",
        "telefone": "82988885555",
        "email": "email@dominio.com",
        "endereco": "endereco"
    }

def test_de_dict_retorna_um_objeto_contato():
    dado = {
        "id": 1,
        "nome": "Breno",
        "telefone": "82988885555",
        "email": "email@gmail.com",
        "endereco": "endereco"
    }

    contato = Contato.de_dict(dado)

    assert contato.id == 1
    assert contato.nome == "Breno"
    assert contato.telefone == "82988885555"
    
