#!/usr/bin/env python3

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

os.mkdir(os.path.join(os.getcwd(),'cache'))

model = AutoModelForSequenceClassification.from_pretrained("fabriceyhc/bert-base-uncased-imdb")
torch.save(model, './saved-model/model.pt')
tokenizer = AutoTokenizer.from_pretrained("fabriceyhc/bert-base-uncased-imdb")
tokenizer.save_pretrained('./saved_model/')

