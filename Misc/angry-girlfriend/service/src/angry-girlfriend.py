#!/usr/bin/env python3

import os
os.environ['HF_HOME'] = os.path.join(os.getcwd(),'cache')
os.environ['TRANSFORMERS_CACHE'] = os.path.join(os.getcwd(),'cache')

import torch
import sys
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import warnings
from decimal import Decimal, getcontext
import string


warnings.filterwarnings("ignore")


print('Be Patient. Loading girlfriend...\n')
sys.stdout.flush()

with open('positive-words.txt', 'r') as f:
  positive_words = f.read().split('\n')
with open('flag.txt', 'r') as f:
  flag = f.read().strip()
  
model = torch.load('./saved-model/model.pt')
tokenizer = AutoTokenizer.from_pretrained('./saved_model/', local_files_only=True)


def gf_response():
  try:
    text = input("YOU: ")
    sys.stdout.flush()
  except:
    print('failure')
    return 0
  
  STOP_WORDS = positive_words

  text_words = [word for word in text.split() if (word.lower().translate(str.maketrans('', '', string.punctuation))) not in STOP_WORDS]
  
  if len(text_words)<5:
    print("GF: That's all you have to say? I expected more from you.")
    return 0
  elif len(text_words)>20:
    print("GF: Stop talking. I don't need you to lecture me.")
    return 0
  
  new_text = ' '.join(text_words)
  inputs = tokenizer(new_text, return_tensors="pt")
  with torch.no_grad():
    logits = model(**inputs).logits
  probabilities = torch.nn.functional.softmax(logits, dim=-1)
  predicted_class_id = logits.argmax().item()

  if predicted_class_id == 0:
    print(f"GF: You're making me angrier...\n\tAnger Level={probabilities[0][0]}")
  elif Decimal(probabilities[0][1].item()) < Decimal(0.995):
    print(f"GF: That's not good enough!\n\tHappy Level={probabilities[0][1]}")
  else:
    print(flag)
    return 1
  
  return 0


response = 0

print("You made your girlfriend mad! Lucky for you, she's now willing to talk to you. Say something to make her happy again.\n\n")
sys.stdout.flush()

while response==0:
  response = gf_response()
  sys.stdout.flush()
