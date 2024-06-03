## Installation

- pytorch >= 1.8.0
- fariseq (git reset --hard 06c65c82973969)
- transformers >= 4.7.0
- apex (optional)

## Pretrained Models

Place the pretrained model to `pretrained-models/` directory. The models we use are: 

- bart-base-chinese: https://huggingface.co/fnlp/bart-base-chinese
- bart-large-chinese: https://huggingface.co/fnlp/bart-large-chinese

## Data Preprocess

The training and validation data should be processed into `.src` and `.tgt` files respectively and placed in the `data/raw` directory with the following directory structure:

```
- data
  - raw
    - train.src
    - train.tgt
    - valid.src
    - valid.tgt
```
The, run the `data_process.sh` for data preprocessing and put the preprocessed data in `data/raw/processed`.

## Train, inference and Evaluation

### Train
- use `train.sh`.
```shell
sh train.sh
``` 
### Inference
- Before the inference, you need to BPE the `.src` data first, and the BPEed data can be put in `data/bpe`.
- To bpe, you can refer to the following script:
```shell
 python bpe.py --input-file ./data/raw/test.src --output-file ./data/bpe/test.src --load-dir ./pretrained-models/bart-base-chinese
```
- To inference, use `interactive.sh`. Usage:
```shell
 sh interactive.sh [checkpoints_folder] test # This means inference on test set.   
```

- Once the inference is complete, you need to use `get_result.sh` to extract the simplified results from the inference log. Example:
```shell
sh get_results.sh [checkpoints_folder] [test_dataset_name]
```

### Evaluate 
 Use EASSE to evaluate the SARI and BLEU scores. Example script:

 ```shell
 easse report -t custom --refs_sents_paths "test/refs/ref_0_tokened.txt,test/refs/ref_2_tokened.txt,test/refs/ref_3_tokened.txt,test/refs/ref_4_tokened.txt,test/refs/ref_5_tokened.txt" --  orig_sents_path "test/test.src.tok" --sys_sents_path $1 -m "sari,bleu" -p "reports/report.html" 
 ```

<!-- 生成评价 `score-test.sh` 和 `score-valid.sh` 两个脚本 -->
