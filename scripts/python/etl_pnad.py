import pandas as pd
import os

def processar_dados():
    input_file = '../../data/raw/pnad_2014_educacao_profissional_cv.xls'
    output_file = '../../data/processed/pnad_tratada.csv'

    print("🚀 Iniciando o processamento dos dados da PNAD 2014...")

    try:
        # skiprows=4 pula as 4 primeiras linhas de título
        # on_bad_lines='skip' ignora qualquer linha solta que esteja bagunçada
        df = pd.read_csv(input_file, sep=',', encoding='latin1', skiprows=4, on_bad_lines='skip')
        
        print(f"✅ Base carregada com sucesso! Total de linhas: {df.shape[0]}")
        print(f"👀 Espiando os nomes das primeiras colunas encontradas:")
        print(df.columns.tolist()[:10])

    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    processar_dados()