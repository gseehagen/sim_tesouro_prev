# investidor.py (Versão Refatorada)

from models.titulo import Titulo
from enum import Enum
import numpy as np

class PerfilInvestidor(Enum):

    CONSERVADOR = 0.10
    MODERADO = 0.15
    ARROJADO = 0.25

class Investidor:
    """Representa o investidor, suas metas e capacidade de simulação."""
    
    def __init__(self, idade, idade_aposentadoria, renda_atual, expectativa_vida, 
                 renda_desejada, titulo: Titulo, perfil: PerfilInvestidor, 
                 aumento_salario, aporte_unico=0):
        self.idade = idade  
        self.idade_aposentadoria = idade_aposentadoria 
        self.renda_atual = renda_atual
        self.expectativa_vida = expectativa_vida
        self.renda_desejada = renda_desejada
        self.titulo = titulo # Título base, pode ser usado para algumas premissas
        self.perfil = perfil
        self.aumento_salario = aumento_salario
        self.aporte_unico = aporte_unico

    def anos_ate_aposentadoria(self):
        return self.idade_aposentadoria - self.idade
    
    def calcular_tempo_aposentado(self):
        return self.expectativa_vida - self.idade_aposentadoria

    def calcular_valor_necessario_aposentadoria(self):
        anos_aposentadoria = self.calcular_tempo_aposentado()
        return self.renda_desejada * 12 * anos_aposentadoria
    
    def simular_aporte_unico_evolucao(self, titulo):
        anos = self.anos_ate_aposentadoria()
        evolucao = []
        for ano in range(anos + 1):
            valor = self.aporte_unico * (1 + titulo.taxa_juros_anual) ** ano
            evolucao.append(valor)
        return evolucao

    def calcular_investimento_mensal_necessario(self):
        taxa_juros_anual = self.titulo.taxa_juros_anual
        n = self.anos_ate_aposentadoria() * 12
        i = (1 + taxa_juros_anual)**(1/12) - 1
        fv = self.calcular_valor_necessario_aposentadoria()
        
        if i == 0:
            return fv / n
        return fv * i / ((1 + i)**n - 1)
    

    def simular_investimento_mensal_evolucao(self, titulo):
        salario = self.renda_atual
        aporte_mensal = salario * self.perfil.value
        meses = self.anos_ate_aposentadoria() * 12
        montante = 0
        evolucao = [0]
        
        ano_de_carreira = 0  
        
        for mes in range(1, meses + 1):
            montante = (montante + aporte_mensal) * (1 + titulo.taxa_mensal())
            
            if mes % 12 == 0:
                evolucao.append(montante)
                ano_de_carreira += 1  # Incrementa um ano de carreira a cada iteração
                
                if ano_de_carreira <= 10:
                    salario *= (1 + 0.05) 
                elif ano_de_carreira <= 25:
                    salario *= (1 + 0.025)
                else:
                    salario *= (1 + 0.01)

                aporte_mensal = salario * self.perfil.value
        
        return evolucao

    def calcular_evolucao_aportes_mensais(self):
        evolucao_aportes = []
        salario_atual = self.renda_atual
        
        # Contador de 'ano de carreira
        for ano_de_carreira in range(1, self.anos_ate_aposentadoria() + 1):
            
            # Primeiro, calcula e armazena o aporte do ano atual
            aporte_mensal = salario_atual * self.perfil.value
            evolucao_aportes.append(aporte_mensal)
            
            # Depois, calcula o novo salário para o ANO SEGUINTE
            # com base na fase da carreira
            if ano_de_carreira <= 10:         
                salario_atual *= (1 + 0.05)
            elif ano_de_carreira <= 25:       
                salario_atual *= (1 + 0.025)
            else:                             
                salario_atual *= (1 + 0.01)
                
        return evolucao_aportes

    def calcular_aporte_unico_equivalente(self, titulo_base):
        fv = self.calcular_valor_necessario_aposentadoria()
        taxa_juros_anual = titulo_base.taxa_juros_anual
        n_anos = self.anos_ate_aposentadoria()
        pv = fv / ((1 + taxa_juros_anual) ** n_anos)
        return pv


    def calcular_juro_real(self, taxa_nominal, taxa_inflacao):
        #Calcula a taxa de juro real com base em uma taxa nominal e na inflação.
        return ((1 + taxa_nominal) / (1 + taxa_inflacao)) - 1