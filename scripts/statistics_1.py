import pandas as pd

def Obj_Col_Count_Per(col:str, df:pd.DataFrame)->pd.DataFrame: # 计算某一列的频数和百分比
    result = df[col].value_counts().reset_index()
    result.columns = [col, 'count'] # 重命名列名
    result['percentage'] = [x/df.shape[0] for x in result['count']] # 计算百分比
    return result

def Print_Obj_Col_Count_Per(cols:list, df:pd.DataFrame)->pd.DataFrame: # 打印某一列的频数和百分比
    for col in cols:
        print(Obj_Col_Count_Per(col, df), '\n')

def GroupInfo(group_by_col:str, col:str, df:pd.DataFrame): # 按照某一列分组，计算多列的统计信息
    grouped = df.groupby(group_by_col)
    result = grouped[col].agg(['mean', 'std', 'min', ('median', 'median'), 'max']).reset_index()
    return result

def Print_GroupInfo(group_by_col:str, col_list:list, df:pd.DataFrame): # 打印按照某一列分组，计算多列的统计信息
    for col in col_list:
        print(f'{col.replace('_', ' ')} description grouped by {group_by_col.replace('_',' ')}\n',GroupInfo(group_by_col, col, df), '\n')

