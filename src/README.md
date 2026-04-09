# LLM Algorithm 库函数

本目录包含了llm-algorithm项目的核心库函数，可以在Jupyter Notebook中引用使用。

## 目录结构

```
src/
├── __init__.py      # 包初始化文件
├── utils.py         # 实用工具函数
└── README.md        # 库使用说明
```

## 使用方法

### 在Jupyter Notebook中引用

要在Jupyter Notebook中使用这些库函数，您需要：

1. 确保您的Notebook位于`notebooks/`目录下
2. 在Notebook的开头添加以下代码，将`src`目录添加到Python路径中：

```python
import sys
sys.path.append('../src')
```

3. 导入所需的函数：

```python
from utils import hello_world, clean_text, tokenize_text, count_words, plot_word_frequency
```

或导入所有函数：

```python
from utils import *
```

### 示例

```python
# 导入所有工具函数
import sys
sys.path.append('../src')
from utils import *

# 使用hello_world函数
print(hello_world("LLM Algorithm"))

# 文本处理示例
sample_text = "Hello World! This is a sample text. Hello again!"
cleaned_text = clean_text(sample_text)
tokens = tokenize_text(sample_text)
word_counts = count_words(sample_text)

# 可视化示例
plot_word_frequency(word_counts, top_n=5)
```

## 可用函数

### 基本函数
- `hello_world(name)`: 简单的问候函数

### 文本处理函数
- `clean_text(text)`: 清理文本，移除特殊字符和多余空格
- `tokenize_text(text)`: 将文本拆分为单词列表
- `count_words(text)`: 统计文本中每个单词的出现次数

### 数据可视化函数
- `plot_word_frequency(word_counts, top_n)`: 绘制单词频率条形图

### 数值计算函数
- `calculate_mean(numbers)`: 计算平均值
- `calculate_accuracy(predictions, targets)`: 计算分类准确率

### 辅助函数
- `print_dict(d, indent)`: 格式化打印字典

## 扩展库

要扩展这个库，您可以：

1. 在`utils.py`中添加新的函数
2. 或者创建新的模块文件（如`nlp.py`, `ml.py`等），然后在`__init__.py`中导入这些模块

## 依赖

本库使用以下Python库：
- numpy
- matplotlib
- seaborn

这些依赖已经包含在项目的`pyproject.toml`文件中，可以通过Poetry安装：

```bash
poetry install
```