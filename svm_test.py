#coding:utf-8
import time
from sklearn import svm
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import math
from sklearn import metrics

localtime = time.asctime( time.localtime(time.time()))
print "本地时间为 :", localtime
start=time.clock()
# print"start time:",start
print "reading data ..."
file_verification="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no" \
                     "_repetiton_eigenvalue_sample_20160601_20160701_fraud_flag.txt"
with open(file_verification,'r') as f1:
    lines=f1.readlines()
data=[]
labels=[]
y_fraud=[]
i=0
for line in lines:
    tokens=line.strip().split(' ')
    if i==0:
        i=1
        continue
    data.append([float(tk) for tk in tokens[:-2]])
    y_fraud.append(float(tokens[-1]))
    labels.append(tokens[-2])
x_verification=np.array(data)
# x_verification = pd.DataFrame(data)

# x_verification =data
labels=np.array(labels)
y_fraud=np.array(y_fraud)
y_verification=np.zeros(labels.shape)
y_verification[labels=='1']=1
print "reading data is completed"
print "downing mode ..."
file_mode="d:\\Users\\xw_zhang\\Desktop\\job\\data\\mode\\train_model_rbf_10.m"
clf=joblib.load(file_mode)
print "downing mode is completed"
print "predicting data ..."
# answer=clf.predict(x_verification)
# answer=[]
# for i in range(x_verification):
#     answer.append(clf.predict([x_verification[i]]))
# print "prediction is completed"
# print"Accuracy:",(np.mean(answer == y_verification))
# print x_verification
# x_verification=[[0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0.0,2]]
# y_scores=clf.predict_proba(x_verification)
a=clf.decision_function(x_verification)
print "prediction is completed"
b=[]

for i in range(len(a)):
    temp=1.0/(1+math.exp(-a[i]))
    b.append(temp)
y_scores=np.array(b)
result=[]
result.append(y_scores)
result.append(y_verification)
result.append(y_fraud)
result=np.array(result)
result=result.T
file_result="d:\\Users\\xw_zhang\\Desktop\\job\\data\\result.txt"
with open(file_result,'w') as f:
    f.write('y_score'+'cheat_flag'+'fraud_flag')
    for i in range(len(result)):
        for v in result[i]:
            f.write(str(v)+' ')
        f.write('\n')
verification_precision, verification_recall, thresholds = precision_recall_curve(y_verification, y_scores)

print "thresholds:",thresholds
for cutoff in np.arange(0,1,0.01):
# cutoff =0.9984
    print "cutoff:",cutoff
    tab1 = pd.crosstab(y_scores > cutoff, y_verification)
    print  tab1,'\n'
print sum(y_fraud)
#
verification_fpr, verification_tpr, thresholds = metrics.roc_curve(y_verification, y_scores)
print "test_auc_score:", metrics.auc(verification_fpr, verification_tpr)
plt.subplot(1,2,1)
plt.plot(verification_fpr,verification_tpr,'g-')
plt.xlabel("fpr")
plt.ylabel("tpr")
plt.subplot(1,2,2)
plt.plot(verification_recall,verification_precision,'r-')
plt.xlabel("recall")
plt.ylabel("precision")
end=time.clock()
print "using time:%f s"%(end-start)
plt.show()
