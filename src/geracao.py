# %%
#########################
#  Carregando os Dados  #
#########################

import pandas as pd
from models.titulo import Titulo
from models.investidor import Investidor, PerfilInvestidor
from models.relatorio_investimento import RelatorioInvestimento

# Carregamento dos dados dos títulos
df = pd.read_csv(r'C:\mq3\sim_tesouro_prev\data\tesouro_direto_titulos.csv') 
df['Rentabilidade anual'] = df['Rentabilidade anual'].astype(float)

# Cria uma lista de objetos 'Titulo' a partir do DataFrame
titulos = [
    Titulo(
        nome=row['Título'],
        vencimento=row['Vencimento'],
        taxa_juros_anual=row['Rentabilidade anual'] / 100
    )
    for _, row in df.iterrows()
]

# Carregamento dos dados históricos do IPCA
df_ipca = pd.read_csv(r'C:\mq3\sim_tesouro_prev\data\historico_ipca.csv', sep=';')
df_ipca['aumento_ipca'] = df_ipca['aumento_ipca'].astype(float) / 100

# %%
#####################################
# DEFINIÇÃO DAS PREMISSAS DO CLIENTE#
#####################################

cliente_perfil = {
    'idade': 30, # Idade de início do investimento
    'idade_aposentadoria': 60, # Idade de aposentadoria
    'renda_atual': 1000,# Salário mensal
    'expectativa_vida': 90, # Expectativa de vida -- Tábua de Mortalidade do IBGE
    'renda_desejada': 3000, # Renda mensal desejada na aposentadoria
    'perfil': PerfilInvestidor.ARROJADO, # 15% do salário
    'aumento_salario': 0 # Inicialmente pensou em se usar essa variável.
}

# Instancia o objeto do cliente
# O 'titulo' aqui é apenas um placeholder, já que as simulações pedem o título como argumento.
cliente = Investidor(**cliente_perfil, titulo=titulos[0])

print("Perfil do cliente definido:")
print(cliente_perfil)

# Cria o objeto de relatório para este cliente (instância única)
relatorio_cliente = RelatorioInvestimento(investidor=cliente)

# %%
###################################
# DEFINIÇÃO DOS TÍTULOS DE ANÁLISE#
###################################

# Títulos selecionados para diferentes análises
titulo_recomendado = titulos[16]  # Título principal para análise detalhada
titulo_prefixado_analise = titulos[2]  # Para análise de cenários inflacionários
titulo_ipca_analise = titulos[16]  # Para comparação com prefixado

print(f"Título Recomendado para Análise Principal: {titulo_recomendado.nome}")
print(f"Título Prefixado para Análise de Cenários: {titulo_prefixado_analise.nome}")
print(f"Título IPCA+ para Análise de Cenários: {titulo_ipca_analise.nome}")

# %%
################################
# CÁLCULOS PRINCIPAIS DA META #
################################

# Cálculos fundamentais para o planejamento
meta_fv = cliente.calcular_valor_necessario_aposentadoria()
aporte_unico_equivalente = cliente.calcular_aporte_unico_equivalente(titulo_recomendado)
aporte_necessario_fixo = cliente.calcular_investimento_mensal_necessario()

print(f"\n--- Cálculos Base da Simulação ---")
print(f"Meta de Aposentadoria (FV): R$ {meta_fv:,.2f}")
print(f"Aporte Único Equivalente (PV) para a meta: R$ {aporte_unico_equivalente:,.2f}")
print(f"Aporte Mensal Fixo (teórico) necessário: R$ {aporte_necessario_fixo:,.2f}")

# Atualiza o valor no objeto para uso posterior
cliente.aporte_unico = aporte_unico_equivalente

# %%
###########################################
# ANÁLISE PRINCIPAL E GERAÇÃO DOS GRÁFICOS#
############################################

print(f"\n--- Gerando Análises para o Título Recomendado: {titulo_recomendado.nome} ---")

# a) Evolução do Patrimônio
print("Gerando Gráfico 1: Evolução do Patrimônio...")
relatorio_cliente.plotar_evolucao_patrimonio(titulo=titulo_recomendado)

# b) Evolução dos Aportes
print("Gerando Gráfico 2: Evolução dos Aportes Mensais...")
relatorio_cliente.plotar_evolucao_aportes()

# c) Análise de Aporte Único vs. Mensal
print("Gerando Gráfico 3: Aporte Único Equivalente vs. Aportes Mensais...")
relatorio_cliente.plotar_aporte_mensal(titulo=titulo_recomendado)

# d) Gráfico de Depleção do Patrimônio
print("Gerando Gráfico 4: Depleção do Patrimônio na Aposentadoria...")
relatorio_cliente.plotar_deplecao_patrimonio(titulo_recomendado)

# %%
########################################
# ANÁLISE DE CENÁRIOS INFLACIONÁRIOS  #
########################################

# Análise da inflação histórica para definição de cenários
ipca_recente = df_ipca[df_ipca['ano'] >= 2004]
media_historica = ipca_recente['aumento_ipca'].mean()
desvio_padrao_historico = ipca_recente['aumento_ipca'].std()

# Define os cenários com base nesses dados
cenario_inflacao_base = media_historica
cenario_inflacao_otimista = media_historica - desvio_padrao_historico
cenario_inflacao_pessimista = media_historica + desvio_padrao_historico

print("\n--- Cenários de Inflação Baseados em Dados Históricos (2004-2024) ---")
print(f"Cenário Base (Média): {cenario_inflacao_base:.2%}")
print(f"Cenário Pessimista (Média + 1 DP): {cenario_inflacao_pessimista:.2%}")
print(f"Cenário Otimista (Média - 1 DP): {cenario_inflacao_otimista:.2%}")

print(f"\nAnalisando o Risco do '{titulo_prefixado_analise.nome}' contra a segurança do '{titulo_ipca_analise.nome}'.")

# Geração do gráfico de cenários inflacionários
print("Gerando Gráfico 5: Análise de Cenários Inflacionários...")
relatorio_cliente.plotar_analise_cenarios_inflacao(
    titulo_prefixado=titulo_prefixado_analise,
    titulo_ipca=titulo_ipca_analise,
    inflacao_otimista=cenario_inflacao_otimista,
    inflacao_base=cenario_inflacao_base,
    inflacao_pessimista=cenario_inflacao_pessimista
)

# %%
#######################
# SUMÁRIO DA SIMULAÇÃO#
#######################

# Dados do perfil do cliente para o relatório
perfil_cliente = {
    'Idade Inicial': cliente.idade,
    'Idade de Aposentadoria': cliente.idade_aposentadoria,
    'Período de Acumulação': cliente.anos_ate_aposentadoria(),
    'Expectativa de Vida': cliente.expectativa_vida,
    'Período de Renda': cliente.calcular_tempo_aposentado(),
    'Renda Atual Mensal': f"R$ {cliente.renda_atual:,.2f}",
    'Renda Desejada na Aposentadoria': f"R$ {cliente.renda_desejada:,.2f}",
    'Perfil de Investidor': f"{cliente.perfil.name} ({cliente.perfil.value*100:.0f}% da renda)",
}

# Cálculos finais da simulação usando o título recomendado
patrimonio_final = cliente.patrimonio_final(titulo_recomendado) # Considera 15% de IR sobre o rendimento 
aportes_evolucao = cliente.calcular_evolucao_aportes_mensais()
aporte_inicial = aportes_evolucao[0]
aporte_final = aportes_evolucao[-1]
total_investido = sum(aportes_evolucao) * 12 # Multiplica por 12 pois a lista é de aportes mensais por ano
juros_totais = patrimonio_final - total_investido
percentual_juros = (juros_totais / patrimonio_final) * 100
superavit_deficit = patrimonio_final - meta_fv
renda_mensal_aposentadoria = cliente.renda_aposentadoria(titulo_recomendado)

# Geração do Texto Final
resumo_texto = f"""
======================================================================
        RESUMO DA SIMULAÇÃO FINANCEIRA PARA APOSENTADORIA
======================================================================

1. PERFIL DO CLIENTE E PREMISSAS
---------------------------------
{pd.Series(perfil_cliente).to_string()}

2. META FINANCEIRA
--------------------
- Título Base para Análise: {titulo_recomendado.nome}
- Taxa de Juro Real Anual: {titulo_recomendado.taxa_juros_anual * 100:.2f}%
- Patrimônio Necessário aos {cliente.idade_aposentadoria} anos (FV): R$ {meta_fv:,.2f}

3. PLANO DE ACUMULAÇÃO
-----------------------
- Aporte Mensal Inicial (aos {cliente.idade} anos): R$ {aporte_inicial:,.2f}
- Aporte Mensal Final (no último ano): R$ {aporte_final:,.2f}
- Valor Total Investido ao longo de {cliente.anos_ate_aposentadoria()} anos: R$ {total_investido:,.2f}

4. RESULTADO DA SIMULAÇÃO
--------------------------
- Patrimônio Final Projetado aos {cliente.idade_aposentadoria} anos: R$ {patrimonio_final:,.2f}
- Total de Juros Acumulados no Período: R$ {juros_totais:,.2f}
- Composição do Patrimônio Final: {percentual_juros:.2f}% proveniente de juros.

5. ANÁLISE DA META
-------------------
- Resultado vs. Meta: O plano de investimentos projetado SUPEROU a meta.
- Superávit/Déficit Projetado: R$ {superavit_deficit:,.2f}
- Renda alcançada na Aposentadoria: R$ {renda_mensal_aposentadoria:,.2f} mensais

"""

print(resumo_texto)


