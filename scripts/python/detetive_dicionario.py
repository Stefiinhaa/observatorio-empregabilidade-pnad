import pandas as pd

def detetive_excel():
    print("Lendo o Dicionário do Excel (.xls)...")
    caminho_dic = '../../data/raw/dicionario_pnad.xls'
    
    try:
        # Lemos o Excel ignorando as duas linhas de título do IBGE
        df = pd.read_excel(caminho_dic, skiprows=2)
        
        df.columns = ['posicao', 'tamanho', 'codigo', 'quesito', 'descricao', 'tipo', 'categorias']
        
        print("\nPERGUNTAS SOBRE QUALIFICAÇÃO ENCONTRADAS:")
        print("-" * 80)
        
        vistos = set()
        for idx, row in df.iterrows():
            desc = str(row['descricao']).lower()
            
            if ('frequentou' in desc or 'conclui' in desc or 'motivo' in desc) and 'qualifica' in desc:
                cod = str(row['codigo']).strip()

                if cod.startswith('V31') and cod not in vistos:
                    vistos.add(cod)
                    # Limpamos os números para não aparecerem com casas decimais (ex: 914.0 vira 914)
                    pos = str(row['posicao']).replace('.0', '')
                    tam = str(row['tamanho']).replace('.0', '')
                    texto = str(row['descricao']).strip()
                    
                    print(f"Código: {cod} | Posição: {pos} | Tamanho: {tam} | {texto[:60]}...")
                    
        print("-" * 80)
        
    except ImportError:
        print("Erro: Falta instalar a biblioteca 'xlrd'. Rode: pip install xlrd no terminal.")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado. Verifique se o nome está como 'dicionario_pnad.xls'.")
    except Exception as e:
        print("Erro inesperado:", e)

if __name__ == '__main__':
    detetive_excel()
