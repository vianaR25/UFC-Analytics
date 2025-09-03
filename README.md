# Análise de Dados: Ranking Peso-por-Peso do UFC (2020-2024)

## 1. Motivação

Este projeto foi inspirado por um debate crescente no mundo do MMA sobre a dominância de lutadores não-americanos, exemplificada por atletas como Islam Makhachev. O objetivo foi utilizar dados para verificar se essa percepção é uma tendência real e quantificável no ranking mais prestigiado do esporte, o Peso-por-Peso (P4P).

## 2. Tech Stack

* **Linguagem:** Python
* **Análise de Dados:** Pandas
* **Web Scraping:** Requests, BeautifulSoup4
* **Visualização e Dashboard:** Dash, Plotly
* **Utilitários:** Tqdm (para barras de progresso), Re (Expressões Regulares)

## 3. Como Executar o Projeto

Siga os passos abaixo para rodar o dashboard interativo localmente.

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
    *(Nota: Certifique-se de criar um arquivo `requirements.txt` com o comando `pip freeze > requirements.txt`)*

4.  **Execute o aplicativo Dash:**
    ```bash
    python app.py
    ```

5.  **Acesse o dashboard** no seu navegador através do endereço `http://127.0.0.1:8050/`.

## 4. Metodologia do Projeto

O desenvolvimento foi estruturado em quatro fases principais:

#### Passo 1: Coleta de Dados Primários
A base inicial foi um dataset do Kaggle contendo o histórico do ranking P4P masculino de 2020 a meados de 2024. Este dataset foi atualizado manualmente para incluir os rankings mais recentes, garantindo a análise até a data presente.

#### Passo 2: Web Scraping para Enriquecimento
Para obter dados demográficos essenciais (nacionalidade, idade, altura, etc.), foi desenvolvido o script `scrape_hometowns.py`. O processo utilizou a biblioteca **`requests`** para gerenciar sessões e fazer as chamadas HTTP à página de atletas do UFC. A biblioteca **`BeautifulSoup4`** foi usada para parsear o conteúdo HTML de cada página, permitindo a extração precisa dos dados. O script também utiliza a biblioteca **`re`** para limpar e formatar os nomes dos lutadores na construção das URLs e **`tqdm`** para exibir uma barra de progresso durante a execução, uma boa prática para scripts de longa duração.

#### Passo 3: Tratamento e Engenharia de Features
Esta foi a fase mais crítica, envolvendo:
* **Limpeza:** Padronização de nomes de lutadores entre as duas bases de dados.
* **Unificação:** Merge dos datasets de ranking e de detalhes dos lutadores.
* **Transformação:** Conversão de colunas de data (Ano, Mês, Dia) para o formato `datetime`.
* **Engenharia de Features:** Criação da coluna `Região` para agrupar lutadores por origem geográfica (ex: "Países Caucasianos", "Estados Unidos", "Brasil"), permitindo a análise central do projeto.

#### Passo 4: Análise Exploratória e Criação do Dashboard
Com os dados tratados, a análise focou em responder à pergunta inicial através de quatro visualizações principais, consolidadas em um dashboard interativo com Dash e Plotly.
1.  **Representatividade no Top 15:** A porcentagem de lutadores caucasianos no ranking geral.
2.  **Dominância no Top 5:** O número absoluto de lutadores caucasianos na elite do ranking.
3.  **Ranking Médio Comparativo:** A evolução da performance média entre os grupos.
4.  **Distribuição de Idade:** Uma análise do perfil demográfico no ranking mais recente.

## 5. Principais Insights
A análise revelou que a percepção de dominância é , de fato, uma tendência estatística. Embora a presença geral de lutadores caucasianos no Top 15 seja estável, sua ocupação no Top 5 e sua performance média melhoraram significativamente nos últimos anos.

## 6. Conclusão

A análise de dados realizada neste projeto permite concluir que a proeminência de lutadores caucasianos no topo do ranking P4P do UFC não é um acontecimento súbito. Pelo contrário, trata-se do clímax de uma tendência de performance sustentada, com indicadores claros de crescimento desde 2022, como a ocupação crescente de vagas no Top 5 e a melhora do ranking médio coletivo.

Os insights extraídos dos dados validam e contextualizam a narrativa atual do esporte. O debate, que frequentemente surge em discussões e artigos, encontra nos números uma base factual sólida.

> **Artigo de Referência:** A inspiração central para esta investigação veio da seguinte notícia, que articula a percepção do cenário atual do UFC:
>
> ### [**Islam Makhachev Reveals Real Reason For Non-American Dominance In UFC**](https://www.yardbarker.com/general_sports/articles/islam_makhachev_reveals_real_reason_for_non_american_dominanceinufc/s1_17325_42635261)








