#coding:utf-8
import pattern_check as pc
file_two_gram="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability.txt"
with open(file_two_gram,'r') as f:
    lines=f.readlines()
two_gram_dict={}
i=0
for line in lines:
    if i==0:
        i=1
        continue
    tokens = line.strip().split('\t')
    two_gram_dict[tokens[0]] = float(tokens[1])
    print tokens[0]

s="a5005a"
s_d="a5"
if s_d in two_gram_dict:
    print s_d
probably=1.0
for i in range(len(s)-1):
    s_temp = ""
    s_temp=s[i]+s[i+1]
    # print s_temp
    if s_temp in two_gram_dict:
        print two_gram_dict[s_temp],s_temp,len(s)
        probably*=two_gram_dict[s_temp]
print  probably
print pc.probably_s(s)
a='a'
print a.isalpha()