import pandas as pd
import os

def processar_dados():
    input_file = '../../data/raw/pnad_2014_raw.txt'
    output_file = '../../data/processed/pnad_tratada.csv'

    print("Iniciando a Extração dos Microdados...")

    try:
        cortes = [
            (0, 4), (4, 6), (17, 18), (26, 29), (32, 33), (702, 714),
            (946, 947), (954, 955), (955, 957)
        ]
        nomes = ['ano', 'uf', 'sexo', 'idade', 'cor_raca', 'renda_mensal', 'frequentou_curso', 'concluiu_curso', 'motivo_evasao']

        df = pd.read_fwf(input_file, colspecs=cortes, names=nomes, encoding='latin1')
        
      
        for col in ['frequentou_curso', 'concluiu_curso', 'motivo_evasao', 'sexo', 'cor_raca']:
            df[col] = pd.to_numeric(df[col], errors='coerce')

     
        df['sexo'] = df['sexo'].replace({2: 'Masculino', 4: 'Feminino'})
        df['cor_raca'] = df['cor_raca'].replace({2: 'Branca', 4: 'Preta', 6: 'Amarela', 8: 'Parda', 0: 'Indígena'})

        df['frequentou_curso'] = df['frequentou_curso'].replace({1: 'Sim', 2: 'Sim', 3: 'Não', 4: 'Não'})
        df['concluiu_curso'] = df['concluiu_curso'].replace({1: 'Sim', 2: 'Não', 3: 'Não', 4: 'Não'})

        motivos = {
            1: 'Dificuldade Financeira',
            2: 'Dificuldade de acesso ao local',
            3: 'Dificuldade de cumprir o horário',
            4: 'Falta de tempo para estudar',
            5: 'Falta de motivação / Curso não era o esperado',
            6: 'Conseguiu emprego em outra área',
            7: 'Problema de saúde ou gravidez',
            8: 'Outro'
        }
        df['motivo_evasao'] = df['motivo_evasao'].replace(motivos)


        df_filtrado = df[df['frequentou_curso'] == 'Sim'].copy()

        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df_filtrado.to_csv(output_file, index=False, encoding='utf-8')

        print(f"SUCESSO! CSV gerado com: {df_filtrado.shape[0]} linhas.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    processar_dados()
