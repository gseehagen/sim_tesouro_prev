import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from models.investidor import Investidor
from models.titulo import Titulo

class RelatorioInvestimento:
    def __init__(self, investidor: Investidor):
        self.investidor = investidor
    
    def plotar_aporte_mensal(self, titulo):
        evolucao_aporte_mensal = self.investidor.simular_investimento_mensal_evolucao(titulo)
        evolucao_aporte_unico = self.investidor.simular_aporte_unico_evolucao(titulo)
        anos = list(range(len(evolucao_aporte_mensal)))
        plt.figure(figsize=(14, 8))
        plt.plot(anos, evolucao_aporte_mensal, 
                label='Aportes Mensais', 
                linewidth=3, 
                color='#2E86AB',
                marker='o',
                markersize=4,
                alpha=0.8)
        plt.plot(anos, evolucao_aporte_unico, 
                label=f'Aporte Único (R$ {self.investidor.aporte_unico:,.0f})', 
                linewidth=3,
                color='#A23B72',
                marker='s',
                markersize=4,
                alpha=0.8)
        
        # Formatação
        plt.xlabel('Anos', fontsize=12, fontweight='bold')
        plt.ylabel('Valor Acumulado (R$)', fontsize=12, fontweight='bold')
        plt.title('Comparação: Aportes Mensais vs Aporte Único', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.legend(fontsize=11, loc='upper left')
        plt.grid(True, alpha=0.3)
        
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}K'))
        
        plt.tight_layout()
        plt.show()

    def plotar_evolucao_patrimonio(self, titulo):
        evolucao = self.investidor.simular_investimento_mensal_evolucao(titulo)
        anos = list(range(len(evolucao)))
        
        plt.figure(figsize=(12, 8))
        plt.plot(anos, evolucao, 
                linewidth=3, 
                color='#2E86AB',
                marker='o',
                markersize=5)
        plt.fill_between(anos, evolucao, alpha=0.3, color='#2E86AB')
        
        plt.xlabel('Anos', fontsize=12, fontweight='bold')
        plt.ylabel('Patrimônio Acumulado (R$)', fontsize=12, fontweight='bold')
        plt.title('Evolução do Patrimônio com Aportes Mensais', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.grid(True, alpha=0.3)
        
        # Formatação dos valores
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}K'))
        
        # Adiciona anotação do valor final
        plt.annotate(f'R$ {evolucao[-1]:,.0f}', 
                    xy=(anos[-1], evolucao[-1]), 
                    xytext=(anos[-1]-5, evolucao[-1]*1.1),
                    fontsize=12, fontweight='bold',
                    ha='center',
                    arrowprops=dict(arrowstyle='->', color='black'))
        
        plt.tight_layout()
        plt.show()


    def plotar_comparacao_titulos(self, lista_titulos, nomes_titulos=None):
            plt.figure(figsize=(14, 8))
            colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#592E83']
            
            for i, titulo in enumerate(lista_titulos[:5]):  # Máximo 5 títulos
                evolucao = self.investidor.simular_investimento_mensal_evolucao(titulo)
                anos = list(range(len(evolucao)))
                
                nome = nomes_titulos[i] if nomes_titulos else f"Título {i+1} ({titulo.taxa_juros_anual*100:.2f}%)"
                
                plt.plot(anos, evolucao, 
                        label=nome,
                        linewidth=3,
                        color=colors[i % len(colors)],
                        marker='o',
                        markersize=4,
                        alpha=0.8)
            
            plt.xlabel('Anos', fontsize=12, fontweight='bold')
            plt.ylabel('Patrimônio Acumulado (R$)', fontsize=12, fontweight='bold')
            plt.title('Comparação entre Diferentes Títulos Públicos', 
                    fontsize=16, fontweight='bold', pad=20)
            plt.legend(fontsize=10, loc='upper left')
            plt.grid(True, alpha=0.3)
            
            ax = plt.gca()
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}K'))
            
            plt.tight_layout()
            plt.show()



    def plotar_evolucao_aportes(self):

        aportes_mensais_por_ano = self.investidor.calcular_evolucao_aportes_mensais()
        anos = list(range(1, len(aportes_mensais_por_ano) + 1))

        plt.figure(figsize=(14, 8))

        bars = plt.bar(anos, aportes_mensais_por_ano, color='#1E8449', alpha=0.8)

        # Formatação
        plt.xlabel('Anos de Contribuição', fontsize=12, fontweight='bold')
        plt.ylabel('Valor do Aporte Mensal (R$)', fontsize=12, fontweight='bold')
        plt.title('Evolução Anual do Aporte Mensal (Efeito da Progressão de Carreira)', 
                fontsize=16, fontweight='bold', pad=20)
        plt.grid(True, axis='y', alpha=0.3, linestyle='--')

        # Formatação do eixo Y para mostrar como moeda.
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))

        # Adicionar o valor no topo da primeira e da última barra para dar contexto.
        if len(bars) > 0:
                primeira_barra = bars[0]
                ultima_barra = bars[-1]
                
                plt.text(primeira_barra.get_x() + primeira_barra.get_width()/2., primeira_barra.get_height(),
                        f'R$ {primeira_barra.get_height():.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
                        
                plt.text(ultima_barra.get_x() + ultima_barra.get_width()/2., ultima_barra.get_height(),
                        f'R$ {ultima_barra.get_height():.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

        plt.tight_layout()
        plt.show()

    def plotar_analise_cenarios_inflacao(self, titulo_prefixado, titulo_ipca, inflacao_otimista, inflacao_base, inflacao_pessimista):
        
        #Gráficos dos cenários de inflação

        # 1. Calcula os juros reais do Prefixado para cada cenário
        juro_real_otimista = self.investidor.calcular_juro_real(titulo_prefixado.taxa_juros_anual, inflacao_otimista)
        juro_real_base = self.investidor.calcular_juro_real(titulo_prefixado.taxa_juros_anual, inflacao_base)
        juro_real_pessimista = self.investidor.calcular_juro_real(titulo_prefixado.taxa_juros_anual, inflacao_pessimista)

        # 2. Cria "títulos virtuais" com essas taxas reais para usar na simulação
        prefixado_otimista = Titulo("Prefixado (Cenário Otimista)", juro_real_otimista, titulo_prefixado.vencimento)
        prefixado_base = Titulo("Prefixado (Cenário Base)", juro_real_base, titulo_prefixado.vencimento)
        prefixado_pessimista = Titulo("Prefixado (Cenário Pessimista)", juro_real_pessimista, titulo_prefixado.vencimento)

        # 3. Roda as 4 simulações
        evolucao_ipca = self.investidor.simular_investimento_mensal_evolucao(titulo_ipca)
        evolucao_prefixado_otimista = self.investidor.simular_investimento_mensal_evolucao(prefixado_otimista)
        evolucao_prefixado_base = self.investidor.simular_investimento_mensal_evolucao(prefixado_base)
        evolucao_prefixado_pessimista = self.investidor.simular_investimento_mensal_evolucao(prefixado_pessimista)
        
        anos = list(range(len(evolucao_ipca)))

        # Plotagem
        plt.figure(figsize=(14, 8))
        

        # Linha do IPCA +
        plt.plot(anos, evolucao_ipca, 
                label=f'Tesouro com rendimentos IPCA+ (Retorno Real Fixo: {titulo_ipca.taxa_juros_anual:.2%})', 
                color='#006400', linewidth=4, alpha=0.8)

        # Linhas tracejadas para os cenários do Prefixado
        plt.plot(anos, evolucao_prefixado_pessimista, 
                label=f'Prefixado - Cenário Pessimista (Inflação {inflacao_pessimista:.2%}, Juro Real {juro_real_pessimista:.2%})', 
                color='#D95D39', linestyle='--', linewidth=2)
        plt.plot(anos, evolucao_prefixado_base, 
                label=f'Prefixado - Cenário Base (Inflação {inflacao_base:.2%}, Juro Real {juro_real_base:.2%})', 
                color='#F1A208', linestyle='--', linewidth=2.5)
        plt.plot(anos, evolucao_prefixado_otimista, 
                label=f'Prefixado - Cenário Otimista (Inflação {inflacao_otimista:.2%}, Juro Real {juro_real_otimista:.2%})', 
                color='#2E86AB', linestyle='--', linewidth=2)
        
        # Formatação
        plt.xlabel('Anos de Contribuição', fontsize=12, fontweight='bold')
        plt.ylabel('Patrimônio Acumulado (Valor Real - R$)', fontsize=12, fontweight='bold')
        plt.title('Análise de Cenários: Retorno Real do Tesouro Prefixado vs. IPCA+', 
                fontsize=16, fontweight='bold', pad=20)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000000:.2f}M')) # Formatando para Milhões (M)
        
        plt.tight_layout()
        plt.show()