python3 preprocess.py "${2}" test_context.json
python3 predict.py --model_name_or_path model/context/pytorch_model.bin \
--config_name model/context/config.json \
--pred_file test_qa.json \
--tokenizer_name model/context/ \
--max_seq_length 384 \
--context_file "${1}" --test_file test_context.json \
--output_dir model/context \
--per_gpu_eval_batch_size=1
python3 predict_qa.py --model_name_or_path model/qa/pytorch_model.bin \
--config_name model/qa/config.json \
--tokenizer_name model/qa/ \
--context_file "${1}" \
--test_file test_qa.json \
--pred_file "${3}" \
--do_predict \
--max_seq_length 384 \
--doc_stride 128 \
--output_dir model/qa/ \
--overwrite_output_dir