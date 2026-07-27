from lista_contatos.repositorio import RepositorioJson
from lista_contatos.agenda import Agenda
import json
import pytest

def test_rejeita_json_invalido(tmp_path):
    caminho_json = tmp_path / "contatos.json"

    caminho_json.write_text('[{"id": 1, "nome": "Breno", "telefone": "82988884444",}]')

    repositorio = RepositorioJson(caminho_json)

    with pytest.raises(ValueError):
        repositorio.carregar()

def test_rejeita_json_que_nao_retorne_lista(tmp_path):
    caminho_json = tmp_path / "contatos.json"

    caminho_json.write_text('{"id": 1, "nome": "Breno", "telefone": "82988884444"}')

    repositorio = RepositorioJson(caminho_json)

    with pytest.raises(ValueError):
        repositorio.carregar()   

def test_salva_json_valido(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)

    agenda.adicionar("Breno", "82988884444")

    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    assert isinstance(dados, list)
    assert dados == [{
        "id": 1,
        "nome": "Breno",
        "telefone": "82988884444",
        "email": "Email não cadastrado.",
        "endereco": "Endereço não cadastrado."
        }]

    