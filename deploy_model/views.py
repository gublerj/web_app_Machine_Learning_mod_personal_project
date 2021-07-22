from django.http import HttpResponse
from django.shortcuts import render
import joblib
import numpy as np

def home(request):
    return render(request, "home.html")

def result(request):

    cls = joblib.load("heart_model.sav")

    lis = []

    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trtbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalachh'])
    lis.append(request.GET['exng'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slp'])
    lis.append(request.GET['caa'])
    lis.append(request.GET['thall'])

    
    # ans = cls.predict([lis])
    # change the threshold to make a more accurate prediction
    THRESHOLD = 0.04
    ans = np.where(cls.predict_proba([lis])[:,1] > THRESHOLD, 1, 0)
    ans_prob = cls.predict_proba([lis])[:,1]

    return render(request,"result.html", {'ans':ans, 'ans_prob':ans_prob, 'lis':lis})