import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import  pickle
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import process as p
from sklearn.externals import joblib
import scipy as sp
from scipy.sparse import hstack

def processing(url):
    
    tokens_slash = str(url.encode('utf-8')).split('/')# make tokens after splitting by slash
    total_Tokens = []
    for i in tokens_slash:
        tokens = str(i).split('-')# make tokens after splitting by dash
        tokens_dot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')# make tokens after splitting by dot
            tokens_dot = tokens_dot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tokens_dot
    finaltest = list(set(total_Tokens))#remove redundant tokens
    return finaltest 


rfc = joblib.load("randomforestfinal.pkl")
vectorizer = joblib.load("vectorizer.pkl")
testapi = vectorizer.transform(["https://web.whatsapp.com"])
n = p.feature_processing("https://web.whatsapp.com")
n = sp.sparse.csr_matrix(n)
t = hstack([testapi,n])
print(rfc.predict(t))