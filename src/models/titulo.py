import pandas as pd
import matplotlib.pyplot as plt

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

    def valor_futuro(self, montante_investido, anos):
        return montante_investido * (1 + self.taxa_juros_anual)**anos
    
    def simular_investimento(self, valor_inicial, aporte_mensal, anos):
        dados = []
        montante = valor_inicial
        for mes in range(1, anos * 12 + 1):
            montante *= (1 + self.taxa_mensal())
            montante += aporte_mensal
            dados.append({"Mês": mes, "Montante": montante})
        return pd.DataFrame(dados)

    def gerar_fluxo_caixa(self):
        # Exemplo simplificado: gráfico de evolução do montante
        df = self.simular_investimento(valor_inicial=1000, aporte_mensal=500, anos=10)
        plt.plot(df["Mês"], df["Montante"])
        plt.title(f"Evolução do Investimento: {self.nome}")
        plt.xlabel("Meses")
        plt.ylabel("Montante (R$)")
        plt.grid()
        plt.show()