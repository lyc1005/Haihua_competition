#!/usr/bin/env python
# coding: utf-8

import json
import random

with open('train.json') as f1:
    traindata = json.load(f1)
    
with open('validation.json') as f2:
    testdata = json.load(f2)

random.seed(2021)
random.shuffle(traindata)

split_pt = int(len(traindata)*0.9)
trainset = traindata[:split_pt]
valset = traindata[split_pt:]

with open('train_1.json', 'w', encoding='utf-8') as f:
    json.dump(trainset, f, indent=2, ensure_ascii=False)

with open('dev_1.json', 'w', encoding='utf-8') as f:
    json.dump(valset, f, indent=2, ensure_ascii=False)

with open('test_1.json', 'w', encoding='utf-8') as f:
    json.dump(testdata, f, indent=2, ensure_ascii=False)
