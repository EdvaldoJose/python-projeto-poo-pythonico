from typing import Dict


class Estoque:
    def __init__(self, produtos: Dict[str, int]) -> None:
        self.produtos = produtos

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        if nome not in self.produtos or quantidade > self.produtos[nome]:
            raise ValueError(
                f"Produto{nome} Noa encontrado ou quantidade insuficiente"
                )
        self.produtos[nome] -= quantidade

    def atualizar_produto_no_estoque(self, nome: str, nova_quantidade: int) -> None:
        if nome not in self.produtos:
            raise ValueError(f"Produto {nome} nao encontrado")
        self.produtos[nome] = nova_quantidade

    def visualizar_estoque(self) -> None:
        for produto, quantidade in self.produtos.items():
            print(f"{produto}: {quantidade}")
