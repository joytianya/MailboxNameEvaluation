#coding:utf-8
import time
import calculate_iv
import numpy as np
import pandas as pd
start=time.clock()
print "reading data ..."
file_eigenvalue="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no" \
                "_repetiton_eigenvalue_sample_20160401_20160531.txt"
eigenvalue=[]
with open(file_eigenvalue,'r') as f:
    lines=f.readlines()
i=0
vocab=[]
for line in lines:

    line=line.strip().split(' ')
    if i==0:
        i=1
        vocab.append([v for v in line])
    else:
        eigenvalue.append([float(v) for v in line])
eigenvalue=np.array(eigenvalue)
eigenvalue_t=eigenvalue.T
print "reading data is completed"
print "calculating iv ..."
# print len(eigenvalue[0]),eigenvalue_t[75]
var_iv=[]
# print eigenvalue_t[len(eigenvalue_t)-1]
# print eigenvalue_t[0]
# print len(eigenvalue_t)-1
for i in range(len(eigenvalue_t)-1):
    var_iv.append(calculate_iv.info_val(eigenvalue_t[len(eigenvalue_t)-1],pd.Series(eigenvalue_t[i]),10))
for i in range(len(var_iv)):
    print vocab[0][i],var_iv[i]
# print len(var_iv),len(vocab[0])
end=time.clock()
print "used time:%f s"%(end-start)