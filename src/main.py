import pandas as pd
from models.titulo import Titulo  


df = pd.read_csv(r'C:\Users\guilherme.seehagen\OneDrive - UNIOESTE\Área de Trabalho\mq3_trabalho\data\tesouro_direto_titulos.csv')

titulos = []

for _, row in df.iterrows():
    titulo = Titulo(
        nome=row['Título'],
        vencimento=row['Vencimento'],
        taxa_juros_anual=row['Rentabilidade anual']
    )
    titulos.append(titulo)

#Teste do titulo
print(titulos[0].resumo_do_titulo())