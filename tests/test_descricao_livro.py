from src.livro.livro import Livro


def test_descricao_livro():
    titulo = "Pense em Python",
    autor = "Pense em Python",
    paginas = 309,

    livro = Livro(titulo, autor, paginas)
    descricao = (f"O livro {titulo} de {autor} possui {paginas} páginas.")
    assert (repr(livro) == descricao)
