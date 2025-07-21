# Simulador de Aposentadoria com Títulos Públicos
## Contexto do Projeto

Este programa foi desenvolvido como parte de um trabalho para a disciplina de Métodos Quantitativos III, do curso de Ciências Econômicas da Universidade Estadual do Oeste do Paraná (UNIOESTE).

O objetivo era criar um relatório detalhado de um plano de aposentadoria para um cliente hipotético (baseado no próprio autor), utilizando títulos do Tesouro Direto. A análise deveria ser respaldada em valores e ilustrada com gráficos, considerando premissas justificadas sobre a vida financeira e os objetivos do cliente.

## Funcionalidades

- **Simulação de Patrimônio:** Calcula a evolução do patrimônio ao longo de décadas, considerando aportes mensais, juros compostos e progressão de carreira.

- **Análise Comparativa:** Compara o desempenho do plano de investimentos em diferentes títulos públicos (Prefixados, IPCA+, etc.).

- **Geração de Relatórios Visuais:** Plota gráficos claros e informativos sobre a evolução do patrimônio, o crescimento dos aportes e comparações entre estratégias (aporte único vs. mensal).

- **Modelagem de Premissas:** Permite a customização de todas as variáveis do cliente, como idade, perfil de investidor, metas financeiras e modelo de carreira.


## Premissas do Modelo de Simulação

Todas as premissas foram definidas buscando um equilíbrio entre a realidade do cliente (um jovem estudante) e a conjuntura econômica brasileira, conforme solicitado no trabalho.

### Perfil do Cliente-Base

* **Idade Atual:** 20 anos.

* **Idade de Aposentadoria:** 70 anos. A idade mínima pelo INSS é de 65 anos para homens, mas foi adotada uma margem para um planejamento mais realista e conservador.

* **Expectativa de Vida:** 80 anos. Para um homem brasileiro de 20 anos, a expectativa de vida segundo a Tábua de Mortalidade do IBGE 2021 é de 74.9 anos (20 + 54.9). Adotou-se 80 anos como margem de segurança para o plano.

    * *Fonte: [IBGE - Tábuas Completas de Mortalidade](https://www.ibge.gov.br/estatisticas/sociais/populacao/9126-tabuas-completas-de-mortalidade.html)*

* **Salário Atual:** R$ 3.000,00. Valor estipulado para simular um salário inicial de um economista recém-formado, em vez de um salário de estágio.

* **Renda Desejada na Aposentadoria:** R$ 10.000,00 por mês, valor considerado suficiente para um padrão de vida confortável.


### Modelo de Progressão de Carreira

Para simular o aumento da capacidade de aporte, foi adotado um modelo de aumentos salariais reais (acima da inflação) em três fases:

1.  **Início de Carreira (Primeiros 10 anos):** Aumento de **5% ao ano**, refletindo o período de rápido aprendizado e promoções iniciais.

2.  **Fase de Consolidação (11º ao 25º ano):** Aumento de **2.5% ao ano**, representando um crescimento mais contido, típico de um profissional sênior.

3.  **Auge/Platô de Carreira (após o 25º ano):** Aumento de **1% ao ano**, representando a estabilização salarial no auge da carreira.


### Perfil de Investimento

Define o percentual da renda mensal que será aportado. Foram consideradas 3 categorias:

* **CONSERVADOR:** 10% da renda/mês.

* **MODERADO:** 15% da renda/mês.

* **ARROJADO:** 25% da renda/mês.

Para as simulações, foi adotado o perfil **MODERADO**, por ser uma categoria intermediária e sustentável no longo prazo.

### Análise da escolha dos títulos e comparações:

Ao analisar os títulos disponíveis, uma análise superficial poderia levar à escolha do Tesouro Prefixado, que no momento da coleta de dados apresentava a maior taxa de juros nominal (acima de 14% a.a.). De fato, as simulações nominais mostram que este título geraria o maior montante financeiro bruto ao final do período.

No entanto, o objetivo de um plano de aposentadoria de longuíssimo prazo (40 anos de acumulação) não é simplesmente maximizar um valor nominal, mas sim garantir e maximizar o poder de compra futuro do investidor. Nesse contexto, o principal risco a ser mitigado é a incerteza inflacionária, especialmente considerando o histórico econômico do Brasil.

A escolha por um título Prefixado representa uma aposta de alto risco. O investidor trava uma taxa de juros por décadas, correndo o risco de que a inflação média no período seja superior a essa taxa, o que resultaria em uma perda real de poder de compra.

Por outro lado, os títulos Tesouro IPCA+ (incluindo o Tesouro Renda+) são desenhados especificamente para eliminar este risco. Eles garantem uma rentabilidade real (acima da inflação) fixa e conhecida no momento da compra (ex: 7,14% a.a.). Isso significa que, independentemente do cenário inflacionário futuro, o investidor tem a certeza de que seu poder de compra crescerá a essa taxa garantida anualmente.



Conclusão da Análise:

Considerando o objetivo de longo prazo e a necessidade de segurança e previsibilidade, a estratégia mais prudente e profissionalmente recomendada é focar nos títulos Tesouro IPCA+. Eles são o instrumento mais adequado para garantir que o cliente não apenas atinja sua meta financeira em termos nominais, mas que esse valor tenha o poder de compra desejado no momento da aposentadoria.



## Estrutura do Código (Paradigma Orientado a Objetos)

O paradigma escolhido foi o de OOP, pois o problema se divide naturalmente em 3 objetos bem definidos:

* **`Investidor`**: Classe que abstrai as premissas do cliente (idade, perfil, renda, etc.) e contém os métodos para as simulações da evolução patrimonial.

* **`Titulo`**: Classe que serve para instanciar os diversos títulos públicos como objetos a partir de um arquivo CSV, facilitando a manipulação e a simulação com qualquer combinação de ativos.

* **`RelatorioInvestimento`**: Classe que recebe um objeto `Investidor`, processa seus dados e retorna as visualizações gráficas de acordo com o título de escolha, separando a lógica de análise da lógica de visualização.



## Bibliotecas/Módulos

* Python 3

* Pandas

* Matplotlib

* NumPy


## Como Executar

1.  Certifique-se de que o arquivo `tesouro_direto_titulos.csv` e `historico_ipca.csv` está na pasta correta, conforme especificado no notebook.

2.  Instale as dependências necessárias: `pip install pandas matplotlib numpy jupyterlab`.

3.  Abra e execute as células do notebook `test.ipynb`. As premissas do cliente podem ser alteradas na Célula 2, e as análises serão geradas sequencialmente.