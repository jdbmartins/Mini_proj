# ANÁLISE DE DADOS - BASE VAREJO
# Estou aprendendo a fazer limpeza, exploração e análise de dados com Python e Pandas
# Vou seguir uma metodologia estruturada em 6 etapas

from pathlib import Path
import pandas as pd
import numpy as np

# Configurar opções de exibição para melhor visualização
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# ============================================================================
# ETAPA 1: CARREGAR A BASE E MOSTRAR INFORMAÇÕES BÁSICAS
# ============================================================================
print("\n" + "="*80)

# Descobri que já existe uma forma de colorir o texto no terminal usando códigos ANSI, então vou usar isso para destacar as etapas
print("\033[1;31mETAPA 1: CARREGAMENTO E EXPLORAÇÃO INICIAL DOS DADOS\033[0m")

print("="*80)

# Baixei do Kaggle e salvei o arquivo CSV no mesmo diretório do script
caminho_atual = Path(__file__).parent
caminho_csv = caminho_atual / "Base Varejo.csv"

# Carregando o arquivo CSV (descobri isso depois, no começo não entendia por que não separava as colunas, pois o separador é ";")
# df vem de DataFrame, que é a estrutura de dados principal do Pandas
# Read é literalmente "ler" e CSV é o formato do arquivo
df = pd.read_csv(caminho_csv, sep=';')

# Removo as colunas "Unnamed" (vazias) que sobraram no carregamento, pois, pelo o que entendi, esse dado não era relevante
colunas_unnamed = [col for col in df.columns if 'Unnamed' in col]

# Len vem de "length" (comprimento) e retorna o tamanho da lista
if len(colunas_unnamed) > 0:
    df = df.drop(columns=colunas_unnamed)

print("\n\033[33m>> Primeiras 10 linhas da base:\033[0m")

# Head é literalmente "cabeça" e mostra as primeiras linhas do DataFrame
print(df.head(10))

print("\n\033[33m>> Dimensões da base (linhas, colunas):\033[0m")
print(f"   Total: {df.shape[0]:,} linhas × {df.shape[1]} colunas")

print("\n\033[33m>> Tipos de dados e informações das colunas:\033[0m")
df.info()

print("\n\033[33m>> Nomes das colunas:\033[0m")
print(list(df.columns))

# ============================================================================
# ETAPA 2: VERIFICAR E REPORTAR PROBLEMAS BÁSICOS
# ============================================================================
print("\n" + "="*80)
print("\033[1;31mETAPA 2: DIAGNÓSTICO - PROBLEMAS BÁSICOS ENCONTRADOS\033[0m")
print("="*80)

# Problema 1: Valores nulos por coluna
print("\n\033[33m1. VALORES NULOS POR COLUNA:\033[0m")

# isnull vem de "is null" e retorna True para valores nulos, sum soma os True (que são tratados como 1)
valores_nulos = df.isnull().sum()
colunas_com_nulos = valores_nulos[valores_nulos > 0]

if len(colunas_com_nulos) == 0:
    print("Nenhum valor nulo encontrado.")
else:
    print(f"Encontradas {len(colunas_com_nulos)} coluna(s) com valores nulos:")
    for coluna, count in colunas_com_nulos.items():
        percentual = (count / len(df)) * 100
        print(f"-{coluna}: {count} nulos ({percentual:.2f}%)")

# Problema 2: Linhas duplicadas
print("\n\033[33m2. LINHAS DUPLICADAS:\033[0m")

# Duplicated é autoexplicativo, retorna True para linhas duplicadas, sum soma os True
duplicadas_totais = df.duplicated().sum()
print(f"   Total de linhas completamente duplicadas: {duplicadas_totais}")

if duplicadas_totais > 0:
    percentual_dup = (duplicadas_totais / len(df)) * 100
    print(f"   Isso representa {percentual_dup:.2f}% dos dados")
    print("\n   Exemplos de duplicatas encontradas:")
    exemplos = df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head(3)
    print(exemplos)
else:
    print("Nenhuma linha duplicada.")

# Problema 3: Inconsistências de datas (coluna DATA)
print("\n\033[33m3. INCONSISTÊNCIAS DE DATAS:\033[0m")
if "DATA" in df.columns:
    # Tento converter para datetime para validar, conforme solicitado no AVA
    df_test = pd.to_datetime(df["DATA"], format='%d/%m/%Y', errors='coerce')
    datas_invalidas = df_test.isnull().sum()
    
    if datas_invalidas > 0:
        print(f"Encontradas {datas_invalidas} datas inválidas")
        print("   Exemplos:")
        invalidas = df[df_test.isnull()]["DATA"].unique()[:5]
        for data in invalidas:
            print(f"     • {data}")
    else:
        print("Todas as datas estão no formato DD/MM/YYYY válido!")
else:
    print("   (Coluna DATA não encontrada nesta base)")

# ============================================================================
# ETAPA 3: LIMPEZA DE DADOS - TRÊS OPERAÇÕES MÍNIMAS
# ============================================================================
print("\n" + "="*80)
print("\033[1;31mETAPA 3: LIMPEZA DE DADOS\033[0m")
print("="*80)

print(f"\nDados ANTES da limpeza: {len(df):,} linhas")

# Operação 1: Remover ou preencher valores nulos
print("\n\033[33m1. TRATAMENTO DE VALORES NULOS:\033[0m")

if len(colunas_com_nulos) > 0:
    for coluna in colunas_com_nulos.index:
        # Se for coluna categórica (object), vai "Sem informação"
        if df[coluna].dtype == 'object':
            df[coluna] = df[coluna].fillna("Sem informação")
            print(f"   • {coluna}: Preenchido com 'Sem informação' (estratégia: valor padrão para categorias)")
        # Se for numérica, vai a média
        else:
            media = df[coluna].mean()
            # fillna vem de "fill NA", que do inglês significa "preencher valores nulos"
            df[coluna] = df[coluna].fillna(media)
            print(f"   • {coluna}: Preenchido com a média ({media:.2f}) (estratégia: manutenção de tendências)")
else:
    print("   (Nenhum valor nulo para tratar)")

# Operação 2: Eliminar duplicatas
print("\n\033[33m2. REMOÇÃO DE LINHAS DUPLICADAS:\033[0m")
linhas_antes = len(df)
df = df.drop_duplicates()
linhas_removidas = linhas_antes - len(df)

print(f"Linhas removidas: {linhas_removidas}")
print(f"Dados agora com {len(df):,} linhas (redução de {(linhas_removidas/linhas_antes)*100:.2f}%)")

# Operação 3: Ajustar tipos de dados (converter DATA para datetime)
print("\n\033[33m3. CONVERSÃO DE TIPOS DE DADOS:\033[0m")
if "DATA" in df.columns:
    df["DATA"] = pd.to_datetime(df["DATA"], format='%d/%m/%Y', errors='coerce')
    print(f"DATA: Convertida para datetime")

# Imprimo um resumo após limpeza
print(f"\nDados DEPOIS da limpeza: {len(df):,} linhas ✓")

# ============================================================================
# ETAPA 4: ESTATÍSTICAS DESCRITIVAS - COLUNA DE NÚMERO DE FILHOS
# ============================================================================
print("\n" + "="*80)
print("\033[1;31mETAPA 4: ESTATÍSTICAS DESCRITIVAS DA COLUNA DE CLIENTES\033[0m")
print("="*80)

# Detectar coluna que poderia ser "número de filhos" (procuro por colunas numéricas razoáveis)
# Se houver CL_FHL (Cliente Filhos), uso essa
coluna_filhos = None
if "CL_FHL" in df.columns:
    coluna_filhos = "CL_FHL"
else:
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    for col in colunas_numericas:
        if 'FHL' in col or 'filh' in col.lower() or 'depend' in col.lower():
            coluna_filhos = col
            break

if coluna_filhos:
    print(f"\n\033[33mAnalisando a coluna: {coluna_filhos}\033[0m")
    coluna_stats = df[coluna_filhos].dropna()
    
    print(f"\n   Contagem (quantidade de registros): {coluna_stats.count()}")
    print(f"   Média: {coluna_stats.mean():.4f}")
    print(f"   Mediana: {coluna_stats.median():.4f}")
    print(f"   Desvio Padrão: {coluna_stats.std():.4f}")
    print(f"   Moda: {coluna_stats.mode().values[0] if len(coluna_stats.mode()) > 0 else 'N/A'}")
    print(f"   Mínimo: {coluna_stats.min():.4f}")
    print(f"   Máximo: {coluna_stats.max():.4f}")
    
    print(f"\n   Quartis:")
    quartis = coluna_stats.quantile([0.25, 0.5, 0.75])
    print(f"   Q1 (25%): {quartis[0.25]:.4f}")
    print(f"   Q2 (50%): {quartis[0.5]:.4f}")
    print(f"   Q3 (75%): {quartis[0.75]:.4f}")
else:
    print("\n   (Não consegui identificar uma coluna de 'número de filhos' para análise)")
    print("   Mostrando estatísticas descritivas gerais:")
    print(df.describe())

# ============================================================================
# ETAPA 5: EXPLORAR PADRÕES DE AGRUPAMENTO
# ============================================================================
print("\n" + "="*80)
print("\033[1;31mETAPA 5: PADRÕES DE AGRUPAMENTO (groupby)\033[0m")
print("="*80)

# Agrupamento 1: Por gênero do cliente
print("\n\033[33mAgrupamento 1: VENDAS POR GÊNERO DO CLIENTE\033[0m")
if "CL_GENERO" in df.columns:
    vendas_por_genero = df.groupby("CL_GENERO").size()
    print(f"\n{vendas_por_genero}")
    print(f"\nInterpretação: Encontrei mais transações do gênero '{vendas_por_genero.idxmax()}' "
          f"({vendas_por_genero.max()} transações, {(vendas_por_genero.max()/len(df)*100):.1f}%)")
else:
    print("(Coluna CL_GENERO não encontrada)")

# Agrupamento 2: Por categoria de produto
print("\n\033[33mAgrupamento 2: VENDAS POR CATEGORIA DE PRODUTO\033[0m")
if "PR_CAT" in df.columns:
    vendas_por_categoria = df.groupby("PR_CAT").size().sort_values(ascending=False)
    print(f"\n{vendas_por_categoria}")
    print(f"\nInterpretação: A categoria '{vendas_por_categoria.idxmax()}' lidera com "
          f"{vendas_por_categoria.max()} transações")
else:
    print("(Coluna PR_CAT não encontrada)")

# Agrupamento 3 (bônus): Cruzamento entre gênero e categoria
print("\n\033[33mAgrupamento 3: CRUZAMENTO GÊNERO × CATEGORIA\033[0m")
if "CL_GENERO" in df.columns and "PR_CAT" in df.columns:
    tabela_cruzada = pd.crosstab(df["CL_GENERO"], df["PR_CAT"], margins=True)
    print(f"\n{tabela_cruzada.iloc[:, :5]}  # Mostrando apenas primeiras 5 categorias")
else:
    print("(Colunas necessárias não encontradas)")

# ============================================================================
# ETAPA 6: CONCLUSÕES E INSIGHTS
# ============================================================================
print("\n" + "="*80)
print("\033[1;31mETAPA 6: CONCLUSÕES E PRINCIPAIS INSIGHTS\033[0m")
print("="*80)

print("\n\033[33m1. QUALIDADE DOS DADOS:\033[0m")
total_celulas = df.shape[0] * df.shape[1]
celulas_nulas_finais = df.isnull().sum().sum()
qualidade_final = ((total_celulas - celulas_nulas_finais) / total_celulas) * 100
print(f"   Após limpeza, qualidade dos dados: {qualidade_final:.2f}%")
print(f"   A base está adequada para análises.")

print("\n\033[33m2. VOLUME E ABRANGÊNCIA:\033[0m")
print(f"   Total de {len(df):,} transações de varejo na base.")
if "CL_ID" in df.columns:
    clientes_unicos = df["CL_ID"].nunique()
    print(f"   {clientes_unicos} clientes únicos realizaram essas compras.")
if "PR_ID" in df.columns:
    produtos_unicos = df["PR_ID"].nunique()
    print(f"   {produtos_unicos} produtos diferentes foram vendidos.")

print("\n\033[33m3. PADRÕES DE COMPRA:\033[0m")
if "CL_GENERO" in df.columns:
    genero_dom = df["CL_GENERO"].value_counts().idxmax()
    print(f"   Gênero dominante entre clientes: {genero_dom}")
if "PR_CAT" in df.columns:
    categoria_dom = df["PR_CAT"].value_counts().idxmax()
    print(f"   Categoria mais popular: {categoria_dom}")

print("\n\033[33m4. DISTRIBUIÇÃO TEMPORAL:\033[0m")
if "DATA" in df.columns and df["DATA"].dtype == 'datetime64[ns]':
    print(f"   Dados cobrem o período de {df['DATA'].min().date()} a {df['DATA'].max().date()}")

print("\n\033[33m5. POSSÍVEIS PROBLEMAS REMANESCENTES:\033[0m")
print("   Verificar se existem outliers nos preços (dados extremos)")
print("   Investigar se há sazonalidade nas compras (período do ano)")
print("   Analisar comportamento de cada segmento de cliente (CL_SEG)")

print("\n\033[33m6. PRÓXIMOS PASSOS RECOMENDADOS:\033[0m")
print("   Análise de RFM (Recência, Frequência, Monetário) de clientes")
print("   Segmentação de clientes com clustering")
print("   Previsão de demanda por categoria de produto")
print("   Correlação entre características do cliente e comportamento de compra")

print("\n" + "="*80)
print("\033[1;32mANÁLISE CONCLUÍDA COM SUCESSO!\033[0m")
print("="*80 + "\n")