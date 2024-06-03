#! /bin/bash
set -e

model_path=$1
phase=$2

cat ${model_path}/${phase}.log \
    | grep ^H \
    | sed 's/^..//' \
    | sort -n \
    | cut -f 3 \
    | sed -r 's/ ##//g' \
    | sed -r 's/ //g' \
    | sed -r 's/\[UNK\]//g' \
    > ${model_path}/${phase}.hyp.trg
