class Titulo:
    def __init__(self, nome, taxa_juros_anual, vencimento):
        self.nome = nome
        self.vencimento = vencimento
        self.taxa_juros_anual = taxa_juros_anual

    def taxa_mensal(self):
        return (1 + self.taxa_juros_anual) ** (1/12) - 1
    def resumo_do_titulo(self):
        print(f'A taxa anual é {self.taxa_juros_anual}')
        print(f'O vencimento do título é {self.vencimento}')
        print(f'O nome do título é {self.nome}')
        print(f'Sua taxa mensal equivalente é {self.taxa_mensal()}')
    
