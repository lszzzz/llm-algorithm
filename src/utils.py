#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具函数库 - 提供可在Jupyter Notebook中引用的通用功能

本模块包含各种实用工具函数，主要用于文本处理、数据可视化和模型评估等任务。
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from typing import List, Dict, Any, Optional


def hello_world(name: str = "World") -> str:
    """
    简单的问候函数
    
    Args:
        name (str): 要问候的名称，默认为"World"
        
    Returns:
        str: 格式化的问候字符串
    """
    return f"Hello, {name}!"


def clean_text(text: str) -> str:
    """
    文本清理函数 - 移除特殊字符和多余空格
    
    Args:
        text (str): 待清理的文本
        
    Returns:
        str: 清理后的文本
    """
    # 转换为小写
    text = text.lower()
    # 移除特殊字符，只保留字母、数字和空格
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def tokenize_text(text: str) -> List[str]:
    """
    文本分词函数 - 将文本拆分为单词列表
    
    Args:
        text (str): 待分词的文本
        
    Returns:
        List[str]: 单词列表
    """
    # 先清理文本
    clean = clean_text(text)
    # 按空格分词
    tokens = clean.split()
    return tokens


def count_words(text: str) -> Dict[str, int]:
    """
    单词计数函数 - 统计文本中每个单词的出现次数
    
    Args:
        text (str): 待统计的文本
        
    Returns:
        Dict[str, int]: 单词计数字典
    """
    tokens = tokenize_text(text)
    word_count = {}
    for token in tokens:
        if token in word_count:
            word_count[token] += 1
        else:
            word_count[token] = 1
    return word_count


def plot_word_frequency(word_counts: Dict[str, int], top_n: int = 10) -> None:
    """
    绘制单词频率条形图
    
    Args:
        word_counts (Dict[str, int]): 单词计数字典
        top_n (int): 显示前N个最频繁的单词，默认为10
    """
    # 按频率降序排序
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*sorted_counts)
    
    # 创建条形图
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(counts), y=list(words))
    plt.xlabel('出现次数')
    plt.ylabel('单词')
    plt.title(f'前{top_n}个最频繁的单词')
    plt.show()


def calculate_mean(numbers: List[float]) -> float:
    """
    计算平均值
    
    Args:
        numbers (List[float]): 数字列表
        
    Returns:
        float: 平均值
    """
    return sum(numbers) / len(numbers)


def calculate_accuracy(predictions: List[Any], targets: List[Any]) -> float:
    """
    计算分类准确率
    
    Args:
        predictions (List[Any]): 预测结果列表
        targets (List[Any]): 真实标签列表
        
    Returns:
        float: 准确率，范围在0到1之间
    """
    if len(predictions) != len(targets):
        raise ValueError("预测结果和真实标签的长度必须相同")
    
    correct = 0
    for pred, target in zip(predictions, targets):
        if pred == target:
            correct += 1
    
    return correct / len(predictions)


def print_dict(d: Dict[Any, Any], indent: int = 0) -> None:
    """
    格式化打印字典
    
    Args:
        d (Dict[Any, Any]): 要打印的字典
        indent (int): 缩进级别，默认为0
    """
    for key, value in d.items():
        print('  ' * indent + str(key) + ':')
        if isinstance(value, dict):
            print_dict(value, indent + 1)
        else:
            print('  ' * (indent + 1) + str(value))


if __name__ == "__main__":
    # 示例用法
    print("工具函数库示例:")
    print(hello_world("LLM Algorithm"))
    
    sample_text = "Hello World! This is a sample text. Hello again!"
    print(f"\n原始文本: {sample_text}")
    print(f"清理后: {clean_text(sample_text)}")
    print(f"分词结果: {tokenize_text(sample_text)}")
    print(f"单词计数: {count_words(sample_text)}")