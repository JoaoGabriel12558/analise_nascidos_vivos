#importando bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Perguntas de pesquisa
#1º - O número de nascidos vivos nos municípios Brasileiros aumentou, diminuiu ou permanece estável entre 2014 e 2023?
#2º - Existe diferença na média de nascidos vivos entre as regiões do Brasil?
#3º - Quais 10 municípios tiveram as maiores e menores médias de nascidos vivos?
#4° - Evolução de nascidos vivos ao longo dos anos no estado do RJ.

#carregar o arquivo csv processado
df = pd.read_csv(
    "nascidos_vivos_2014a2023.csv",
    sep=',',
    encoding='utf-8'
)
#1-tendencia temporal

#seleciona apenas as colunas de nascidos por ano
anos = [f"nasc{ano}" for ano in range(2014, 2024)]

#calcula a soma de total nascidos vivos por ano
nascidos_por_ano = df[anos].sum()

print(nascidos_por_ano)

plt.figure(figsize=(14, 7))

plt.plot(
    nascidos_por_ano.index,
    nascidos_por_ano.values,
    marker='o',
)

plt.title("Total de Nascidos Vivos no Brasil por ano (2014–2023)", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Total de nascidos vivos", fontsize=12)

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig("graficos/total_nascidos_2014_2023.png")
plt.show()

#2-Diferença entre as médias das regiões
media_regioes = df.groupby('regiao')[anos].mean().mean(axis=1)
plt.figure(figsize=(10, 6))
media_regioes.sort_values().plot(kind='barh')
plt.title("Média de Nascidos Vivos por Região (2014–2023)")
plt.xlabel("Média de nascidos vivos")
plt.ylabel("Região")
plt.tight_layout()
plt.savefig("graficos/media_geral_regioes.png")
plt.show()


#3º - Quais 10 municípios tiveram as maiores e menores médias de nascidos vivos?

## média geral por município (2014–2023)
media_municipios = df.groupby('municipio')[anos].mean().mean(axis=1)

## top 10 maiores e menores
top_10_maiores = media_municipios.sort_values(ascending=False).head(10)
top_10_menores = media_municipios.sort_values().head(10)

## -------- gráfico: maiores médias --------
plt.figure(figsize=(10, 6))
plt.barh(top_10_maiores.sort_values().index,
         top_10_maiores.sort_values().values)

plt.title("Top 10 Municípios com Maiores Médias de Nascidos Vivos")
plt.xlabel("Média de nascidos vivos")
plt.ylabel("Município")

for i, v in enumerate(top_10_maiores.sort_values().values):
    plt.text(v, i, f"{int(v):,}".replace(',', '.'),
             va='center', ha='left')

plt.tight_layout()
plt.savefig("graficos/top10_maiores_municipios.png")
plt.show()


## -------- gráfico: menores médias --------
plt.figure(figsize=(10, 6))
plt.barh(top_10_menores.index,
         top_10_menores.values)

plt.title("Top 10 Municípios com Menores Médias de Nascidos Vivos")
plt.xlabel("Média de nascidos vivos")
plt.ylabel("Município")

for i, v in enumerate(top_10_menores.values):
    plt.text(v, i, f"{int(v):,}".replace(',', '.'),
             va='center', ha='left')

plt.tight_layout()
plt.savefig("graficos/top10_menores_municipios.png")
plt.show()


#4° - Evolução de nascidos vivos ao longo dos anos no estado do RJ.
df_rj = df[df['uf'] == 'RJ']
nascidos_rj_por_ano = df_rj[anos].sum()
plt.figure(figsize=(14, 7))
plt.plot(
    nascidos_rj_por_ano.index,
    nascidos_rj_por_ano.values,
    marker='o',
)   
plt.title("Total de Nascidos Vivos no Estado do RJ por ano (2014–2023)", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Total de nascidos vivos", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("graficos/total_nascidos_rj_2014_2023.png")
plt.show()
#fim do código
