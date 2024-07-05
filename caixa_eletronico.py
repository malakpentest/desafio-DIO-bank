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
        print('==' * 30)
        print('{:^60}'.format('BANCO DO FEFEBANK'))
        print('==' * 30)
        print('')
        print('{:^60}'.format('MENU PRINCIPAL'))
        print('==' * 30)
        print('')
        print('{}  {}  {}'.format('Deposito', '_' * 47, '1'))
        print('')
        print('{}  {}  {}'.format('Saque', '__' * 25, '2'))
        print('')
        print('{}  {}  {}'.format('Extrato', '_' * 48, '3'))
        print('')
        print('{}  {}  {}'.format('Sair', '_' * 51, '4'))
        print('')
        print('==' * 30)

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
