#!/usr/bin/env python3

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

os.mkdir(os.path.join(os.getcwd(),'cache'))

model_name = "lvwerra/distilbert-imdb"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
torch.save(model, './saved-model/model.pt')
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained('./saved_model/')

