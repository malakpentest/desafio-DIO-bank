# Projeto de Caixa Eletrônico

class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
        if 0 < valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para saque ou saldo insuficiente.")

    def extrato(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

if __name__ == "__main__":
    caixa = CaixaEletronico()

    while True:
        print("\nOpções:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Encerrar")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor do depósito: "))
            caixa.deposito(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor do saque: "))
            caixa.saque(valor_saque)
        elif opcao == "3":
            caixa.extrato()
        elif opcao == "4":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Escolha novamente.")
