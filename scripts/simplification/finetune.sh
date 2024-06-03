#! /bin/zsh

export CUDA_VISIBLE_DEVICES=0,1,2

DATA_DIR=data-ft/processed
BART_DIR=pretrained-models/bart-large-chinese
CKPT=checkpoints/simp-small-bart-large-0305/checkpoint_best_unft.pt
MODEL_NAME=simp-small-bart-large-ft-0309
mkdir -p checkpoints/$MODEL_NAME

python train.py $DATA_DIR \
    --fp16 \
    --seed 42 \
    --user-dir bart-zh \
    --arch hf_bart \
    --task translation_hf_bart \
    --hf-model-name $BART_DIR \
    --optimizer adam \
    --clip-norm 0.1 \
    --lr 1e-5 \
    --lr-scheduler inverse_sqrt \
    --warmup-updates 100 \
    --criterion label_smoothed_cross_entropy \
    --label-smoothing 0.1 \
    --update-freq 4 \
    --max-tokens 2048 \
    --max-epoch 25 \
    --num-workers 10 \
    --save-dir checkpoints/$MODEL_NAME \
    --restore-file $CKPT \
    --log-format simple \
    --log-interval 50 \
    --left-pad-source \
    2>&1 | tee -a checkpoints/$MODEL_NAME/training.log
