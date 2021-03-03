# Haihua_competition

Baseline code for Haihua 2021 AI competition

Competition Link:
1. https://www.biendata.xyz/competition/haihua_2021/ (Profession Group)
2. https://www.biendata.xyz/competition/haihua2021_k12/ (Student Group)

How to use the baseline:

1. Install required packages 
```
pip install requirements.txt
```

2. Download competition data from Biendata websites, move the `train.json` and `validation.json` into the same directory as the codes, then run following codes for training
```
python preprocessing.py

python run_base.py --task_name rc --do_train --do_eval --data_dir . --init_checkpoint hfl/chinese-bert-wwm-ext --max_seq_length 512 --train_batch_size 16 --eval_batch_size 8 --learning_rate 1e-5 --num_train_epochs 5 --output_dir mrc_bert --gradient_accumulation_steps 8
```

After finishing running, there would be a `test_output.csv` in your output folder for you to submit.
