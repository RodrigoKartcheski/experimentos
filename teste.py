import pandas as pd
from datamerge.main import DataMergeLoader

# Criando o DataFrame de origem (df_source)
data_source = {'chave_primaria': [1, 2, 3],
               'coluna1': ['A', 'B', 'C'],
               'coluna2': [10, 20, 30]}
df_source = pd.DataFrame(data_source)

# Criando o DataFrame alvo (df_target)
data_target = {'chave_primaria': [2, 3, 4],
               'coluna1': ['D', 'E', 'F'],
               'coluna2': [40, 50, 60]}
df_target = pd.DataFrame(data_target)

# Imprimindo os DataFrames
print("df_source:")
print(df_source)
print("\ndf_target:")
print(df_target)

col_pk = 'chave_primaria'

result_df = DataMergeLoader.merge_df(df_source, df_target, col_pk)
print(result_df)