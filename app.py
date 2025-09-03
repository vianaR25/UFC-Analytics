import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def carregar_e_tratar_dados(caminho_rankings, caminho_lutadores):
    df_rankings = pd.read_csv(caminho_rankings)
    df_lutadores = pd.read_csv(caminho_lutadores)

    df_lutadores.rename(columns={'Nome do Lutador': 'fighter'}, inplace=True)
    df_merged = pd.merge(df_rankings, df_lutadores, on='fighter', how='left')

    mes_map = {
        'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
        'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
    }
    df_merged['Mês_num'] = df_merged['Mês_x'].str.lower().map(mes_map)
    df_merged['date'] = pd.to_datetime(
        df_merged['Ano_x'].astype(str) + '-' + 
        df_merged['Mês_num'].astype(str) + '-' + 
        df_merged['Dia_x'].astype(str), 
        errors='coerce'
    )

    df_merged.dropna(subset=['date', 'Região'], inplace=True)

    def assign_group(region):
        return 'Caucasiano' if region in ['Países Caucasianos', 'Estados Unidos'] else 'Não Caucasiano'
    
    df_merged['grupo_analise'] = df_merged['Região'].apply(assign_group)
    
    return df_merged

def criar_figuras(df):
    
    # Figura 1: Representatividade
    total_fighters = df.groupby('date')['fighter'].nunique()
    caucasian_fighters = df[df['grupo_analise'] == 'Caucasiano'].groupby('date')['fighter'].nunique()
    percentage_caucasian = (caucasian_fighters / total_fighters * 100).fillna(0)
    monthly_percentage = percentage_caucasian.resample('ME').mean()
    
    fig1 = px.line(
        monthly_percentage, x=monthly_percentage.index, y=monthly_percentage.values,
        title='Representatividade Caucasiana no P4P Top 15 (Média Mensal)',
        labels={'x': 'Ano', 'y': 'Porcentagem (%)'}, template='plotly_white'
    )
    fig1.update_layout(yaxis_range=[0, 100])

    # Figura 2: Dominância Top 5
    df_top5 = df[df['rank'] <= 5].copy()
    df_top5.set_index('date', inplace=True)
    caucasian_in_top5 = df_top5[df_top5['grupo_analise'] == 'Caucasiano'].groupby(level=0)['fighter'].nunique()
    monthly_caucasian_in_top5 = caucasian_in_top5.resample('ME').mean().fillna(0)
    
    fig2 = px.line(
        monthly_caucasian_in_top5, x=monthly_caucasian_in_top5.index, y=monthly_caucasian_in_top5.values,
        title='Dominância Caucasiana no P4P Top 5 (Média Mensal)',
        labels={'x': 'Ano', 'y': 'Número Médio de Lutadores (de 5)'}, template='plotly_white'
    )
    fig2.update_layout(yaxis=dict(tickmode='linear', tick0=0, dtick=1), yaxis_range=[0, 5])

    # Figura 3: Ranking Médio
    avg_rank_monthly = df.groupby(['date', 'grupo_analise'])['rank'].mean().unstack().resample('ME').mean()
    
    fig3 = px.line(
        avg_rank_monthly, x=avg_rank_monthly.index, y=['Caucasiano', 'Não Caucasiano'],
        title='Ranking Médio Mensal P4P: Caucasianos vs. Não Caucasianos',
        labels={'x': 'Ano', 'value': 'Ranking Médio'}, template='plotly_white'
    )
    fig3.update_yaxes(autorange="reversed")

    # Figura 4: Idade
    most_recent_date = df['date'].max()
    df_recent = df[df['date'] == most_recent_date]
    
    fig4 = px.box(
        df_recent, x='grupo_analise', y='Idade',
        title=f'Distribuição de Idade no P4P (em {most_recent_date.strftime("%d/%m/%Y")})',
        labels={'grupo_analise': 'Grupo de Análise', 'Idade': 'Idade'}, template='plotly_white'
    )
    
    return fig1, fig2, fig3, fig4

def criar_layout(fig1, fig2, fig3, fig4):
    return html.Div(children=[
        html.H1(
            children='Dashboard de Análise P4P - Evolução dos Lutadores Caucasianos',
            style={'textAlign': 'center', 'fontFamily': 'Arial'}
        ),
        html.Div(
            children='Uma análise visual da presença e performance de lutadores caucasianos no ranking Peso-por-Peso do UFC de 2020 a 2025.',
            style={'textAlign': 'center', 'fontFamily': 'Arial'}
        ),
        dcc.Graph(id='graph-representatividade', figure=fig1),
        dcc.Graph(id='graph-dominancia', figure=fig2),
        dcc.Graph(id='graph-ranking-medio', figure=fig3),
        dcc.Graph(id='graph-idade', figure=fig4)
    ])

if __name__ == '__main__':
    
    caminho_arquivo_rankings = 'Dados tratados rankings_history.csv'
    caminho_arquivo_lutadores = 'lutadores_dados tratados.csv'

    try:
        dados_tratados = carregar_e_tratar_dados(caminho_arquivo_rankings, caminho_arquivo_lutadores)
        figura1, figura2, figura3, figura4 = criar_figuras(dados_tratados)
        
        app = dash.Dash(__name__)
        app.layout = criar_layout(figura1, figura2, figura3, figura4)
        app.run(debug=True)
        
    except FileNotFoundError:
        print(f"Erro: Um dos arquivos não foi encontrado. Verifique os caminhos:\n- {caminho_arquivo_rankings}\n- {caminho_arquivo_lutadores}")