import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.llm_util import *

# fname = "../data/fra-eng.zip"
# base_dir = os.path.dirname("../data/fra-eng.zip")
# print(base_dir)

# data_dir, ext = os.path.splitext(fname)
# print(data_dir)
# print(ext)

# fp = zipfile.ZipFile(fname, 'r')

batch_size, num_steps = 64, 10
train_iter, src_vocab, tgt_vocab = load_data_nmt(batch_size, num_steps)

# 打印train_iter一个迭代的数据内容
for batch in train_iter:
    src, src_valid_len, tgt, tgt_valid_len = batch
    print("源序列:", src)
    print("源序列有效长度:", src_valid_len)
    print("目标序列:", tgt)
    print("目标序列有效长度:", tgt_valid_len)
    break

# 打印src_vocab 中每个index及其对应的文本
for idx, token in enumerate(src_vocab.idx_to_token):
    print(f"Index {idx}: {token}")
