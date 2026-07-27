from lista_contatos.agenda import Agenda

def test_agenda_adiciona_contato_e_retorna_lista_com_os_contatos():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")
    agenda.adicionar("Ellie", "82977776666")
    agenda.adicionar("Kevin", "82966667777")

    contatos = agenda.listar()

    assert contatos[0].nome == "Breno"
    assert contatos[1].nome == "Ellie"
    assert contatos[2].nome == "Kevin"

def test_agenda_busca_por_id():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")

    assert agenda.buscar_por_id(1).nome == "Breno"

def test_agenda_busca_por_id_retorna_falso_para_id_nao_cadastrado():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")

    assert not agenda.buscar_por_id(2)

def test_buscar_por_nome_retorna_lista_com_nomes_compativeis_sem_diferenciar_maiusculas_e_minusculas():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")
    agenda.adicionar("Brenovisk", "82977773333")
    agenda.adicionar("Ellie", "82922223333")
    agenda.adicionar("Kevin", "82944449999")

    resultados = agenda.buscar_por_nome("brEnO")

    assert resultados[0].nome == "Breno"
    assert resultados[1].nome == "Brenovisk"
    assert len(resultados) == 2

def test_retorna_falso_para_nome_nao_cadastrado():
    agenda = Agenda()
    agenda.adicionar("Breno", "82955556666")

    assert not agenda.buscar_por_nome("Bruno")

def test_edita_contato_e_salva_novo_contato():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")

    assert agenda.buscar_por_id(1).nome == "Breno"

    agenda.editar(1, nome="Ellie")

    assert agenda.buscar_por_id(1).nome == "Ellie"

def test_editar_retorna_falso_para_contato_nao_cadastrado():
    agenda = Agenda()
    agenda.adicionar("Breno", "82988885555")

    assert not agenda.editar(2, nome="Ellie")

def test_remove_contato_antes_presente_na_agenda():
    agenda = Agenda()
    agenda.adicionar("Breno", "82996574444")

    assert agenda.buscar_por_id(1)

    agenda.remover(1)

    assert not agenda.buscar_por_id(1)