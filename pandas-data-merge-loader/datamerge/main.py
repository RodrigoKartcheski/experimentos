import pandas as pd

class DataMergeLoader:
    @staticmethod
    def merge_df(df_source, df_target, col_pk):
        # Onde tem valor em target mas não tem em source então deleta
        merged_df = df_target.merge(df_source, on=col_pk, how='left', indicator=True, suffixes=('', '_y'))
        delete_df = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
        delete_df = delete_df[df_target.columns]
        delete_df['transact_op'] = 'D'
        
        # Onde tem valor em source mas não tem em target então deleta
        merged_df = df_source.merge(df_target, on=col_pk, how='left', indicator=True, suffixes=('', '_y'))
        insert_df = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
        insert_df = insert_df[df_source.columns]
        insert_df['transact_op'] = 'I'
        
        # Onde as chaves são iguais em ambos então faz update
        compared_df = df_source.assign(Equal=(df_source == df_target).all(axis='columns'))
        update_df = pd.merge(compared_df, df_target[col_pk], on=col_pk, how='inner', indicator=True, suffixes=('', '_y')).drop('_merge', axis=1)
        update_df = update_df[update_df["Equal"] == False].drop("Equal", axis=1)
        update_df['transact_op'] = 'U'
        
        result_df = pd.concat([insert_df, delete_df, update_df], ignore_index=True)
        return result_df

if __name__ == '__main__':
    # Remova as chamadas das funções que não fazem parte do código
    pass