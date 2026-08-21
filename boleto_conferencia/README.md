# Processamento de Grandes Volumes TXT para Excel

Automação desenvolvida em Python para extrair, tratar e organizar grandes volumes de registros armazenados em arquivos TXT semiestruturados.

O script percorre o arquivo linha por linha, identifica apenas os registros relevantes, aplica regras de validação e gera automaticamente uma planilha Excel organizada por data e pronta para análise.

## Objetivo

Substituir um processo manual de leitura, filtragem e montagem de planilhas por um fluxo automatizado, capaz de processar milhares de registros com padronização, velocidade e menor risco de erro humano.

## Funcionalidades

* Leitura eficiente do arquivo TXT linha por linha;
* Identificação automática das datas de processamento;
* Extração de dados por expressões regulares;
* Validação da estrutura de cada registro;
* Remoção de registros fora das regras definidas;
* Conversão de valores monetários para formato numérico;
* Agrupamento automático dos dados por data;
* Criação de uma aba do Excel para cada período identificado;
* Formatação das colunas monetárias;
* Aplicação automática de filtros;
* Congelamento do cabeçalho;
* Ajuste da largura das colunas;
* Exibição de um resumo do processamento no terminal.

## Fluxo do processamento

```text
Arquivo TXT
    ↓
Leitura linha por linha
    ↓
Identificação da data
    ↓
Extração dos registros
    ↓
Validação e filtragem
    ↓
Tratamento dos campos
    ↓
Agrupamento por data
    ↓
Geração do Excel
```

## Dados extraídos

Para cada registro válido, o programa identifica e organiza os seguintes campos:

| Campo   | Descrição                                       |
| ------- | ----------------------------------------------- |
| Agência | Código da agência                               |
| Conta   | Número da conta                                 |
| Nome    | Nome associado ao registro                      |
| Crédito | Valor de crédito convertido para número         |
| Débito  | Valor de débito convertido para número          |
| Flag    | Indicador presente no arquivo                   |
| Tipo    | Classificação utilizada nas regras de filtragem |
| SMS     | Informação adicional do registro                |

## Regras de tratamento

Durante o processamento, o script:

1. Ignora linhas anteriores à primeira data identificada;
2. Descarta linhas que não correspondem ao padrão esperado;
3. Remove automaticamente registros classificados como `DD`;
4. Limpa espaços desnecessários nos campos de texto;
5. Converte valores no padrão brasileiro para números;
6. Agrupa os registros conforme a data encontrada no arquivo;
7. Ignora grupos que não possuam registros válidos.

Essa abordagem permite processar arquivos extensos sem depender da manipulação manual de cada linha.

## Tecnologias utilizadas

* Python
* pandas
* openpyxl
* Expressões regulares — Regex
* pathlib
* collections

## Estrutura do projeto

```text
projeto/
├── processador.py
├── retorno_arquivo.TXT
├── requirements.txt
└── README.md
```

Após a execução, será criado o arquivo:

```text
retorno_arquivo.xlsx
```

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente

No Windows:

```bash
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install pandas openpyxl
```

### 5. Adicione o arquivo de entrada

Coloque o arquivo `retorno_arquivo.TXT` na mesma pasta do script.

Se o arquivo possuir outro nome, altere esta variável:

```python
ARQUIVO = "retorno_arquivo.TXT"
```

### 6. Execute o programa

```bash
python processador.py
```

## Resultado

O programa gera uma planilha Excel contendo:

* Uma aba para cada data encontrada;
* Registros organizados em colunas;
* Valores monetários formatados;
* Cabeçalhos destacados;
* Filtros automáticos;
* Primeira linha congelada;
* Colunas ajustadas conforme o conteúdo.

Ao final, o terminal apresenta a quantidade de registros processados em cada data, o total geral e o caminho completo do arquivo gerado.

Exemplo:

```text
============================================================
13/05/2022: 8.420 registros
24/09/2024: 9.135 registros
07/07/2029: 7.890 registros
------------------------------------------------------------
TOTAL: 25.445 registros
Arquivo salvo em:
caminho/retorno_arquivo.xlsx
============================================================
```

> Os valores acima são apenas ilustrativos.

## Diferenciais técnicos

O processamento é realizado linha por linha, evitando a necessidade de carregar todo o conteúdo bruto simultaneamente para análise.

As expressões regulares permitem reconhecer somente registros compatíveis com o layout esperado, enquanto as regras de negócio eliminam informações desnecessárias antes da criação da planilha.

O resultado é um fluxo reutilizável para tratamento de arquivos operacionais extensos, reduzindo tarefas repetitivas e entregando dados estruturados para conferência ou análise.

## Observação

Os dados e nomes apresentados neste repositório são fictícios ou anonimizados. Nenhuma informação confidencial, interna ou pertencente a terceiros está incluída no projeto.
