from flask import Flask, request, jsonify , render_template
import pickle
import  process as p
from sklearn.externals import joblib
import scipy as sp
from scipy.sparse import hstack

app = Flask(__name__)
rfc = joblib.load("randomforestfinal.pkl")

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

vectorizer = joblib.load("vectorizer.pkl")

@app.route('/',methods=['GET'])
def main():
    return render_template('index.html',websitename="Maltracker");

@app.route('/api',methods=['GET'])
def predict():
    params = request.args.get('url')
    testapi = vectorizer.transform([params])
    n = p.feature_processing(params)
    n = sp.sparse.csr_matrix(n)
    t = hstack([testapi,n])
    data = rfc.predict(t);
    return  jsonify(status=(data[0]))

if __name__ == '__main__':
   app.run()