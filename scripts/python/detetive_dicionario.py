import pandas as pd

def investigar_dicionario():

    caminho_dicionario = '../../data/raw/dicionario_pnad.xls'
    
    print("A ler o dicionário do IBGE para encontrar as nossas variáveis...\n")

    try:
        # Lemos o ficheiro ignorando as duas primeiras linhas de cabeçalho confusas
        df = pd.read_csv(caminho_dicionario, skiprows=2, encoding='latin1', header=None, low_memory=False)

        # Renomeamos as colunas de acordo com a estrutura do ficheiro do IBGE
        df = df.rename(columns={
            0: 'posicao',
            1: 'tamanho',
            2: 'codigo',
            3: 'num_quesito',
            4: 'descricao'
        })

        # Removemos linhas vazias
        df = df.dropna(subset=['descricao', 'codigo'])

        # Procuramos pelas palavras-chave vitais para o nosso observatório
        palavras = 'qualificação|concluiu|motivo'
        filtro = df['descricao'].str.contains(palavras, case=False, na=False)
        
        # Filtramos para garantir que traz apenas os Códigos de Variável corretos (que começam com V)
        df_filtrado = df[filtro & df['codigo'].astype(str).str.startswith('V')]

        # Removemos possíveis duplicados
        resultados = df_filtrado[['codigo', 'posicao', 'tamanho', 'descricao']].drop_duplicates(subset=['codigo'])

        # Configuramos o Pandas para mostrar o texto completo no terminal
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)

        print("Variáveis encontradas no Dicionário:")
        print("-" * 80)
        print(resultados.head(25)) # Mostra os primeiros 25 resultados encontrados
        print("-" * 80)

    except FileNotFoundError:
        print(f"Erro: O ficheiro não foi encontrado. Verifica se o nome está como 'dicionario_pnad.csv' na pasta 'data/raw/'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    investigar_dicionario()