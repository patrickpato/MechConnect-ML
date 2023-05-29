from fastapi import FastAPI 
from pydantic import BaseModel
import joblib
import pandas as pd 
import pickle
import numpy as np

app = FastAPI() 
model = joblib.load("carDiagnosticPipeline.sav")
#Text cleaning
def load_stopwords(stopwords_file):
  with open(stopwords_file, "r", encoding="utf-8") as f:
    stopwords = f.readlines()
    stop_set = set(m.strip() for m in stopwords)
    return list(frozenset(stop_set))
stopwords = load_stopwords("stopwords.txt")

class Prompt(BaseModel):
    carPrompt: str
    
# Receives prompts and returns potential problems
@app.post("/get_preds")
def returnEndpoint(item:Prompt):
    prompt = item.carPrompt
    clean_prompt = ' '.join([word for word in prompt.lower().split() if word not in (stopwords)])
    pred_issue_probas = model.predict_proba([clean_prompt])
    top_issues = np.argsort(-pred_issue_probas, axis=1)[:, :3]
    top_issue = model.classes_[top_issues][0]
    
    return {top_issue[0],top_issue[1], top_issue[2]}


