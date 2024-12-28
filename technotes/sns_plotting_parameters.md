# sns库绘图接口的常用参数

`seaborn`（简称 `sns`）是一个基于 `matplotlib` 的数据可视化库，提供了更高级的接口来绘制统计图表。以下是 `sns` 库绘图接口的一些常用参数及其含义：

## 常用参数

- `data`：数据集，通常是 `pandas` 的 `DataFrame`。
- `x`：指定 x 轴数据的变量名。
- `y`：指定 y 轴数据的变量名。
- `hue`：根据该变量的不同值对数据进行分组，并用不同颜色显示。
- `palette`：指定调色板，用于设置不同类别的颜色。
- `style`：根据该变量的不同值对数据进行分组，并用不同的线条样式显示。
- `size`：根据该变量的不同值对数据进行分组，并用不同的点大小显示。
- `col`：根据该变量的不同值对数据进行分组，并在不同的列中显示。
- `row`：根据该变量的不同值对数据进行分组，并在不同的行中显示。
- `kind`：指定图表类型，如 `scatter`（散点图）、`line`（折线图）、`bar`（条形图）等。
- `height`：每个子图的高度（以英寸为单位）。
- `aspect`：子图的宽高比。
- `markers`：指定散点图中点的形状。
- `legend`：是否显示图例，布尔值。
- `ax`：指定绘图的 `matplotlib` 轴对象。

## 示例

```python
import seaborn as sns
import pandas as pd

# 创建示例数据
data = pd.DataFrame({
    'x': range(10),
    'y': range(10),
    'category': ['A', 'B'] * 5
})

# 绘制散点图
sns.scatterplot(data=data, x='x', y='y', hue='category', palette='deep')
```

以上示例中，`data` 参数指定了数据集，`x` 和 `y` 参数指定了 x 轴和 y 轴的数据，`hue` 参数根据 `category` 变量的不同值对数据进行分组，并用不同颜色显示。
