import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

Path = '/Users/wesley/GitProject/statistics/png/user_personalize_features'
# Set a style for the plots
sns.set_theme(style="whitegrid")

# global parameter
figsize_:tuple = (16, 8)
dpi_:int = 300
fts_title:int = 14
fts_label:int = 12
fts_font:int = 10
palette = sns.color_palette(['#3d5a80', '#98c1d9', '#e0fbfc', '#ee6c4d', '#293241'])
default_color = '#3d5a80'
bar_width = 0.4

# method
def DrawBar(cols: list, df: pd.DataFrame):  # 柱状图
    rows = (len(cols) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()
    for ax, col in zip(axes, cols):
        sns.countplot(data=df, x=col, hue=col, palette=palette, edgecolor='black', width=bar_width, ax=ax)
        ax.set_title(f'Distribution of {col}', fontsize=fts_title, fontweight='bold')
        ax.set_xlabel(col, fontsize=fts_label)
        ax.set_ylabel('Counts', fontsize=fts_label)
        if df[col].nunique() > 10:
            ax.set_xticklabels(ax.get_xticklabels(), fontsize=fts_font, rotation=90)
        else:
            ax.set_xticklabels(ax.get_xticklabels(), fontsize=fts_font, rotation=0)
        ax.tick_params(axis='y', labelsize=fts_font)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    for ax in axes[len(cols):]:
        ax.remove()
    plt.tight_layout()
    plt.savefig(f'{Path}/object/{"_".join(cols)}_Bar.png')
    plt.close()

def DrawHist(cols: list, df: pd.DataFrame):  # 直方图
    rows = (len(cols) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()
    for ax, col in zip(axes, cols):
        sns.histplot(df[col], kde=True, color='skyblue', edgecolor='black', ax=ax)
        ax.set_title(f'Distribution of {col}', fontsize=fts_title, fontweight='bold')
        ax.set_xlabel(col, fontsize=fts_label)
        ax.set_ylabel('Frequency', fontsize=fts_label)
        ax.tick_params(axis='x', labelsize=fts_font)
        ax.tick_params(axis='y', labelsize=fts_font)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    for ax in axes[len(cols):]:
        ax.remove()
    plt.tight_layout()
    plt.savefig(f'{Path}/numeric/{"_".join(cols)}_hist.png')
    plt.close()

def DrawBox(x: str, ys: list, df: pd.DataFrame):  # 箱线图
    rows = (len(ys) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()
    for ax, y in zip(axes, ys):
        sns.boxplot(data=df, x=x, y=y, hue=x, width=0.4, palette='muted', ax=ax)
        ax.set_title(f'Boxplot of {x} vs {y}', fontsize=fts_title, fontweight='bold')
        ax.set_xlabel(x, fontsize=fts_label)
        ax.set_ylabel(y, fontsize=fts_label)
        ax.tick_params(axis='x', labelsize=fts_font)
        ax.tick_params(axis='y', labelsize=fts_font)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    for ax in axes[len(ys):]:
        ax.remove()
    plt.tight_layout()
    plt.savefig(f'{Path}/numeric/{x}_{"_".join(ys)}_Box.png')
    plt.close()

def Drawpdf(cols: list, df: pd.DataFrame, hue: str = None):  # 概率密度图
    rows = (len(cols) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()
    for ax, col in zip(axes, cols):
        if hue:
            sns.kdeplot(data=df, x=col, hue=hue, fill=True, shade=True, palette='coolwarm', ax=ax)
        else:
            sns.kdeplot(data=df, x=col, fill=True, shade=True, color='blue', ax=ax)
        ax.set_title(f'Distribution of {col}', fontsize=fts_title, fontweight='bold')
        ax.set_xlabel(col, fontsize=fts_label)
        ax.set_ylabel('Density', fontsize=fts_label)
        ax.tick_params(axis='x', labelsize=fts_font)
        ax.tick_params(axis='y', labelsize=fts_font)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    for ax in axes[len(cols):]:
        ax.remove()
    plt.tight_layout()
    plt.savefig(f'{Path}/numeric/{"_".join(cols)}_pdf.png')
    plt.close()

def DrawPie(cols: list, df: pd.DataFrame):  # 饼图
    rows = (len(cols) + 2) // 3
    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()
    for ax, col in zip(axes, cols):
        df[col].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=False, colors=palette, ax=ax)
        ax.set_title(f'Distribution of {col}', fontsize=fts_title, fontweight='bold')
        ax.set_ylabel('')
        ax.tick_params(axis='x', labelsize=fts_font)
        ax.tick_params(axis='y', labelsize=fts_font)
    for ax in axes[len(cols):]:
        ax.remove()
    plt.tight_layout()
    plt.savefig(f'{Path}/object/{"_".join(cols)}_Pie.png')
    plt.close()
    
def DrawGraph(cols: list, df: pd.DataFrame, graph_type: str, x: str = None, hue: str = None):

    max_plots_per_fig = 6 # 每张画布最多8个图
    num_figs = (len(cols) + max_plots_per_fig - 1) // max_plots_per_fig # 计算需要多少张画布
    
    for fig_num in range(num_figs): # 循环画布
        start_idx = fig_num * max_plots_per_fig
        end_idx = min(start_idx + max_plots_per_fig, len(cols))
        current_cols = cols[start_idx:end_idx]
        
        fig, axes = plt.subplots(2, 3, figsize=figsize_, dpi = dpi_)
        axes = axes.flatten()
        
        for ax, col in zip(axes, current_cols):
            if graph_type == 'Barplot':
                sns.countplot(data=df, x=col, hue=col, palette=palette, edgecolor='black', width=bar_width, ax=ax, legend=False)
                ax.set_ylabel('Counts', fontsize=fts_label)
            elif graph_type == 'Histplot':
                sns.histplot(df[col], kde=True, color=default_color, edgecolor='black', ax=ax)
                ax.set_ylabel('Frequency', fontsize=fts_label)
            elif graph_type == 'Boxplot' and x:
                sns.boxplot(data=df, x=x, y=col, hue=x, width=0.4, palette=palette, ax=ax, legend=False)
                ax.set_ylabel(col, fontsize=fts_label)
            elif graph_type == 'Pdfplot':
                if hue:
                    sns.kdeplot(data=df, x=col, hue=hue, fill=True, shade=True, palette=palette, ax=ax)
                else:
                    sns.kdeplot(data=df, x=col, fill=True, shade=True, color=default_color, ax=ax)
                ax.set_ylabel('Density', fontsize=fts_label)
            elif graph_type == 'Pieplot':
                sns.pieplot(df[col].value_counts(), labels=df[col].value_counts().index, autopct='%1.1f%%', startangle=90, colors=palette, ax=ax)
                ax.set_ylabel('')
            else:
                raise ValueError("Unsupported graph type")
            
            ax.set_title(f'{graph_type} of {col.replace("_", " ")}', fontsize=fts_title, fontweight='bold')
            ax.set_xlabel(col, fontsize=fts_label)
            ax.tick_params(axis='x', labelsize=fts_font)
            ax.tick_params(axis='y', labelsize=fts_font)
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            
            # 自动调整标签角度
            if len(ax.get_xticklabels()) > 10 or any(len(label.get_text()) > 10 for label in ax.get_xticklabels()):
                ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        
        for ax in axes[len(current_cols):]: # 删除多余的子图
            ax.remove()
        
        plt.tight_layout()
        if x:
            plt.savefig(f'{Path}/{graph_type} of {x}{fig_num + 1}.png')
        else:
            plt.savefig(f'{Path}/{graph_type} of {col}{fig_num + 1}.png')
        plt.close()

def DrawHeatmap(col_list: list, df: pd.DataFrame) -> None:
    plt.figure(figsize=figsize_, dpi=dpi_)  # 创建一个新的图形，指定大小和分辨率
    corr = df[col_list].corr()  # 计算指定列的相关矩阵
    mask = np.triu(np.ones_like(corr, dtype=bool))  # 为相关矩阵的上三角创建一个掩码
    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5, square=True)  # 使用相关矩阵、掩码和指定样式绘制热图
    plt.title('Correlation Heatmap', fontsize=fts_title, fontweight='bold')  # 设置热图的标题
    plt.xticks(fontsize=fts_font)  # 设置x轴和y轴刻度的字体大小
    plt.yticks(fontsize=fts_font)  # 设置x轴和y轴刻度的字体大小
    plt.tight_layout()  # 调整布局以适应所有内容
    plt.savefig(f'{Path}/Correlation_Heatmap.png')  # 将热图保存到文件
    plt.close()  # 关闭图形以释放内存

def DrawScatter(col1:str, col2:str, hue_col:str, df:pd.DataFrame)->None:
    plt.figure(figsize=figsize_, dpi=dpi_)
    sns.scatterplot(data=df, x = col1, y = col2, hue = hue_col, palette = palette,
                    edgecolor = 'black', alpha = 0.7, legend =  True)
    plt.title(f'Scatter plot of {col1.replace('_', ' ')} vs {col2.replace('_', ' ')}', fontsize = fts_title, fontweight = 'bold')
    plt.xlabel(col1.replace('_', ' '), fontsize = fts_label)
    plt.ylabel(col2.replace('_', ' '), fontsize = fts_label)
    plt.xticks(fontsize = fts_font)
    plt.yticks(fontsize= fts_font)
    plt.tight_layout()
    plt.savefig(f'{Path}/Scatter plot of {col1.replace('_', ' ')} vs {col2.replace('_', ' ')}.png')
    plt.close()

