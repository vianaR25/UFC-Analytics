import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re
from tqdm import tqdm

def generate_ufc_url(fighter_name):
    """Gera a URL de um lutador a partir do seu nome."""
    name_cleaned = re.sub(r'\s*".*?"\s*', ' ', fighter_name)
    slug = name_cleaned.strip().lower().replace(' ', '-')
    return f"https://www.ufc.com.br/athlete/{slug}"

def scrape_fighter_details(fighter_url, session):
    """
    Visita a página de um lutador e extrai todos os detalhes, incluindo a URL da foto.
    """
    try:
        response = session.get(fighter_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        full_name_tag = soup.find('h1', {'class': 'hero-profile__name'})
        full_name = full_name_tag.get_text(strip=True) if full_name_tag else 'Nome não encontrado'

        details = {
            'Nome do Lutador': full_name,
            'URL da Foto': 'Não encontrada',
            'País': 'Não encontrado',
            'Idade': 'Não encontrado',
            'Altura': 'Não encontrado',
            'Peso': 'Não encontrado',
            'Estreia no UFC': 'Não encontrado'
        }

        
        image_tag = soup.find('img', class_='hero-profile__image')
        if image_tag and image_tag.has_attr('src'):
            details['URL da Foto'] = image_tag['src']

        # Lógica para extrair os outros dados da biografia
        all_labels = soup.find_all('div', class_='c-bio__label')
        
        for label in all_labels:
            label_text = label.get_text(strip=True).lower()
            value_div = label.find_next_sibling('div', class_='c-bio__text')
            
            if value_div:
                value_text = value_div.get_text(strip=True)

                if label_text == 'cidade natal':
                    details['País'] = value_text.split(',')[-1].strip()
                elif label_text == 'idade':
                    details['Idade'] = value_text
                elif label_text == 'altura':
                    details['Altura'] = value_text
                elif label_text == 'peso':
                    details['Peso'] = value_text
                elif label_text == 'estreia no ufc':
                    details['Estreia no UFC'] = value_text
        
        return details

    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException as e:
        print(f"  -> Erro de conexão ao acessar {fighter_url}: {e}")
        return None

def main():
    """
    Função principal que lê o XLSX, cria uma sessão e extrai os dados.
    """
    input_filename = 'rankings_history.xlsx'
    output_filename = 'lutadores_dados_completos.csv' 
    ATHLETES_PAGE_URL = "https://www.ufc.com.br/athletes/all"

    try:
        df = pd.read_excel(input_filename)
    except FileNotFoundError:
        print(f"ERRO: Arquivo '{input_filename}' não encontrado.")
        return
    except Exception as e:
        print(f"ERRO: Não foi possível ler o arquivo Excel. Detalhes: {e}")
        return

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    })
    
    print("Iniciando sessão e obtendo cookies...")
    try:
        session.get(ATHLETES_PAGE_URL)
        print("Sessão iniciada com sucesso.")
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível iniciar a sessão: {e}")
        return

    fighter_column = 'fighter' 
    if fighter_column not in df.columns:
        print(f"ERRO: A coluna '{fighter_column}' não foi encontrada. As colunas disponíveis são: {list(df.columns)}")
        return

    unique_fighters = df[fighter_column].dropna().unique()
    
    print(f"\nEncontrados {len(unique_fighters)} lutadores únicos para pesquisar.")
    
    scraped_data = []

    for fighter_name in tqdm(unique_fighters, desc="Raspando dados dos lutadores"):
        fighter_name_str = str(fighter_name)
        fighter_url = generate_ufc_url(fighter_name_str)
        details = scrape_fighter_details(fighter_url, session)
        
        if details:
            scraped_data.append(details)
        
        time.sleep(0.5)

    if not scraped_data:
        print("Nenhum dado foi extraído.")
        return
        
    results_df = pd.DataFrame(scraped_data)
    results_df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*50)
    print("Processo concluído com sucesso!")
    print(f"Os dados foram salvos no arquivo: {output_filename}")
    print("="*50)
    print("\nAmostra dos dados extraídos:")
    print(results_df.head())


if __name__ == '__main__':
    main()