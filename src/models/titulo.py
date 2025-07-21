class Titulo:
    def __init__(self, nome, taxa_juros_anual, vencimento):
        self.nome = nome
        self.vencimento = vencimento
        self.taxa_juros_anual = taxa_juros_anual

    def taxa_mensal(self):
        return (1 + self.taxa_juros_anual) ** (1/12) - 1
    
    def resumo_do_titulo(self):
        print(f'Título: {self.nome}')
        print(f'Vencimento: {self.vencimento}')
        print(f'Taxa Anual: {self.taxa_juros_anual * 100:.2f}%')
        print(f'Taxa Mensal Equivalente: {self.taxa_mensal() * 100:.4f}%')