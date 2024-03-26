# MCTS: A Multi-Reference Chinese Text Simplification Dataset

## ✨ 简介

LREC-COLING 2024 论文 **[MCTS (Multi-Reference Chinese Text Simplification Dataset)](<https://arxiv.org/abs/2306.02796>) 的官方仓库。

文本简化任务是自然语言处理领域的基础任务之一，旨在通过改写使句子更容易理解。文本简化可以助力分级阅读、机器翻译等研究，并帮助语言学习者理解复杂文本。目前，关于中文文本简化的研究较少，缺乏通用的评估数据是重要原因之一。为此，我组构建了多参考中文文本简化数据集 MCTS（Multi-Reference Chinese Text Simplification Dataset）。该数是迄今为止中文文本简化任务上规模最大、参考最多的评估数据集，包括 723 条从新闻语料中挑选的复杂结构句子，每一句分别包含多条人工简化后的句子。这是我们探索中文文本简化的一项基础性工作，期望能为今后的研究提供参考。

论文地址：[https://arxiv.org/abs/2306.02796](< https://arxiv.org/abs/2306.02796 >)

### 数据规模

MCTS 数据集是中文文本简化任务上规模最大、参考最多的评估数据集，包括 723 条从新闻语料中挑选的复杂结构句，每个句子分别包含 5 条人工简化后的句子。通过这项基础性工作，我们希望能建立对中文文本简化的基本认识，为今后的研究提供参考。

### 数据格式

所有文件均为纯文本格式。在文件中，每行是一个文本样本。

文件的内容以命名方式区分。文件的名称由三部分组成：前缀、中缀和后缀。命名格式为：

```
前缀.中缀.后缀（.num）
```

所有文件均以 ``mcts`` 为前缀。中缀为 ``test`` 的文件是测试集，中缀为 ``dev`` 的文件是开发集。

后缀为 ``orig`` 的文件是未经简化的源语句文件。由标注员简化的5条参考句后缀为 ``simp`` ，后接序号。对于拥有相同中缀的源语句文件和参考句文件，其中句子是按行一一对应的。

### 数据示例

![alt 数据示例](https://github.com/blcuicall/mcts/blob/main/images/exp.png)

### 评估方式

我们采用 [EASSE](https://github.com/feralvam/easse) 提供的自动化评估指标SARI、BLEU，以及Kong等人在论文 [*Multitasking framework for unsupervised simple definition generation*](https://arxiv.org/abs/2203.12926) 中提供的HSK-Level评估方式。

*注：若您使用 EASSE 软件包进行评估，您应该先对所有测试数据执行分词。*

用于评估 HSK-Level 的脚本放在 ``script`` 目录下。若想评估测试集源语句文件 ``mcts.test.orig`` 的HSK-Level，使用以下指令：

```sh
python scripts/hsk_evaluate.py dataset/mcts.test.orig
```

## 🛠️ 训练数据构建

由于大规模平行语料的稀缺，我们采用机器翻译与英文文本简化相结合的方法构建训练语料。（方法详见论文）

![alt 训练数据构建](https://github.com/blcuicall/mcts/blob/main/images/pseudo_data.png)

经过严格的自动筛选，我们最终获得了691,474条高质量平行训练数据，这也是迄今为止在中文文本简化领域规模最大的可用训练数据。我们通过实验证明了数据的有效性。（详见相关实验）

这些数据放在``pseudo_data``目录下，其中``zh_selected.ori``为复杂句，``zh_selected.sim``为简单句。

## 📊 文本特征分析

我们计算了简化示例的 8 种文本特征。以下为文本特征的统计图。（详细数据见论文）

![alt 评测结果](https://github.com/blcuicall/mcts/blob/main/images/feature.png)

## 🧪 相关实验

我们对多种基线方法进行了比较，这些方法包括：

- **OpenAI 模型**（gpt-3.5-turbo, text-davinci-003）：使用 GPT-3.5-turbo 和 text-davinci-003 模型的测试结果；
- **直接反向翻译**（Direct Back Translation）：谷歌翻译进行反向翻译的生成结果；
- **翻译Wiki-Large**（Translated Wiki-Large）：使用翻译的 Wiki-Large 数据集训练的 BART-base 文本简化模型生成的测试结果；
- **跨语言伪数据**（Cross-Lingual Pseudo Data）： 用构造的数据训练 BART-Base 模型生成的测试结果。

使用自动化评估工具计算的 SARI、BLEU、HSK-Level 结果如下表：

![alt 评测结果](https://github.com/blcuicall/mcts/blob/main/images/result1-mod.png)

对其中表现较好的几种代表性方法，我们聘请语言学背景的同学，从流利性、语义完整性和简单性三个方面，进行了人工评估。评估结果如下：

![alt 评测结果](https://github.com/blcuicall/mcts/blob/main/images/result2-mod.png)

MCTS数据集中的人工简化参考 (Gold Reference) 在人工评估中获得了最好的平均分数和排名，明显优于简化系统的输出结果。

## 作者

如果您有任何问题，或对我们的相关研究感兴趣，欢迎联系我们！

崇瑞宁：（chongruining@outlook.com）

鲁鹿鸣：（lulm410402@foxmail.com）

欢迎关注[**BLCU-ICALL研究组**](< https://blcuicall.org >)的主页和最新动态！

## 引用

如果使用了 MCTS 数据集，请您引用：

```
@misc{chong-2023-mcts,
      title={MCTS: A Multi-Reference Chinese Text Simplification Dataset}, 
      author={Ruining Chong and Luming Lu and Liner Yang and Jinran Nie and Shuhan Zhou and Yaoxin Li and Erhong Yang},
      year={2023},
      eprint={2306.02796},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@misc{kong-acl-2022-simpdefiner,
      title={Multitasking Framework for Unsupversied Simple Definition Generation}, 
      author={Cunliang Kong and Yun Chen and Hengyuan Zhang and Liner Yang and Erhong Yang},
      booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},     
      year={2022}
}
```
