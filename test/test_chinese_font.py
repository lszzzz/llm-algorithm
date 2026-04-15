#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 测试中文显示修复
import sys
import os

# 添加项目根目录到Python路径，这样可以正确导入src包
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.utils import plot_word_frequency, count_words

# 测试数据
sample_text = "你好 世界! 这是一个测试文本。你好 再次!"
print(f"原始文本: {sample_text}")
word_counts = count_words(sample_text)
print(f"单词计数: {word_counts}")

# 测试绘制中文图表
print("\n绘制中文图表...")
plot_word_frequency(word_counts, top_n=5)
print("图表绘制完成!")