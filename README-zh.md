# MCTS: A Multi-Reference Chinese Text Simplification Dataset

## ✨ 简介

LREC-COLING 2024 论文 **[MCTS: Multi-Reference Chinese Text Simplification Dataset](<https://aclanthology.org/2024.lrec-main.969>)** 的官方仓库。

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

<!-- ![alt DataExample](https://github.com/blcuicall/mcts/blob/main/images/exp.png) -->
| 原句 | 简化句 |
|----------|-----------|
| 为适应大西南进出口物资迅速增长的需要，北部湾沿海四市开始了新一轮建港热潮。<br> In order to adapt to the rapid growth of import and export materials in the southwest, four coastal cities in the Beibu Gulf have started a new wave of port construction. | 大西南进口和出口物资的需要迅速增长，北部湾沿海四座城市兴起了新一轮港口建设。<br> The demand for imported and exported materials in the southwest has grown rapidly. Four coastal cities in the Beibu Gulf have begun a new round of port construction.  |
| 中国又一条煤炭运输大通道──连接天津蓟县与天津港之间的蓟港铁路日前破土动工。<br>Another major coal transportation corridor in China - the Jigang Railway connecting Tianjin Jixian County and Tianjin Port - has recently broken ground. | 蓟港铁路连接天津蓟县和天津港，用于煤炭运输，前几天开始建造。<br>Jigang Railway connects Tianjin Jixian County and Tianjin Port for coal transportation, and construction began a few days ago.  | 
| 按设计，“进步M-24”号载重飞船可同轨道站在无人操纵的情况下进行自动对接。<br>According to the design, the "Progress M-24" heavy-duty spacecraft can automatically dock with the orbital station under unmanned control. | 按照设计，无人操控的“进步M-24”号飞船可以自动对接轨道站。<br>According to the design, the unmanned "Progress M-24" spacecraft can automatically dock with the orbital station. |


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

- **OpenAI 模型**（gpt-3.5-turbo, text-davinci-003）：使用 GPT-3.5-turbo 和 text-davinci-003 模型的测试结果。我们还在 GPT-3.5-turbo 上进行了In-context Few-shot的测试；
- **直接反向翻译**（Direct Back Translation）：谷歌翻译进行反向翻译的生成结果；
- **翻译Wiki-Large**（Translated Wiki-Large）：使用翻译的 Wiki-Large 数据集训练的 BART-base 文本简化模型生成的测试结果；
- **跨语言伪数据**（Cross-Lingual Pseudo Data）： 用构造的数据训练 BART-Base 模型生成的测试结果。

使用自动化评估工具计算的 SARI、BLEU、HSK-Level 结果如下表：

<!-- ![alt EvaluateResult](https://github.com/blcuicall/mcts/blob/main/images/result1-mod.png) -->

| Method                  | SARI ↑    | BLEU ↑   | L1-3 (%) ↑ | L7+ (%) ↓ |
|-------------------------|-----------|----------|------------|-----------|
| Source                  | 22.37     | 84.75    | 40.24      | 44.90     |
| Gold Reference          | 48.11     | 61.62    | 46.25      | 39.50     |
| Direct Back Translation | 40.37     | 48.72    | 39.19      | 45.44     |
| Translated Wiki-Large   | 28.30     | **82.20**   | 40.32      | 44.92     |
| Cross-Lingual Pseudo Data | 38.49   | 63.06    | 41.57      | 44.24     |
|gpt-3.5-turbo-few-shot   | **43.95**   | 56.46    | **44.44**  | **40.67** |
| gpt-3.5-turbo           | 42.39     | 49.22    | 43.68      | 41.29     |
| text-davinci-003        | 37.97     | 36.18    | 38.80      | 45.32     |

对其中表现较好的几种代表性方法，我们聘请语言学背景的同学，从流利性、语义完整性和简单性三个方面，进行了人工评估。评估结果如下：

<!-- ![alt EvaluateResult2](https://github.com/blcuicall/mcts/blob/main/images/result2-mod.png) -->

| Method                  | Simplicity ↑     | Fluency ↑        | Adequacy ↑       | Avg. ↑          | Rank ↓         |
|-------------------------|------------------|------------------|------------------|-----------------|----------------|
| Direct Back Translation | 3.42 ±0.87       | 4.36 ±0.78       | **4.72** ±0.56   | 4.17            | 2.88           |
| Cross-Lingual Pseudo Data | 4.11 ±0.81     | 4.46 ±0.65       | 3.88 ±0.96       | 4.15            | 2.86           |
| gpt-3.5-turbo           | 4.17 ±0.89       | 4.46 ±0.70       | 4.43 ±0.78       | 4.35            | 2.29           |
| Gold Reference          | **4.20** ±1.08   | **4.68** ±0.55   | 4.31 ±0.93       | **4.40**        | **1.97**       |


MCTS数据集中的人工简化参考 (Gold Reference) 在人工评估中获得了最好的平均分数和排名，明显优于简化系统的输出结果。

## 作者

如果您有任何问题，或对我们的相关研究感兴趣，欢迎联系我们！

崇瑞宁：（chongruining@outlook.com）

鲁鹿鸣：（lulm410402@foxmail.com）

欢迎关注[**BLCU-ICALL研究组**](< https://blcuicall.org >)的主页和最新动态！

## 引用

如果使用了 MCTS 数据集，请您引用：

```
@inproceedings{chong-etal-2024-mcts-multi,
    title = "{MCTS}: A Multi-Reference {C}hinese Text Simplification Dataset",
    author = "Chong Ruining and Lu Luming and Yang Liner and Nie Jinran and Liu Zhenghao and Wang Shuo and Zhou Shuhan and Li Yaoxin and Yang Erhong",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italy",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.969",
    pages = "11111--11122",
}
@misc{kong-acl-2022-simpdefiner,
      title={Multitasking Framework for Unsupversied Simple Definition Generation}, 
      author={Cunliang Kong and Yun Chen and Hengyuan Zhang and Liner Yang and Erhong Yang},
      booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},     
      year={2022}
}
```
