# Simulador de Aposentadoria com Títulos Públicos
## Contexto do Projeto

Este programa foi desenvolvido como parte de um trabalho para a disciplina de Métodos Quantitativos III, do curso de Ciências Econômicas da Universidade Estadual do Oeste do Paraná (UNIOESTE).

O objetivo era criar um relatório detalhado de um plano de aposentadoria para um cliente hipotético (baseado no próprio autor), utilizando títulos do Tesouro Direto. A análise deveria ser respaldada em valores e ilustrada com gráficos, considerando premissas justificadas sobre a vida financeira e os objetivos do cliente.

## Funcionalidades

- **Simulação de Patrimônio:** Calcula a evolução do patrimônio ao longo de décadas, considerando aportes mensais, juros compostos e progressão de carreira.

- **Análise Comparativa:** Compara o desempenho do plano de investimentos em diferentes títulos públicos (Prefixados, IPCA+, etc.).

- **Geração de Relatórios Visuais:** Plota gráficos claros e informativos sobre a evolução do patrimônio, o crescimento dos aportes e comparações entre estratégias (aporte único vs. mensal).

- **Modelagem de Premissas:** Permite a customização de todas as variáveis do cliente, como idade, perfil de investidor, metas financeiras e modelo de carreira.


### Perfil do Cliente-Base

 **Idade Atual**

* **Idade de Aposentadoria**

* **Expectativa de Vida:** Pode ser calculada com base na idade do perfil analisado.
    * *Fonte: [IBGE - Tábuas Completas de Mortalidade](https://www.ibge.gov.br/estatisticas/sociais/populacao/9126-tabuas-completas-de-mortalidade.html)*

* **Salário Atual:**

* **Renda Desejada na Aposentadoria:** 


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



## Estrutura do Código (Paradigma Orientado a Objetos)

O paradigma escolhido foi o de OOP, pois o problema se divide naturalmente em 3 objetos bem definidos:

* **`Investidor`**: Classe que abstrai as premissas do cliente (idade, perfil, renda, etc.) e contém os métodos para as simulações da evolução patrimonial.

* **`Titulo`**: Classe que serve para instanciar os diversos títulos públicos como objetos a partir de um arquivo CSV, facilitando a manipulação e a simulação com qualquer combinação de ativos.

* **`RelatorioInvestimento`**: Classe que recebe um objeto `Investidor`, processa seus dados e retorna as visualizações gráficas de acordo com o título de escolha, separando a lógica de análise da lógica de visualização.



## Bibliotecas/Módulos

* Pandas

* Matplotlib

* NumPy


## Como Executar

1.  Certifique-se de que o arquivo `tesouro_direto_titulos.csv` e `historico_ipca.csv` está na pasta correta, conforme especificado no notebook.

2.  Instale as dependências necessárias: `pip install pandas matplotlib numpy jupyterlab`.

3.  Abra e execute as células do notebook `geracao.ipynb`. As premissas do cliente podem ser alteradas na Célula 3, e as análises serão geradas sequencialmente.
