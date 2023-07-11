from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("Pense em Python", "Allen B. Downey", 309)
    assert livro.titulo == "Pense em Python"
    assert livro.autor == "Allen B. Downey"
    assert livro.paginas == 309
