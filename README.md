# CSIE5431-2022-Spring-ADL-HW2

download pretrained models for to model/
```
bash ./download.sh
```
run prediction on data:
```
bash ./run.sh /path/to/context.json /path/to/test.json  /path/to/pred/prediction.csv
```
## train models:

multiple choice:
```
!python3 run_swag.py --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
--do_train --do_eval \
--context_file /path/to/context.json \
--train_file /path/to/train.json \
--validation_file /path/to/valid.json \
--cache_dir /cache \
--learning_rate 3e-5 \
--num_train_epochs 1 \
--max_seq_length 384 \
--output_dir model/context/ \
--per_gpu_eval_batch_size=1 \
--per_device_train_batch_size=1 \
--gradient_accumulation_steps 2 \
--load_best_model_at_end True \
--metric_for_best_model eval_accuracy \
--evaluation_strategy steps \
--overwrite_output \
--save_total_limit 5
```
QA:
```
!python3 run_swag.py --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
--do_train \
--do_eval \
--context_file /path/to/context.json \
--train_file /path/to/train.json \
--validation_file /path/to/valid.json \
--cache_dir /cache \
--learning_rate 3e-5 \
--num_train_epochs 2 \
--max_seq_length 384 \
--output_dir model/qa/ \
--per_gpu_eval_batch_size=1 \
--per_device_train_batch_size=1 \
--gradient_accumulation_steps 2 \
--overwrite_output \
--load_best_model_at_end True \
--metric_for_best_model eval_accuracy \
--evaluation_strategy steps \
--save_total_limit 5
```
