import pandas as pd

# Caminho do arquivo CSV
arquivo = "mesario/convocacao_mesarios_2022/convocacao_mesarios_2022_DF.csv"

# Carrega o arquivo CSV especificando o delimitador correto (no caso, ;)
df = pd.read_csv(arquivo, delimiter=';', encoding='latin1')

# Verifica as colunas corretamente separadas
print("Colunas disponíveis no arquivo CSV:")
print(df.columns)

# Pega a coluna 'DS_FAIXA_ETARIA' e remove duplicatas
if 'DS_FAIXA_ETARIA' in df.columns:
    faixa_etaria = df['DS_FAIXA_ETARIA'].drop_duplicates()

    # Percorre e imprime os valores únicos de faixa etária
    for faixa in faixa_etaria:
        print(faixa)
else:
    print("A coluna 'DS_FAIXA_ETARIA' não foi encontrada no arquivo CSV.")
