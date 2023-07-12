from src.livro.livro import Livro


def test_cria_livro():
    titulo = "Pense em Python"
    autor = "Allen B. Downey"
    paginas = 309

    livro = Livro(titulo, autor, paginas)
    assert livro.titulo == titulo
    assert livro.autor == autor
    assert livro.paginas == 309
