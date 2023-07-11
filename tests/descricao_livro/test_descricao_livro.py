from src.livro.livro import Livro


def test_descricao_livro():
    titulo = "Pense em Python",
    autor = "Pense em Python",
    paginas = 309,

    livro = Livro(titulo, autor, paginas)
    descricao = (f"O livro{titulo} do {autor} possui {paginas} paginas.")
    assert (
        repr(livro) == descricao
    )
