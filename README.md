# agritech_optimization
Projeto para otimizar a aplicação de nitrogênio em agricultura usando dados ambientais.

# Projeto Agritech: Otimização da Aplicação de Nitrogênio

## 🎯 Objetivo do Projeto
O objetivo principal deste projeto é desenvolver um modelo de **Machine Learning** para prever e otimizar a quantidade ideal de **nitrogênio** a ser aplicada em plantações agrícolas. A análise utiliza dados históricos de variáveis ambientais (como temperatura, precipitação e umidade do solo) e dados da cultura, com o propósito de aumentar a eficiência e a sustentabilidade na agricultura.

Este projeto demonstra um pipeline completo de **Ciência de Dados**, desde a Análise Exploratória (EDA) e pré-processamento, até a modelagem e avaliação de performance.

## 📁 Estrutura do Repositório
* `data/`: Contém o dataset simulado utilizado na análise (`dataset_simulado.csv`).
* `notebooks/`: Armazena o notebook Jupyter (`01_analise_exploratoria.ipynb`) com todo o fluxo de trabalho e a documentação da análise.
* `src/`: Módulo Python com o código modularizado (`data_processing.py`), focado na reprodutibilidade do projeto.
* `README.md`: Este arquivo, que serve como a documentação principal do projeto.
* `requirements.txt`: Lista todas as bibliotecas e suas versões necessárias para a execução do projeto.

## 🛠️ Tecnologias e Dependências
* Python 3.11.8
* Pandas (para manipulação de dados)
* Scikit-learn (para modelagem e avaliação do modelo)
* Matplotlib & Seaborn (para visualização de dados)

Para instalar as dependências, execute o seguinte comando no terminal:
`pip install -r requirements.txt`

## 📊 Análise Exploratória de Dados (EDA)
A análise exploratória inicial revelou insights importantes sobre o dataset:
* O conjunto de dados possui 200 amostras e 8 variáveis. Não foram encontrados valores ausentes.
* **A variável alvo**, `Aplicacao_nitrogenio`, tem uma distribuição relativamente normal, com uma média de **59.9 kg/ha**.
* As visualizações (histogramas, boxplots e pairplots) mostraram fortes relações entre a aplicação de nitrogênio e variáveis como o **tipo de solo**, a **cultura** e o **estágio da cultura**. A cultura de milho, por exemplo, demonstrou maior variabilidade e uma média mais alta na aplicação de nitrogênio.

## 🧠 Metodologia de Machine Learning
1.  **Pré-processamento**: As variáveis categóricas (`Tipo_solo`, `Cultura`, `Estagio_cultura`) foram convertidas em um formato numérico usando **One-Hot Encoding**.
2.  **Divisão dos Dados**: O dataset foi dividido em 80% para treino e 20% para teste, garantindo que o modelo fosse avaliado em dados que ele nunca viu.
3.  **Modelagem**: Um modelo de **Regressão Linear** foi utilizado para prever a `Aplicacao_nitrogenio`. Este modelo foi escolhido pela sua simplicidade e interpretabilidade.
4.  **Avaliação**: A performance do modelo foi medida usando as métricas **$R^2$** e **MAE**.

## ✨ Resultados do Modelo
Após o treinamento e a avaliação, o modelo obteve as seguintes métricas:
* **R-quadrado ($R^2$):** 0.5055
    * Isso indica que o modelo consegue explicar aproximadamente **50.55%** da variabilidade na aplicação de nitrogênio, o que é um resultado promissor para a primeira iteração.
* **Erro Absoluto Médio (MAE):** 8.4485
    * Em média, a previsão do modelo tem um erro de **$8.45 kg/ha$** para mais ou para menos.

## 🧠 Metodologia de Machine Learning
1.  **Pré-processamento**: As variáveis categóricas (`Tipo_solo`, `Cultura`, `Estagio_cultura`) foram convertidas em um formato numérico usando **One-Hot Encoding**.
2.  **Divisão dos Dados**: O dataset foi dividido em 80% para treino e 20% para teste.
3.  **Modelagem**: Foram testados dois modelos: uma **Regressão Linear** para uma baseline e um **Random Forest Regressor** para capturar relações mais complexas nos dados.
4.  **Avaliação**: A performance dos modelos foi medida usando as métricas **$R^2$** e **MAE**.

## ✨ Resultados do Modelo
A tabela abaixo compara o desempenho dos modelos testados:

| Modelo | R-quadrado ($R^2$) | Erro Absoluto Médio (MAE) |
| :--- | :---: | :---: |
| Regressão Linear | 0.5055 | 8.4485 |
| **Random Forest** | **0.7088** | **7.0270** |

O **Random Forest** demonstrou um desempenho superior, conseguindo explicar mais da variabilidade da variável alvo e reduzindo o erro médio de previsão. O modelo final é robusto e demonstra que as variáveis ambientais e da cultura são fortes preditores para a otimização da aplicação de nitrogênio.

## ⏭️ Próximos Passos
O projeto pode ser aprimorado com as seguintes ações:
* Otimizar o modelo Random Forest com um ajuste de hiperparâmetros (como `GridSearchCV`).
* Explorar a possibilidade de usar dados mais complexos, como dados de satélite ou séries temporais.