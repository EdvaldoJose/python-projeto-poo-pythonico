class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return (
            f"O livro {self.titulo}"
            f" de {self.autor}"
            f" possui {self.paginas} páginas."
        )
