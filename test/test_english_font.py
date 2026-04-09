#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 测试英文显示功能
import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import plot_word_frequency, count_words, clean_text

# 测试英文数据
sample_text = "Hello World! This is a sample text. Hello again!"
print(f"原始文本: {sample_text}")
print(f"清理后(保留中文): {clean_text(sample_text)}")
print(f"清理后(不保留中文): {clean_text(sample_text, keep_chinese=False)}")
word_counts = count_words(sample_text)
print(f"单词计数: {word_counts}")

# 测试绘制英文图表
print("\n绘制英文图表...")
plot_word_frequency(word_counts, top_n=5)
print("图表绘制完成!")