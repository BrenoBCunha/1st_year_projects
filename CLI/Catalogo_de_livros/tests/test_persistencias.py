import pytest
from biblioteca import CatalogoLivros, RepositorioJSON, Livro
from pathlib import Path


### ---- BLOCO CatalogoLivros ---- ###

def test_inicia_programa_sem_arquivo_criado(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    assert not caminho_json.exists()

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    assert caminho_json.exists()


def test_livros_adicionados_permanecem_apos_reiniciar(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    novo_catalogo = CatalogoLivros(repositorio)
    livro = novo_catalogo.buscar(1)

    assert livro.titulo == "O Hobbit"


def test_livros_editados_sao_salvos_apos_reiniciar(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    catalogo.editar(1, titulo="Crime e Castigo", autor="Fiódor Dostoiévski")

    novo_catalogo = CatalogoLivros(repositorio)
    livro = novo_catalogo.buscar(1)

    assert livro.titulo == "Crime e Castigo" and livro.autor == "Fiódor Dostoiévski"


def test_livros_sao_removidos_e_remocao_salva_apos_reiniciar(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")    

    catalogo.remover(1)

    novo_catalogo = CatalogoLivros(repositorio)

    assert novo_catalogo.buscar(1) is None
    assert novo_catalogo.listar() == []


def test_rejeita_livro_sem_titulo_ou_autor(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)

    with pytest.raises(ValueError):
        catalogo.adicionar("", "J. R. R. Tolkien")  

    with pytest.raises(ValueError):
        catalogo.adicionar("O Hobbit", "")

    with pytest.raises(ValueError):
        catalogo.adicionar("", "")


def test_rejeita_edicao_sem_titulo_ou_autor(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    with pytest.raises(ValueError):
        catalogo.editar(1, "", "J. R. R. Tolkien")  

    with pytest.raises(ValueError):
        catalogo.editar(1, "O Hobbit", "")

    with pytest.raises(ValueError):
        catalogo.editar(1, "", "")
    

def test_busca_titulo_sem_diferenciar_maiuscula(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    assert isinstance(catalogo.buscar_titulo("o hObBi"), list) and not catalogo.buscar_titulo("o hObBit") == []


def test_buscar_retorna_objeto_livro(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")

    resultado = catalogo.buscar(1)

    assert isinstance(resultado, Livro)
    assert resultado.id == 1
    assert resultado.titulo == "O Hobbit"


def test_listar_retorna_uma_lista_ordenada(tmp_path):
    caminho_json = tmp_path / "livros.json"
    repositorio = RepositorioJSON(caminho_json)

    catalogo = CatalogoLivros(repositorio)
    catalogo.adicionar("O Hobbit", "J. R. R. Tolkien")
    catalogo.adicionar("1984", "George Orwell")
    catalogo.adicionar("Dom Casmurro", "Machado de Assis")

    titulos = [livro.titulo for livro in catalogo.listar()]

    assert titulos == ["1984", "Dom Casmurro", "O Hobbit"]



### ---- BLOCO RepositorioJSON ---- ###

def test_rejeita_json_invalido(tmp_path):
    caminho_json = tmp_path / "livros.json"

    caminho_json.write_text('[{"id": 1, "titulo": "O Hobbit",}]', encoding="utf-8")

    repositorio = RepositorioJSON(caminho_json)

    with pytest.raises(ValueError):
        repositorio.carregar()


def test_rejeita_json_que_nao_retorne_lista(tmp_path):
    caminho_json = tmp_path / "livros.json"
    
    caminho_json.write_text('{"id": 1, "titulo": "O Hobbit",}', encoding="utf-8")

    repositorio = RepositorioJSON(caminho_json)

    with pytest.raises(ValueError):
        repositorio.carregar()




