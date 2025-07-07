import pandas as pd
import numpy as np

# Aquisição de dados
df = pd.read_csv('data/base_vendas.csv')
df.tail()

# Informações iniciais
qtd_linhas = df.shape[0]
qtd_colunas = df.shape[1]
print(f"Número de linhas: {qtd_linhas}, Número de colunas: {qtd_colunas}")

# Verificar tipos de dados e valores faltantes
df.info()
df.describe().round(1)
df.describe(include=object)

# Colunas não padronizadas
df.columns

# Verificando valores faltantes
df.isnull().sum()
df.isnull().sum() / qtd_linhas * 100

# Verificando duplicatas
df.duplicated().sum()

# Padronização das colunas 
colunas = [
    'matricula_funcionario', 'nome_funcionario', 'cargo', 'codigo_loja',
    'nome_loja', 'codigo_produto', 'descricao_produto', 'categoria',
    'preco_custo', 'valor_unitario', 'quantidade', 'comissao',
    'dt_venda', 'dt_entrega'
]
df.columns = colunas
df.columns

# Converter matrícula para string
df.matricula_funcionario = df.matricula_funcionario.astype('str')
df.info()

# Corrigir separador decimal e converter para float
df['valor_unitario'] = df['valor_unitario'].str.replace(',', '.')
df['preco_custo'] = df['preco_custo'].str.replace(',', '.')
df['comissao'] = df['comissao'].str.replace(',', '.')

df.valor_unitario

df = df.astype({
    'valor_unitario': np.float64,
    'preco_custo': np.float64,
    'comissao': np.float64
})
df.info()

# Conversão de datas
df['dt_venda'] = pd.to_datetime(df['dt_venda'], format='%d/%m/%Y %H:%M')
df['dt_entrega'] = pd.to_datetime(df['dt_entrega'], format='%d/%m/%Y %H:%M')

df.dt_venda
df.dt_entrega
df['dt_venda'].dt.year

# Preenchimento de valores nulos - forward fill (cópia do valor anterior)
df.comissao.ffill()

# Backward fill (cópia do valor seguinte)
df.comissao.bfill()

# Apagar coluna (sem alterar df original)
df.drop(columns=['comissao'])

# Apagar linhas com valores nulos
df.dropna()

# Apagar colunas com valores nulos
df.dropna(axis='columns')

# Substituir valores faltantes pela média
df['comissao'].fillna(df['comissao'].mean().round(2))

# Criar nova coluna com o faturamento total da venda
df['valor_total'] = df['quantidade'] * df['valor_unitario']
df.head()

# Ordenar dados por categoria (A-Z) e valor total 
df.sort_values(['categoria', 'valor_total'], ascending=[True, False], inplace=True)
df.head()

# Verificação de duplicatas em colunas específicas
df.duplicated().sum()
df['categoria'].duplicated().sum()
df['categoria'].value_counts()

# Remover duplicatas sem alterar a tabela original
df.drop_duplicates()
df['categoria'].duplicated().sum()