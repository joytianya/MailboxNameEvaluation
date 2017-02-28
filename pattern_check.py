#coding:utf-8
file_two_gram_alp_num_no_1_sp="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph_num_no_1_sp.txt"
file_two_gram_alp_num_1_sp="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph_num_1_sp.txt"
file_two_gram_alp="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph.txt"
with open(file_two_gram_alp_num_no_1_sp,'r') as f:
    lines=f.readlines()
two_gram_alp_num_no_1_sp_dict={}
i=0
for line in lines:
    if i==0:
        i=1
        continue
    tokens = line.strip().split('\t')
    two_gram_alp_num_no_1_sp_dict[tokens[0]] = float(tokens[1])
f.close()
with open(file_two_gram_alp_num_1_sp,'r') as f:
    lines=f.readlines()
two_gram_alp_num_1_sp_dict={}
i=0
for line in lines:
    if i==0:
        i=1
        continue
    tokens = line.strip().split('\t')
    two_gram_alp_num_1_sp_dict[tokens[0]] = float(tokens[1])
f.close()
with open(file_two_gram_alp,'r') as f:
    lines=f.readlines()
two_gram_alp_dict={}
i=0
for line in lines:
    if i==0:
        i=1
        continue
    tokens = line.strip().split('\t')
    two_gram_alp_dict[tokens[0]] = float(tokens[1])
f.close()
def is_alpha_num(s):
    if s[0]>'z' or s[0]<'a':
        return 0
    alp=""
    num=""
    flag=0
    flag_0=0
    flag_1=0
    for i in range(len(s)):
        if flag==0:
            if s[i]<='z' and s[i]>='a':
                alp+=s[i]
            elif s[i]<='9' and s[i]>='0':
                flag=1
                num+=s[i]
            else:
                flag_0=1
                break

        else:
            if s[i] <= '9' and s[i] >= '0':
                num+=s[i]
            else:
                flag_0 = 1
                break
    if len(num)>0 and flag_0!=1 :

        return 1
    else:
        return 0
def is_num_alpha(s):
    if s[0]>'9' or s[0]<'0':
        return 0
    alp=""
    num=""
    flag=0
    flag_0=0
    flag_1=0
    for i in range(len(s)):
        if flag==0:
            if s[i]<='z' and s[i]>='a':
                flag = 1
                alp+=s[i]
            elif s[i]<='9' and s[i]>='0':

                num+=s[i]
            else:
                flag_0=1
                break

        else:
            if s[i] <= 'z' and s[i] >= 'a':
                num+=s[i]
            else:
                flag_0 = 1
                break
    if len(alp)>0 and flag_0!=1 :

        return 1
    else:
        return 0
def count_change(s):
    count=0
    if s.isalnum():
        for i in range(len(s)-1):
            if s[i]<='z' and s[i]>='a' and s[i+1]<='9' and s[i+1]>='0':
                count+=1
            if s[i]<='9' and s[i]>='0' and s[i+1]<='z' and s[i+1]>='a':
                count+=1
    return count
def probably_alp_num_no_1_sp_s(s):

    probably=1.0
    flag=0
    for i in range(len(s)-1):
        s_temp = ""
        if s[i]>='0' and s[i]<='9':
            name_s='0'
        else:
            name_s=s[i]
        if s[i+1]>='0' and s[i+1]<='9':
            name_e='0'
        else:
            name_e=s[i+1]
        s_temp=name_s+name_e
        if s_temp in two_gram_alp_num_no_1_sp_dict:
            flag=1
            probably*=two_gram_alp_num_no_1_sp_dict[s_temp]
    if len(s)==1 or flag==0:
       return 0
    return probably
def probably_alp_num_1_sp_s(s):

    probably=1.0
    flag=0
    for i in range(len(s)-1):
        s_temp = ""
        if s[i]>='0' and s[i]<='9':
            name_s='0'
        else:
            name_s=s[i]
        if s[i+1]>='0' and s[i+1]<='9':
            name_e='0'
        else:
            name_e=s[i+1]
        s_temp=name_s+name_e
        if s_temp in two_gram_alp_num_1_sp_dict:
            flag=1
            probably*=two_gram_alp_num_1_sp_dict[s_temp]
    if len(s)==1 or flag==0:
       return 0
    return probably
def probably_alp_s(s):

    probably=1.0
    flag=0
    name_s=''
    name_e=''
    for i in range(len(s)-1):
        s_temp = ""

        # print i,len(s)
        if name_s == '' or name_s == '0':
            if s[i]<'a' or s[i]>'z':
                name_s='0'
            else:
                name_s=s[i]
        # if name_e == '' or name_e == '0':
        # print len(s)
        if s[i+1]<'a' or s[i+1]>'z':
            name_e='0'
        else:
            name_e=s[i+1]

        if name_s!='0' and name_e!='0':
            s_temp=name_s+name_e
            name_s=''
            name_e =''
        if s_temp in two_gram_alp_dict:
            flag=1
            probably*=two_gram_alp_dict[s_temp]
    if len(s)==1 or flag==0:
       return 0
    return probably
