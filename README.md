# 🥊 Análise Interativa do Ranking P4P do UFC

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Dash](https://img.shields.io/badge/Dash-2.17%2B-blue?style=for-the-badge&logo=dash)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-purple?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-green?style=for-the-badge&logo=plotly)
![Scraping](https://img.shields.io/badge/Scraping-Requests_&_BS4-orange?style=for-the-badge&logo=python)

---

### 🎯 Sobre o Projeto

Este projeto nasceu da fusão entre a paixão pelo MMA e a ciência de dados. Inspirado por um debate sobre a crescente dominância de lutadores não-americanos no UFC, o objetivo foi investigar essa hipótese com dados. A aplicação combina um histórico de rankings P4P (2020-2025) com informações demográficas coletadas via web scraping, apresentando os resultados em um dashboard interativo construído com Dash. O projeto demonstra um fluxo completo de análise de dados: desde a coleta e limpeza até a visualização e interpretação de insights.

---

### ✨ Principais Funcionalidades

* **🤖 Coleta de Dados via Web Scraping:** Um script customizado com `Requests` e `BeautifulSoup4` extrai dados detalhados (país, idade, altura, etc.) diretamente dos perfis dos lutadores no site oficial do UFC.
* **📊 Dashboard Interativo:** Interface rica construída com `Dash`, apresentando quatro análises visuais principais sobre a evolução e o perfil dos atletas no ranking P4P.
* **🔄 Unificação de Múltiplas Fontes:** Combina e padroniza dados de um dataset do Kaggle com os dados extraídos pelo web scraper, criando uma base de análise coesa e enriquecida.
* **🛠️ Engenharia de Features:** Criação de novas colunas, como a categorização de lutadores por `Região`, para permitir uma análise segmentada e responder à questão central do projeto.
* **📈 Análises Visuais Detalhadas:** O dashboard inclui:
    * Evolução da representatividade no Top 15.
    * Análise de dominância no Top 5.
    * Comparativo de ranking médio entre grupos.
    * Distribuição de idade dos atletas no ranking mais recente.
* **⏳ Análise Histórica:** A base de dados consolidada cobre um período de mais de quatro anos, permitindo a identificação de tendências de médio a longo prazo.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Dashboard:** Dash
* **Manipulação de Dados:** Pandas
* **Visualização de Dados:** Plotly
* **Web Scraping:** Requests, BeautifulSoup4
* **Utilitários:** Tqdm (para barras de progresso), Re (Expressões Regulares)

---

### 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Dash:**
    ```bash
    python app.py
    ```
5.  **Acesse o dashboard** no seu navegador através do endereço `http://127.0.0.1:8050/`.

---

### 💡 Principais Insights

A análise revelou que a percepção de dominância é, de fato, uma tendência estatística. Embora a presença geral de lutadores caucasianos no Top 15 seja estável, sua ocupação no Top 5 e sua performance média melhoraram significativamente nos últimos anos.

---

### 🏁 Conclusão

A análise de dados realizada neste projeto permite concluir que a proeminência de lutadores caucasianos no topo do ranking P4P do UFC não é um acontecimento súbito. Pelo contrário, trata-se do clímax de uma tendência de performance sustentada, com indicadores claros de crescimento desde 2022, como a ocupação crescente de vagas no Top 5 e a melhora do ranking médio coletivo.

Os insights extraídos dos dados validam e contextualizam a narrativa atual do esporte. O debate, que frequentemente surge em discussões e artigos, encontra nos números uma base factual sólida.

> **Artigo de Referência:** A inspiração central para esta investigação veio da seguinte notícia, que articula a percepção do cenário atual do UFC:
>
> ### [**Islam Makhachev Reveals Real Reason For Non-American Dominance In UFC**](https://www.yardbarker.com/general_sports/articles/islam_makhachev_reveals_real_reason_for_non_american_dominanceinufc/s1_17325_42635261)

---

# UFC-P4P-Dashboard