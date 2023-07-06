from typing import Dict


class Estoque:
    def __init__(self, produtos: Dict[str, int]) -> None:
        pass

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        pass

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        pass

    def atualizar_produto_no_estoque(
        self, nome: str, nova_quantidade: int
    ) -> None:
        pass

    def visualizar_estoque(self) -> None:
        pass
