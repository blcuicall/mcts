# -*- coding: utf-8 -*-
import pandas as pd
import sys
import jieba


def read_hsk_vocab(path):
    hsk_vocab = {}
    vocab = pd.read_excel(path)
    level_keys = {
        '一级': 1,
        '二级': 2,
        '三级': 3,
        '四级': 4,
        '五级': 5,
        '六级': 6,
        '七-九级': 7
    }
    for k in level_keys:
        for word in vocab[k].dropna():
            if '/' in word:
                words = word.split('/')
                for w in words:
                    hsk_vocab[w.strip()] = level_keys[k]
            else:
                hsk_vocab[word.strip()] = level_keys[k]
    return hsk_vocab


def count_nums(file_path, hsk_vocab):
    level_freq = {}
    num_tokens = 0
    num_types = 0
    with open(file_path) as fr:
        for line in fr:
            line = line.strip().replace(' ', '')
            seg_line = jieba.lcut(line)
            for word in seg_line:
                if word in hsk_vocab:
                    level = hsk_vocab[word]
                else:
                    level = 8
                if level not in level_freq:
                    level_freq[level] = {}
                if word not in level_freq[level]:
                    level_freq[level][word] = 0
                    num_types += 1
                level_freq[level][word] += 1
                num_tokens += 1
    return level_freq, num_tokens, num_types


def main(*argv):
    if not argv:
        argv = sys.argv[1:]
    assert len(argv) == 1

    inp_file = argv[0]
    hsk_vocab = read_hsk_vocab('metrics/vocab.xls')

    level_freq, num_tokens, num_types = count_nums(inp_file, hsk_vocab)
    # for level in level_freq:
    #     level_types = len(level_freq[level])
    #     level_tokens = sum(level_freq[level].values())
    #     level_type_rate = (level_types / num_types) * 100
    #     level_token_rate = (level_tokens / num_tokens) * 100
    #     print(f"{level_type_rate},{level_token_rate}")

    low_level_types = 0
    low_level_tokens = 0
    for level in [1, 2, 3]:
        low_level_types += len(level_freq[level])
        low_level_tokens += sum(level_freq[level].values())
    low_level_type_rate = (low_level_types / num_types) * 100
    low_level_token_rate = (low_level_tokens / num_tokens) * 100
    # print(f"Low Level Type Rate: {low_level_type_rate:.2f}%")
    print(f"Low Level Token Rate: {low_level_token_rate:.2f}%")

    high_level_types = 0
    high_level_tokens = 0
    for level in [7, 8]:
        high_level_types += len(level_freq[level])
        high_level_tokens += sum(level_freq[level].values())
    high_level_type_rate = (high_level_types / num_types) * 100
    high_level_token_rate = (high_level_tokens / num_tokens) * 100
    # print(f"High Level Type Rate: {high_level_type_rate:.2f}%")
    print(f"High Level Token Rate: {high_level_token_rate:.2f}%")

    return 0


if __name__ == '__main__':
    sys.exit(main())
