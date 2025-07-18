import pandas as pd
from models.titulo import Titulo


df = pd.read_csv(r'C:\Users\guilherme.seehagen\OneDrive - UNIOESTE\Área de Trabalho\mq3_trabalho\data\tesouro_direto_titulos.csv')

# Converte a rentabilidade para decimal (7.62 → 0.0762)
df['Rentabilidade anual'] = df['Rentabilidade anual'].astype(float) / 100

# Cria os títulos
titulos = [
    Titulo(
        nome=row['Título'],
        vencimento=row['Vencimento'],
        taxa_juros_anual=row['Rentabilidade anual']
    )
    for _, row in df.iterrows()
]

# Teste
titulos[2].resumo_do_titulo()