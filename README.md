# CSIE5431-2022-Spring-ADL-HW2

download pretrained models for to model/
```
bash ./download.sh
```
run prediction on data:
```
bash ./run.sh /path/to/input.jsonl /path/to/output.jsonl
```
## train models:
```
python3 run_summarization.py \
    --model_name_or_path google/mt5-small \
    --train_file /path/to/train.jsonl \
    --validation_file /path/to/validation.jsonl \
    --do_train \
    --do_eval \
    --text_column "maintext" \
    --summary_column "title" \
    --source_prefix "summarize: " \
    --learning_rate 5e-4 \
    --num_train_epochs 3 \
    --output_dir /path/to/output_dir \
    --per_device_train_batch_size=4 \
    --gradient_accumulation_steps 2 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate \
    --load_best_model_at_end True \
    --metric_for_best_model eval_loss \
    --evaluation_strategy steps \
    --save_total_limit 5
```
