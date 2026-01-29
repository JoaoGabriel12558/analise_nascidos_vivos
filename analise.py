#importando bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Perguntas de pesquisa
#1º - O número de nascidos vivos nos municípios Brasileiros aumentou, diminuiu ou permanece estável entre 2014 e 2023?
#2º - Existe diferença na média de nascidos vivos entre as regiões do Brasil?
#3º - Houve queda no número de nascidos vivos em 2020 e 2021?
#4º - Quais 10 municípios tiveram as maiores e menores médias de nascidos vivos?
#5° - Evolução de nascidos vivos ao longo dos anos no estado do RJ.

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
    marker='o'
)

plt.title("Tendência de Nascidos Vivos no Brasil (2014–2023)", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Total de nascidos vivos", fontsize=12)

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig("graficos/tendencia_nascidos_2014_2023.png")
plt.show()
