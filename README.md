# Análise nascidos vivos 2014 - 2023 no Brasil.  

Esse projeto tem como finalidade análisar uma base de dados sobre o número de nascidos vivos nos municípios Brasileiros entre 2014 e 2023.  

## Perguntas de pesquisa  
Para a Análise, foram elaboradas 5 perguntas sobre  contexto de nascidos vivos:  

### 1º - O número de nascidos vivos nos municípios Brasileiros aumentou, diminuiu ou permanece estável entre 2014 e 2023?  
>**Tendência ao longo do tempo**  
>Tendência temporal.  

### 2º - Existe diferença na média de nascidos vivos entre as regiões do Brasil?  
>**Diferença entre as regiões**  
>Comparação regional.

### 3º - Houve queda no número de nascidos vivos em 2020 e 2021?  
>**impacto da pandemia do Covid-19**  
>Evento externo (pandemia).

### 4º - Quais 10 municípios tiveram as maiores e menores médias de nascidos vivos?  
>**Mnicípios com maiores e menores valores**  
>Os extremos de distribuição

### 5° - Evolução de nascidos vivos ao longo dos anos no estado do RJ.  
>**Evolução de um estad específico.**  
>Estudo de caso.


## Base de dados
Os dados brutos estão armazenados em um arquivo csv, [clique aqui](https://drive.google.com/file/d/1D45N22DZhASAqiqugFuvwFYqprUMYLkS/view?usp=drive_link) para acessar o arquivo, disponível também nesse repostóro.  

## Limpeza do arquivo csv com python  

**Bibliotecas**  
>pandas: leitura, tratamento, padronização e criação de variáveis
>re: limpeza e padronização de textos

```python
import pandas as pd
import re
