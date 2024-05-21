# MCTS: A Multi-Reference Chinese Text Simplification Dataset
<div align="center">

 [Chinese version](https://github.com/blcuicall/mcts/blob/main/README-zh.md)

</div>

## ✨ Overview

This repository contains the official dataset and scripts of our LREC-COLING 2024 paper: **[MCTS: Multi-Reference Chinese Text Simplification Dataset](< https://aclanthology.org/2024.lrec-main.969 >)**

The task of text simplification is one of the fundamental tasks in the field of natural language processing, aiming to make the text easier to understand by performing multiple rewriting transformations. Text Simplification can help research on graded reading, machine translation, and help language learners understand complex texts.  Currently, there are fewer studies on Chinese text simplification, and the lack of generalized evaluation data is one of the important reasons. For this reason, we constructed the **MCTS (Multi-Reference Chinese Text Simplification Dataset)**, the first published dataset on the Chinese Text Simplification Task. It is the largest evaluation dataset on the Chinese text simplification task so far and has the most number of references. This is a foundational piece of work in our exploration of Chinese text simplification, and we expect it to inform future research.

Paper address: [https://aclanthology.org/2024.lrec-main.969](< https://aclanthology.org/2024.lrec-main.969 >)

### Data Scale

MCTS is the largest evaluation dataset on the Chinese text simplification task and has the most number of references, including 723 complex-structured sentences selected from the news corpus, each of which contains multiple manually simplified sentences respectively. 

### Data Format

All data files are in plain text format. Each line in the file is a instance.

The contents of a file are distinguished by naming. The name of a file consists of three parts: *prefix*, a *infix*, and a *suffix*. The naming format is:

```
prefix.infix.suffix（.num）
```

All files have the same prefix ``mcts``. Files with the infix ``test`` means the test set, while the infix ``dev`` means dev set.

Files with the suffix ``orig`` are unsimplified source sentence files. The five reference files simplified by the annotator are suffixed ``simp``, followed by the ``num``. For source files and reference files with the same suffix, the sentences in them correspond to each other on a line-by-line basis.

### Data Example

<!-- ![alt DataExample](https://github.com/blcuicall/mcts/blob/main/images/exp.png) -->
| Original | Reference |
|----------|-----------|
| 为适应大西南进出口物资迅速增长的需要，北部湾沿海四市开始了新一轮建港热潮。<br> In order to adapt to the rapid growth of import and export materials in the southwest, four coastal cities in the Beibu Gulf have started a new wave of port construction. | 大西南进口和出口物资的需要迅速增长，北部湾沿海四座城市兴起了新一轮港口建设。<br> The demand for imported and exported materials in the southwest has grown rapidly. Four coastal cities in the Beibu Gulf have begun a new round of port construction.  |
| 中国又一条煤炭运输大通道──连接天津蓟县与天津港之间的蓟港铁路日前破土动工。<br>Another major coal transportation corridor in China - the Jigang Railway connecting Tianjin Jixian County and Tianjin Port - has recently broken ground. | 蓟港铁路连接天津蓟县和天津港，用于煤炭运输，前几天开始建造。<br>Jigang Railway connects Tianjin Jixian County and Tianjin Port for coal transportation, and construction began a few days ago.  | 
| 按设计，“进步M-24”号载重飞船可同轨道站在无人操纵的情况下进行自动对接。<br>According to the design, the "Progress M-24" heavy-duty spacecraft can automatically dock with the orbital station under unmanned control. | 按照设计，无人操控的“进步M-24”号飞船可以自动对接轨道站。<br>According to the design, the unmanned "Progress M-24" spacecraft can automatically dock with the orbital station. |

### Evaluation Metrics

We use the automated metrics SARI and BLEU provided by [EASSE](https://github.com/feralvam/easse) , and the HSK-Level provided by Kong et al. in their paper [*Multitasking framework for unsupervised simple definition generation*](https://arxiv.org/abs/2203.12926).

*Note: If you are using the EASSE package for evaluation, you should first TOKENIZE all test data.*

The script used to evaluate HSK-Level is placed in the ``script`` directory. For example, to evaluate the HSK-Level of the test set source file ``mcts.test.orig``, use the following command:

```sh
python scripts/hsk_evaluate.py dataset/mcts.test.orig
```

## 🛠️ Building Training Data

Due to the scarcity of massively parallel corpus, we use a combination of Machine Translation and English Text Simplification to build the training corpus. (See the paper for details)

![alt TrainingData](https://github.com/blcuicall/mcts/blob/main/images/pseudo_data.png)

After rigorous automatic screening, we finally obtained 691,474 high-quality parallel training data, which is by far the largest scale of available training data in the field of Chinese Text S0implification. We demonstrate the validity of the data through experiments. (See related experiments for details)

This data is placed in the ``pseudo_data`` directory, where ``zh_selected.ori`` is the complex sentences and ``zh_selected.sim`` is the simple sentences. 

## 📊 Text Features Analysis

We calculated several low-level features for all simplification examples to measure the rewriting transformations included in MCTS. Below is a statistical plot of the text features. (See paper for detailed data)

![alt result](https://github.com/blcuicall/mcts/blob/main/images/feature.png)

## 🧪 Related Experiments

We compared a variety of baseline methods, which included: 

- **OpenAI Models**: Test results using GPT-3.5-turbo and text-davinci-003 models, and a In-context few-shot test on GPT-3.5-turbo; 
- **Direct Back Translation**: Generated results of back translation performed by Google Translate;
- **Translated Wiki-Large**: Test results generated from the BART-base text simplification model trained on the translated Wiki-Large dataset;
- **Cross-Lingual Pseudo Data**: Test results generated by training the BART-Base model with the constructed pseudo data.

The SARI, BLEU, and HSK-Level results calculated using the automated evaluating tool are shown in the table below:

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



For several of these representative methods that performed well, we hired students with linguistic backgrounds to manually evaluate them in terms of fluency, semantic integrity and simplicity. The evaluation results are as follows:

<!-- ![alt EvaluateResult2](https://github.com/blcuicall/mcts/blob/main/images/result2-mod.png) -->

| Method                  | Simplicity ↑     | Fluency ↑        | Adequacy ↑       | Avg. ↑          | Rank ↓         |
|-------------------------|------------------|------------------|------------------|-----------------|----------------|
| Direct Back Translation | 3.42 ±0.87       | 4.36 ±0.78       | **4.72** ±0.56   | 4.17            | 2.88           |
| Cross-Lingual Pseudo Data | 4.11 ±0.81     | 4.46 ±0.65       | 3.88 ±0.96       | 4.15            | 2.86           |
| gpt-3.5-turbo           | 4.17 ±0.89       | 4.46 ±0.70       | 4.43 ±0.78       | 4.35            | 2.29           |
| Gold Reference          | **4.20** ±1.08   | **4.68** ±0.55   | 4.31 ±0.93       | **4.40**        | **1.97**       |


The human simplified reference (Gold Reference) in the MCTS dataset achieved the best average score and rank in the manual evaluation, significantly outperforming the output of the simplification system.

## Authors

If you have any questions or are interested in our related research, please contact us!

Ruining Chong (chongruining@outlook.com)

Luming Lu (lulm410402@foxmail.com)

Welcome to the homepage of our group [**BLCU-ICALL**](< https://blcuicall.org >) for the latest news!!

## Citation

If you use our MCTS dataset, please cite:

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
