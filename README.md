# Análise de Nascidos Vivos no Brasil (2014–2023)

Este projeto tem como finalidade analisar uma base de dados sobre o número de nascidos vivos nos municípios brasileiros entre os anos de 2014 e 2023.

A análise busca identificar tendências temporais, diferenças regionais e possíveis impactos de eventos externos, como a pandemia de COVID-19, utilizando técnicas básicas de análise de dados com Python.

---

## Perguntas de pesquisa

Para a análise, foram elaboradas quatro perguntas relacionadas ao contexto de nascidos vivos no Brasil:  

### 1º – O número de nascidos vivos nos municípios brasileiros aumentou, diminuiu ou permaneceu estável entre 2014 e 2023?  
> **Tendência ao longo do tempo**    
> Análise da evolução temporal dos nascimentos no período estudado.  

### 2º – Existe diferença na média de nascidos vivos entre as regiões do Brasil?  
> **Diferença entre as regiões**  
> Comparação regional das médias de nascimentos.  

### 3º – Quais são os 10 municípios com as maiores e as menores médias de nascidos vivos?  
> **Municípios com maiores e menores valores**    
> Análise dos extremos da distribuição.  

### 4º – Como evoluiu o número de nascidos vivos ao longo dos anos no estado do Rio de Janeiro?  
> **Evolução em um estado específico**    
> Estudo de caso.  

---  

## Base de dados

Os dados brutos estão armazenados em um arquivo CSV.  
[ Clique aqui para acessar a base de dados ](https://drive.google.com/file/d/1D45N22DZhASAqiqugFuvwFYqprUMYLkS/view?usp=drive_link)

O arquivo também está disponível neste repositório.

---

## Limpeza e preparação dos dados com Python

### Bibliotecas utilizadas

>- **pandas**: leitura do arquivo CSV, tratamento dos dados, padronização e criação de novas variáveis  
>- **re**: limpeza e padronização de textos utilizando expressões regulares  

```python
import pandas as pd
import re
```

---

### Leitura do arquivo CSV

```python
df = pd.read_csv(
    "tabela-apoio-brasil-nascidosvivos-5570municipios.csv",
    sep=";",
    encoding="utf-8"
)
```

>O arquivo CSV é carregado e armazenado em um DataFrame para facilitar a manipulação dos dados.

---

### Conversão de colunas numéricas

```python
df["nasc2023"] = pd.to_numeric(df["nasc2023"], errors="coerce")
```

>A coluna `nasc2023` estava no formato texto devido à presença de caracteres inválidos.  
>A conversão para formato numérico força valores inválidos a se tornarem `NaN`.

---

### Exclusão de colunas desnecessárias

```python
df = df.drop(columns=["ID"], errors="ignore")
```

>A coluna `ID` é removida, pois não é relevante para as análises propostas.

---

### Renomeação de colunas

```python
df = df.rename(columns={
    "codmun6num": "codigo_municipio",
    "municipio-residencia-mae": "municipio",
    "media14a23": "media"
})
```

>Algumas colunas possuíam nomes pouco intuitivos. A renomeação facilita a análise.

---

### Remoção de números no início do nome dos municípios

```python
df["municipio"] = df["municipio"].apply(
    lambda x: re.sub(r"^\d+\s*", "", str(x))
)
```

>Os nomes dos municípios continham o código do município concatenado ao texto.

---

### Mapeamento da UF a partir do código do município

```python
map_uf = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL",
    "28": "SE", "29": "BA", "31": "MG", "32": "ES", "33": "RJ", "35": "SP", "41": "PR",
    "42": "SC", "43": "RS", "50": "MS", "51": "MT", "52": "GO", "53": "DF"
}
```

>Aqui é criada a variável `map_uf`, responsável por mapear os códigos de UF do IBGE.

```python
df["uf"] = (
    df["codigo_municipio"]
    .astype(str)
    .str.zfill(6)
    .str[:2]
    .map(map_uf)
)
```

>A coluna `uf` é criada a partir do código do município.

---

### Mapeamento da região a partir da UF

```python
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
```

```python
df["regiao"] = df["uf"].map(map_regiao)
```

>A coluna `regiao` é criada a partir da UF.

---

### Salvamento do arquivo tratado

```python
df.to_csv(
    "nascidos_vivos_2014a2023.csv",
    index=False,
    encoding="utf-8"
)
```

>O arquivo final é salvo com os dados prontos para análise em csv.

<br>  

## Análise do arquivo csv tratado.



