# -*- coding: utf-8 -*-
import time
import os
import scipy.interpolate
import scipy as sp
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
import scipy as sp
from sklearn import svm
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import math
from sklearn.metrics import precision_recall_curve
from sklearn import metrics
data = []
labels = []
start=time.clock()
print "start time:",time.asctime(time.localtime(time.time()))
print "reading data ..."
file_eigenvalue_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_eigenvalue_sample_20160401_20160531.txt"
i=0
with open(file_eigenvalue_data,'r') as f1:
    for line in f1:
        if i==0:
            i=1
            continue
        tokens = line.strip().split(' ')
        data.append([float(tk) for tk in tokens[:-1]])
        labels.append(tokens[-1])
x = np.array(data)
# x= pd.DataFrame(data)
labels = np.array(labels)

y = np.zeros(labels.shape)
y[labels == '1'] = 1
print y
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=1)
print "reading data is completed"
print "SVM classification starting ..."
''''' SVM '''''
# title for the plots
titles = ['LinearSVC (linear kernel)',
          'SVC with polynomial (degree 3) kernel',
          'SVC with RBF kernel',
          'SVC with Sigmoid kernel']
# clf_linear = svm.SVC(kernel='linear').fit(x, y)
# clf_poly = svm.SVC(C=1.5,kernel='poly', degree=3,class_weight='balanced').fit(x, y)
# clf= svm.SVC(C=0.1).fit(x_train, y_train )
# clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)
print x_train,y_train
file_mode="d:\\Users\\xw_zhang\\Desktop\\job\\data\\mode\\train_model_rbf_10.m"
if os.path.exists(file_mode)==False:
    clf=svm.SVC(C=1,class_weight="balanced").fit(x_train, y_train)
    # clf= svm.SVC(kernel='linear').fit(x, y)
    # clf = svm.SVC(C=1.5,kernel='poly', degree=3,class_weight='balanced').fit(x, y)
    # clf= svm.SVC(C=0.1).fit(x_train, y_train )
    # clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)

    joblib.dump(clf, file_mode)
clf=joblib.load(file_mode)
print "training data is completed"
# for i,clf in enumerate((clf_rbf,clf_poly)):
answer=clf.predict(x_test)
# for i in range(50):
#     print answer[i]
# plt.subplot(1, 2,1)
a=clf.decision_function(x_test)
b=[]
for i in range(len(a)):
    temp=1.0/(1+math.exp(-a[i]))
    b.append(temp)
y_scores=np.array(b)
test_precision, test_recall, thresholds = precision_recall_curve(y_test, y_scores)
# for cutoff in thresholds:
#     print "cutoff:",cutoff
#     tab1 = pd.crosstab(y_scores > cutoff, y_test)
#     print  tab1,'\n'
print "thresholds:",thresholds
print "Accuracy:",np.mean(answer == y_test)
test_fpr, test_tpr, thresholds = metrics.roc_curve(y_test, y_scores)
print "test_auc_score:", metrics.auc(test_fpr, test_tpr)


a=clf.decision_function(x)
b=[]
for i in range(len(a)):
    temp=1.0/(1+math.exp(-a[i]))
    b.append(temp)
y_scores=np.array(b)
train_precision, train_recall, thresholds = precision_recall_curve(y, y_scores)
train_fpr, train_tpr, thresholds = metrics.roc_curve(y, y_scores)
print "train_auc_score:", metrics.auc(train_fpr, train_tpr)

print "ploting curve ..."
plt.subplot(1,2,1)
plt.plot(test_fpr,test_tpr,'g-',train_fpr,train_tpr,'r-')
plt.xlabel("fpr")
plt.ylabel("tpr")


plt.subplot(1,2,2)
plt.plot(test_recall,test_precision,'g-',train_recall,train_precision,'r-')
plt.xlabel("recall")
plt.ylabel("precision")

# test_precision_smooth=[]
# plt.subplot(1,3,3)
# for i in np.arange(0,len(test_precision),0.1):
#     test_precision_smooth
# x_interp = np.linspace(0, np.pi, 10)
# y_interp = sp.interpolate.barycentric_interpolate(test_recall,test_precision,x_interp)
# plt.plot(x_interp, y_interp,'--')



y_test_num_precise=0
y_test_num_recall=0
answer_num_precise=0
answer_num_recall=0
for i in range(len(y_test)):
    if y_test[i]==1:
        y_test_num_recall+=1
        if answer[i]==1:
            answer_num_recall+=1
print "y_test_num_recall:",y_test_num_recall,"answer_num_recall",answer_num_recall
if y_test_num_recall!=0:
    print "recall:",float(answer_num_recall*1.0/y_test_num_recall)

for i in range(len(answer)):
    if answer[i]==1:
        answer_num_precise+=1
        if y_test[i]==1:
            y_test_num_precise+=1

print  "answer_num_precise",answer_num_precise,"y_test_num_precise",y_test_num_precise
if answer_num_precise!=0:
    print "precise:",float(y_test_num_precise*1.0/answer_num_precise)
end=time.clock()
print "using time:%f s"%(end-start)
plt.show()
