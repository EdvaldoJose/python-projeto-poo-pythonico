class Produto:
    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        pass

    def get_preco(self) -> float:
        pass

    def get_quantidade(self) -> int:
        pass

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        pass

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        pass

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        pass
