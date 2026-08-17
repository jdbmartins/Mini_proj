# Análise de Dados Base Varejo 📊

**Projeto Educacional** | Aprendizado em Python e Análise de Dados

---

## 📌 Descrição do Projeto

Este projeto é resultado de **6 semanas de aulas** sobre Python e Análise de Dados no SENAI. Através dele, estou desenvolvendo habilidades práticas de:

- ✅ Importação e exploração de dados com Pandas
- ✅ Limpeza e validação de dados
- ✅ Análise descritiva e estatística
- ✅ Exploração de padrões através de agrupamentos
- ✅ Geração de insights e conclusões

**Nota**: Este é um projeto em fase de aprendizado, portanto pode conter evoluções e melhorias contínuas.

---

## 📋 O Que Faz Este Projeto?

O script realiza uma **análise completa de dados de varejo**, passando por **6 etapas estruturadas**:

| Etapa | Descrição |
|-------|-----------|
| **1️⃣ Carregamento** | Importa dados do CSV e explora a estrutura básica |
| **2️⃣ Diagnóstico** | Identifica valores nulos, duplicatas e inconsistências |
| **3️⃣ Limpeza** | Remove duplicatas e padroniza tipos de dados |
| **4️⃣ Estatísticas** | Calcula média, mediana, quartis e distribuições |
| **5️⃣ Agrupamentos** | Explora padrões de compra por gênero e categoria |
| **6️⃣ Conclusões** | Gera insights e identifica próximos passos |

---

## 🚀 Como Usar

### Pré-requisitos

- **Python 3.8+** instalado
- **Pandas** e **NumPy** (bibliotecas de dados)

### Instalação de Dependências

```bash
pip install pandas numpy
```

### Executar o Projeto

1. **Clone ou baixe este repositório:**
   ```bash
   git clone https://github.com/jdbmartins/Mini_proj.git
   cd Mini_proj
   ```

2. **Certifique-se de que o arquivo `Base Varejo.csv` está na mesma pasta:**
   ```
   Mini_proj/
   ├── MIniProj_JoaoMartins.py
   ├── Base Varejo.csv          ← Necessário!
   └── README.md
   ```

3. **Execute o script:**
   ```bash
   python MIniProj_JoaoMartins.py
   ```

4. **Visualize os resultados** diretamente no terminal!

---

## 📊 Saída Esperada

O script exibe um relatório completo com:

### Exemplo de Output:
```
================================================================================
ETAPA 1: CARREGAMENTO E EXPLORAÇÃO INICIAL DOS DADOS
================================================================================

>> Primeiras 10 linhas da base:
[DataFrame com dados do CSV]

>> Dimensões da base (linhas, colunas):
   Total: 830,000 linhas × 10 colunas

================================================================================
ETAPA 2: DIAGNÓSTICO - PROBLEMAS BÁSICOS ENCONTRADOS
================================================================================

1. VALORES NULOS POR COLUNA: ✓ Nenhum encontrado
2. LINHAS DUPLICADAS: 96,553 duplicatas encontradas (11.63%)
3. INCONSISTÊNCIAS DE DATAS: ✓ Todas válidas

[... e assim por diante nas 6 etapas ...]
```

---

## 📈 Estrutura do Código

### Etapa 1: Carregamento e Exploração
```python
# Carrega o CSV com separador ";"
df = pd.read_csv(caminho_csv, sep=';')

# Remove colunas vazias (Unnamed)
# Exibe primeiras linhas, dimensões e tipos de dados
```

**O que você aprende:** Como importar dados, explorar estrutura e lidar com formatação de CSV.

---

### Etapa 2: Diagnóstico
```python
# Verifica valores nulos
valores_nulos = df.isnull().sum()

# Identifica linhas duplicadas
duplicadas_totais = df.duplicated().sum()

# Valida datas
df_test = pd.to_datetime(df["DATA"], format='%d/%m/%Y', errors='coerce')
```

**O que você aprende:** Como identificar problemas de qualidade nos dados.

---

### Etapa 3: Limpeza
```python
# 1. Imputação de nulos: categorias → "Sem informação", numéricos → média
# 2. Remoção de duplicatas
df = df.drop_duplicates()

# 3. Conversão de tipos
df["DATA"] = pd.to_datetime(df["DATA"], format='%d/%m/%Y', errors='coerce')
```

**O que você aprende:** Estratégias de limpeza e padronização de dados.

---

### Etapa 4: Estatísticas Descritivas
```python
# Calcula estatísticas para coluna CL_FHL (número de filhos)
coluna_stats = df["CL_FHL"].dropna()

print(f"Média: {coluna_stats.mean():.4f}")
print(f"Mediana: {coluna_stats.median():.4f}")
print(f"Desvio Padrão: {coluna_stats.std():.4f}")
print(f"Moda: {coluna_stats.mode().values[0]}")
```

**O que você aprende:** Cálculo e interpretação de estatísticas descritivas.

---

### Etapa 5: Agrupamentos
```python
# Agrupa por gênero
vendas_por_genero = df.groupby("CL_GENERO").size()

# Agrupa por categoria
vendas_por_categoria = df.groupby("PR_CAT").size()

# Cruzamento de duas dimensões
tabela_cruzada = pd.crosstab(df["CL_GENERO"], df["PR_CAT"])
```

**O que você aprende:** Como usar `groupby()` e `crosstab()` para análise exploratória.

---

### Etapa 6: Conclusões
```python
# Gera insight sobre qualidade, volume, padrões e distribuição temporal
# Identifica problemas remanescentes
# Sugere próximos passos de análise
```

**O que você aprende:** Como transformar dados em insights acionáveis.

---

## 📁 Arquivo de Dados

### Base Varejo.csv

Contém transações de varejo com as seguintes colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `DATA` | String | Data da transação (formato DD/MM/YYYY) |
| `CO_ID` | Integer | ID da loja/comércio |
| `CL_ID` | Integer | ID do cliente |
| `CL_GENERO` | String | Gênero do cliente (M/F) |
| `CL_EC` | Integer | Classe econômica |
| `CL_FHL` | Integer | Número de filhos |
| `CL_SEG` | String | Segmento do cliente |
| `PR_ID` | Integer | ID do produto |
| `PR_CAT` | String | Categoria do produto |
| `PR_NOME` | String | Nome do produto |

**Estatísticas da Base:**
- 🔢 **830.000 linhas** (antes da limpeza)
- 📊 **733.447 linhas** (após remoção de duplicatas)
- 📅 **Período:** Janeiro 2019 a Dezembro 2022
- 👥 **Clientes únicos:** 1.000
- 🛍️ **Produtos únicos:** 229

---

## 🎯 Principais Descobertas

Com base na execução do script, alcancei:

### 1. Qualidade dos Dados
✅ **100% de qualidade** após limpeza (sem valores nulos)

### 2. Padrões de Compra
- 👩 **Mulheres (F)**: 52,1% das transações
- 👨 **Homens (M)**: 47,9% das transações
- 🥇 **Categoria top**: ALIMENTOS (384.197 transações)

### 3. Perfil do Cliente
- 📊 **Média de filhos**: 1,15
- 📈 **Mediana**: 0 filhos
- 📉 **Máximo**: 4 filhos

### 4. Distribuição Temporal
- 📅 Dados cobrem período de **4 de janeiro de 2019 a 8 de dezembro de 2022** (~4 anos)

---

## 🔧 Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Pandas** - Manipulação e análise de dados
- **NumPy** - Operações numéricas
- **Git** - Controle de versão

---

## 📚 Conceitos Aprendidos

Durante o desenvolvimento deste projeto, aprendi:

- ✅ Importação de dados com Pandas (`read_csv`)
- ✅ Exploração inicial (`head()`, `info()`, `describe()`)
- ✅ Limpeza de dados (`fillna()`, `drop_duplicates()`)
- ✅ Conversão de tipos de dados (`pd.to_datetime()`)
- ✅ Tratamento de erros (`errors='coerce'`)
- ✅ Análise estatística descritiva (média, mediana, quartis, etc.)
- ✅ Agrupamento de dados (`groupby()`, `crosstab()`)
- ✅ Filtros e seleções de dados
- ✅ Formatação de output com cores ANSI
- ✅ Versionamento com Git

---

## 🚧 Melhorias Futuras

Nas próximas semanas/fases, pretendo:

- [ ] Adicionar visualizações gráficas (Matplotlib/Seaborn)
- [ ] Realizar análise de RFM (Recência, Frequência, Monetário)
- [ ] Implementar segmentação de clientes com clustering
- [ ] Criar previsões de demanda
- [ ] Exportar relatórios para Excel/PDF
- [ ] Otimizar performance com dados maiores
- [ ] Adicionar testes unitários

---

## 📞 Contato e Créditos

- **Aluno:** João Martins
- **Instituição:** SENAI (Cursos de Python e Análise de Dados)
- **Período:** 6 semanas de aulas práticas
- **Repositório:** [GitHub - Mini_proj](https://github.com/jdbmartins/Mini_proj)

---

## 📄 Licença

Este projeto é fornecido para fins educacionais. Sinta-se livre para usar, modificar e distribuir conforme necessário para aprendizado.

---

## 💡 Dicas de Aprendizado

1. **Explore o código:** Cada seção tem comentários explicativos em primeira pessoa
2. **Modifique os dados:** Experimente filtrar, agrupar por outras colunas
3. **Tente melhorias:** Adicione mais validações ou cálculos
4. **Documente:** Anote o que você aprendeu em cada etapa
5. **Compartilhe:** Discuta os insights com colegas e mentores

---

**Desenvolvido com ❤️ durante fase de aprendizado em Python e Análise de Dados**

*Última atualização: Agosto de 2026*
