# -*- coding: utf-8 -*-


import torch
import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')



# Summarized output from above ::::::::::
# the us has over 637,000 confirmed Covid-19 cases and over 30,826 deaths. 
# president Donald Trump predicts some states will reopen the country in april, he said. 
# "we'll be the comeback kids, all of us," the president says.

import pandas as pd
def generate_summary():
  df = pd.read_csv("livemint.csv")

  yello = []
  for text,title in zip(df['text'],df['title']):
    if len(text.split())<=100 : 
      yello.append(text)
    else:
      preprocess_text = text.strip().replace("\n","")
      t5_prepared_Text = "summarize: "+preprocess_text
      print ("original text preprocessed: \n", preprocess_text)

      tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


      # summmarize 
      summary_ids = model.generate(tokenized_text,
                                          num_beams=4,
                                          no_repeat_ngram_size=2,
                                          min_length=30,
                                          max_length=100,
                                          early_stopping=True)

      output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

      print ("\n\nSummarized text: \n",output)
      yello.append((title,text,output))
  return yello
 


