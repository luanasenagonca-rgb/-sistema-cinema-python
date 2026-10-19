import sys


class Cinema:
    def __init__(self, filme, classificacao_idade, total_assentos):
        self.filme = filme
        self.classificacao_idade = classificacao_idade
        self.total_assentos = total_assentos
        self.assentos_disponiveis = total_assentos
        self.ingressos_vendidos = []

    def exibir_painel(self):
        print("\n" + "=" * 45)
        print("  PAINEL DO CINEMA - SESSÃO ATUAL")
        print("=" * 45)
        print(f" Filme: {self.filme}")
        print(f" Classificação: {self.classificacao_idade} anos")
        print(
            f" Lotação: {self.assentos_disponiveis}/{self.total_assentos} assentos livres"
        )
        print("=" * 45)

    def validar_idade(self, idade):
        return idade >= self.classificacao_idade

    def vender_ingresso(self, nome, idade, tipo_ingresso):
        if self.assentos_disponiveis <= 0:
            print("\n❌ ERRO: Sessão esgotada! Não há assentos disponíveis.")
            return False

        if not self.validar_idade(idade):
            print(
                f"\n❌ ENTRADA NEGADA: O cliente tem {idade} anos. "
                f"A classificação mínima para '{self.filme}' é "
                f"{self.classificacao_idade} anos."
            )
            return False

        preco = 15.00 if tipo_ingresso.lower() == "meia" else 30.00
        numero_assento = self.total_assentos - self.assentos_disponiveis + 1

        ingresso = {
            "id": len(self.ingressos_vendidos) + 1,
            "nome": nome,
            "assento": numero_assento,
            "tipo": tipo_ingresso.capitalize(),
            "preco": preco,
        }

        self.ingressos_vendidos.append(ingresso)
        self.assentos_disponiveis -= 1
        self._imprimir_comprovante(ingresso)
        return True

    def _imprimir_comprovante(self, ingresso):
        print("\n" + "-" * 35)
        print("      🎟️  INGRESSO EMITIDO  🎟️")
        print("-" * 35)
        print(f" Ticket ID : #{ingresso['id']:04d}")
        print(f" Cliente   : {ingresso['nome']}")
        print(f" Filme     : {self.filme}")
        print(f" Assento   : A-{ingresso['assento']:02d}")
        print(f" Tipo      : {ingresso['tipo']}")
        print(f" Valor     : R$ {ingresso['preco']:.2f}")
        print("-" * 35 + "\n")


def menu_principal():
    cinema = Cinema(filme="Batman", classificacao_idade=14, total_assentos=5)

    while True:
        cinema.exibir_painel()
        print("1. Processar Entrada / Vender Ingresso")
        print("2. Ver Lista de Entradas Confirmadas")
        print("3. Sair do Sistema")

        opcao = input("\nEscolha uma opção (1-3): ").strip()

        if opcao == "1":
            print("\n--- CADASTRO DE CLIENTE ---")
            nome = input("Nome do cliente: ").strip()

            try:
                idade = int(input("Idade do cliente: "))
            except ValueError:
                print("❌ Idade inválida! Digite apenas números.")
                continue

            tipo = input("Tipo de ingresso (1 - Inteira / 2 - Meia): ").strip()
            tipo_str = "Meia" if tipo == "2" else "Inteira"
            cinema.vender_ingresso(nome, idade, tipo_str)

        elif opcao == "2":
            print("\n" + "=" * 45)
            print("  LISTA DE ENTRADAS CONFIRMADAS")
            print("=" * 45)
            if not cinema.ingressos_vendidos:
                print("Nenhum ingresso vendido ainda.")
            else:
                for ing in cinema.ingressos_vendidos:
                    print(
                        f"Assento A-{ing['assento']:02d} | {ing['nome']} | "
                        f"Tipo: {ing['tipo']}"
                    )
            print("=" * 45)

        elif opcao == "3":
            print("\nEncerrando sistema de controle do cinema. Até logo!")
            sys.exit()

        else:
            print("\n❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
