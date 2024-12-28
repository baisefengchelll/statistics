import pandas as pd
import seaborn as sns
import warnings
import draw
import statistics_1 as sts1
warnings.filterwarnings('ignore')

# Load data
data = pd.read_csv('data/user_personalized_features.csv',index_col='User_ID')

# Drop the first column and remove duplicates
data.drop(columns='Unnamed: 0', inplace=True)
data.drop_duplicates(inplace=True)

# data description
print('缺失值统计\n ', data.isna().sum(), '\n')
print('---------------------------------------\n')
print('重复值统计\n ', data.duplicated().sum())
print('---------------------------------------\n')
print('变量属性\n ', data.dtypes)
print('---------------------------------------\n')
print('数据描述\n ', data.describe())

# data type
object_columns = data.select_dtypes(include=['object','bool']).columns
numeric_columns = data.select_dtypes(exclude=['object','bool']).columns
print('---------------------------------------\n')
print(' Object Columns\n', object_columns)
print('---------------------------------------\n')
print(' Numeric Columns\n', numeric_columns)

# descriptive statistics
draw.DrawGraph(cols=object_columns, df = data, graph_type='Barplot') # 绘制柱状图
draw.DrawGraph(cols=numeric_columns, df=data, graph_type = 'Histplot') # 绘制直方图
draw.DrawGraph(cols=numeric_columns, df=data, graph_type='Pdfplot') # 绘制概率密度图

for grouped_col in object_columns:
    print('-------------------------------------------------------------------------\n')
    sts1.Print_GroupInfo(group_by_col='Location', col_list=numeric_columns, df=data)
    draw.DrawGraph(cols=numeric_columns, df = data, graph_type='Boxplot', x='Location')

draw.DrawScatter(col1='Age', col2='Income', hue_col='Gender', df=data)
sns.pairplot(data[numeric_columns])