## Esse script cria a classe Investidor
from titulo import Titulo

class Investidor:
    def __init__(self, idade, idade_aposentadoria, renda_atual, expectativa_vida, renda_desejada, titulo: Titulo):
        self.idade = idade  
        self.idade_aposentadoria = idade_aposentadoria 
        self.renda_atual = renda_atual
        self.expectativa_vida = expectativa_vida
        self.renda_desejada = renda_desejada
        self.titulo = titulo

    def anos_ate_aposentadoria(self):
        return self.idade_aposentadoria - self.idade
    

    def calcular_tempo_aposentado(self):
        return self.expectativa_vida - self.idade_aposentadoria
    

    def calcular_valor_necessario_aposentadoria(self):
        anos_aposentadoria = self.calcular_tempo_aposentado
        return self.renda_mensal_desejada_aposentadoria * 12 * anos_aposentadoria
    
    def calcular_investimento_mensal_necessario(self, taxa_juros_anual):
        n = self.calcular_tempo_ate_apose() * 12
        i = (1 + taxa_juros_anual)**(1/12) - 1
        fv = self.calcular_valor_necessario_aposentadoria()
        
        if i == 0:
            return fv / n
        return fv * i / ((1 + i)**n - 1)
    
    def taxa_juros(self):
        return self.titulo.taxa_juros_anual
        
    

    
