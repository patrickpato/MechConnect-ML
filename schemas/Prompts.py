import joblib
import numpy as np 
model = joblib.load("carDiagnosticPipeline.sav")
#Text cleaning
def load_stopwords(stopwords_file):
  with open(stopwords_file, "r", encoding="utf-8") as f:
    stopwords = f.readlines()
    stop_set = set(m.strip() for m in stopwords)
    return list(frozenset(stop_set))
stopwords = load_stopwords("stopwords.txt") 

def userPrompt(item) -> dict:
    clean_prompt = ' '.join([word for word in item["prompt"].lower().split() if word not in (stopwords)])
    pred_issue_probas = model.predict_proba([clean_prompt])
    top_issues = np.argsort(-pred_issue_probas, axis=1)[:, :3]
    least_likely = model.classes_[top_issues][0][0]
    likely = model.classes_[top_issues][0][1]
    most_likely = model.classes_[top_issues][0][2]
    return {
        "id":str(item["_id"]), 
        "prompt":item["prompt"], 
        "predictedIssue":[least_likely, likely, most_likely], 
        "actualIssue":item["actualIssue"]
    }
def usersPrompts(entity) -> list:
    return [userPrompt(item) for item in entity]