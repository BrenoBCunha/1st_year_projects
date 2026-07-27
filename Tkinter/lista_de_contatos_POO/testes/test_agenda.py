from lista_contatos.agenda import Agenda
from lista_contatos.repositorio import RepositorioJson

def test_listar_retorna_uma_lista_ordenada(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")
    agenda.adicionar("Ellie", "82977776666")
    agenda.adicionar("Kevin", "82966667777")

    contatos = agenda.listar()
    lista = [contato.nome for contato in contatos]

    assert lista == ["Breno", "Ellie", "Kevin"]

def test_agenda_busca_por_id_retorna_objeto_contato(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")

    assert agenda.buscar_por_id(1).nome == "Breno"

def test_agenda_busca_por_id_retorna_falso_para_id_nao_cadastrado(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")

    assert not agenda.buscar_por_id(2)

def test_buscar_por_nome_retorna_lista_com_nomes_compativeis_sem_diferenciar_maiusculas_e_minusculas(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")
    agenda.adicionar("Brenovisk", "82977773333")
    agenda.adicionar("Ellie", "82922223333")
    agenda.adicionar("Kevin", "82944449999")

    resultados = agenda.buscar_por_nome("brEnO")

    assert resultados[0].nome == "Breno"
    assert resultados[1].nome == "Brenovisk"
    assert len(resultados) == 2

def test_retorna_falso_para_nome_nao_cadastrado(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82955556666")

    assert not agenda.buscar_por_nome("Bruno")

def test_edita_contato_e_salva_novo_contato(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")

    assert agenda.buscar_por_id(1).nome == "Breno"

    agenda.editar(1, nome="Ellie")

    assert agenda.buscar_por_id(1).nome == "Ellie"

def test_editar_retorna_falso_para_contato_nao_cadastrado(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988885555")

    assert not agenda.editar(2, nome="Ellie")

def test_remove_contato_antes_presente_na_agenda(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82996574444")

    assert agenda.buscar_por_id(1)

    agenda.remover(1)

    assert not agenda.buscar_por_id(1)

# Testes de Persistencia dos Dados

def test_inicia_programa_sem_arquivo_criado(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)

    assert not caminho_json.exists()

    agenda.adicionar("Breno", "82988884444")

    assert caminho_json.exists()

def test_salva_contato_mesmo_apos_reiniciar_programa(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988884444") 

    assert agenda.buscar_por_id(1).nome == "Breno"

    novo_caminho = tmp_path / "contatos.json"
    novo_repositorio = RepositorioJson(novo_caminho)
    nova_agenda = Agenda(novo_repositorio)

    assert nova_agenda.buscar_por_id(1).nome == "Breno"

def test_contato_editado_e_salvo_apos_reiniciar_programa(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988884444") 

    assert agenda.buscar_por_id(1).nome == "Breno"

    agenda.editar(1, "Ellie")

    novo_caminho = tmp_path / "contatos.json"
    novo_repositorio = RepositorioJson(novo_caminho)
    nova_agenda = Agenda(novo_repositorio)

    assert nova_agenda.buscar_por_id(1).nome == "Ellie"

def test_remover_persiste_apos_reiniciar_programa(tmp_path):
    caminho_json = tmp_path / "contatos.json"
    repositorio = RepositorioJson(caminho_json)
    agenda = Agenda(repositorio)
    agenda.adicionar("Breno", "82988884444") 

    assert agenda.buscar_por_id(1).nome == "Breno"

    agenda.remover(1)

    novo_caminho = tmp_path / "contatos.json"
    novo_repositorio = RepositorioJson(novo_caminho)
    nova_agenda = Agenda(novo_repositorio)

    assert not agenda.buscar_por_id(1)
    