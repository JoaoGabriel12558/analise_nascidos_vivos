import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# ler o arquivo csv
df = pd.read_csv(
    "tabela-apoio-brasil-nascidosvivos-5570municipios.csv",
    sep=';',
    encoding='utf-8'
)
# converter colunas numéricas
df['nasc2023'] = pd.to_numeric(df['nasc2023'], errors='coerce')

# excluir colunas desnecessárias (caso existam)
df = df.drop(columns=['ID'], errors='ignore')

# renomear colunas para facilitar o acesso
df = df.rename(columns={
    'codmun6num': 'codigo_municipio',
    'municipio-residencia-mae': 'municipio',
    'media14a23': 'media'
})

# remover números do início do nome dos municípios
df['municipio'] = df['municipio'].apply(
    lambda x: re.sub(r'^\d+\s*', '', str(x))
)

# mapear UF a partir do código do município
map_uf = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL",
    "28": "SE", "29": "BA", "31": "MG", "32": "ES", "33": "RJ", "35": "SP", "41": "PR",
    "42": "SC", "43": "RS", "50": "MS", "51": "MT", "52": "GO", "53": "DF"
}

df["uf"] = (
    df["codigo_municipio"]
    .astype(str)
    .str.zfill(6)
    .str[:2]
    .map(map_uf)
)

# mapear região a partir da UF
map_regiao = {
    "AC": "Norte", "AP": "Norte", "AM": "Norte", "PA": "Norte",
    "RO": "Norte", "RR": "Norte", "TO": "Norte",

    "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste",
    "PB": "Nordeste", "PE": "Nordeste", "PI": "Nordeste", "RN": "Nordeste",
    "SE": "Nordeste",

    "DF": "Centro-Oeste", "GO": "Centro-Oeste",
    "MT": "Centro-Oeste", "MS": "Centro-Oeste",

    "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",

    "PR": "Sul", "RS": "Sul", "SC": "Sul"
}

df["regiao"] = df["uf"].map(map_regiao)

# visualizar resultado
#print(df.head(50))

# salvar o dataframe processado em um novo arquivo CSV
df.to_csv("nascidos_vivos_2014a2023.csv", index=False, encoding='utf-8')