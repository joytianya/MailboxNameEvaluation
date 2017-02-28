import math
import codecs
import string
file_cheat_flag_0_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_0_20160401_20160531.txt"
with codecs.open(file_cheat_flag_0_no_repetition_data,'r') as f:
    lines=f.readlines()
list_comb=[]
s=""

x_list=string.lowercase
for i in range(10):
    x_list+=str(i)
x_list+='.'
x_list+='_'
x_list+='-'
y_list=x_list
for x in x_list:
    for y in y_list:
        s=x+y
        list_comb.append(s)
list_comb_set=set(list_comb)
two_gram=[]
for line in lines:
    tokens=line.strip().split("\t")
    s=""
    name=tokens[0].split('@')
    name[0]=name[0].lower()
    name_s=''
    name_e=''
    for i in range(len(name[0])-1):
        # if name_s=='' or name_s=='0':
        if name[0][i]>='0'and name[0][i]<='9':
            name_s='0'
        else:
            name_s = name[0][i]
        # if name_e=='' or name_e=='0':
        if name[0][i+1]>='0'and name[0][i+1]<='9':
            name_e='0'
        else:
            name_e = name[0][i + 1]
        # if name_s!='0' and name_e!='0':

        s=name_s+name_e
        if s in list_comb_set :
            two_gram.append(s)
            # name_s=''
            # name_e=''
            # print s,name[0]
            # two_gram.append(s)
# file_temp= "d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_list.txt"
# with open(file_temp,'w') as f:
#     for m in two_gram:
#           f.write(m+'\n')
#

two_gram_set=set(two_gram)
two_gram_dict={}
two_gram_list=list(two_gram_set)
for v in two_gram_set:
    # print v
    two_gram_dict[v]=0
for v in two_gram:
    two_gram_dict[v]+=1
for k in two_gram_dict.keys():
    two_gram_dict[k]=(two_gram_dict[k]*0.1/len(two_gram))*pow(10,1)
# for k in two_gram_dict.keys():
#
#     if k[0].isdigit() and k[1].isalpha():
#         two_gram_dict[k]=1.0
#     if k[1].isdigit() and k[0].isalpha():
#         two_gram_dict[k]=1.0
#     if k.isdigit():
#         two_gram_dict[k]=1.0

file_two_gram="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph_num_no_1_sp.txt"
with codecs.open(file_two_gram,'w') as f:
    f.write('two_gram_name'+'\t'+'probability'+'\n')
    for k in two_gram_dict.keys():
        f.write(k+'\t'+str(two_gram_dict[k])+'\n')

for k in two_gram_dict.keys():
    if two_gram_dict[k]>=1.0:
        print len(two_gram_set),two_gram_dict[k],k

# print two_gram_dict['0k']
list_comb=[]
s=""

x_list=string.lowercase
# for i in range(10):
#     x_list+=str(i)
y_list=x_list
for x in x_list:
    for y in y_list:
        s=x+y
        list_comb.append(s)
list_comb_set=set(list_comb)
two_gram=[]
for line in lines:
    tokens=line.strip().split("\t")
    s=""
    name=tokens[0].split('@')
    name[0]=name[0].lower()
    name_s=''
    name_e=''
    for i in range(len(name[0])-1):
        if name_s=='' or name_s=='0':
            if name[0][i]<'a'or name[0][i]>'z':
                name_s='0'
            else:
                name_s = name[0][i]
        # if name_e=='' or name_e=='0':
        if name[0][i+1]<'a'or  name[0][i+1]>'z':
            name_e='0'
        else:
            name_e = name[0][i + 1]
        if name_s!='0' and name_e!='0':
            s=name_s+name_e
            if s in list_comb_set :
                two_gram.append(s)
            name_s=''
            name_e=''
            # print s,name[0]
            # two_gram.append(s)
# file_temp= "d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_list.tx
# with open(file_temp,'w') as f:
#     for m in two_gram:
#           f.write(m+'\n')
#

two_gram_set=set(two_gram)
two_gram_dict={}
two_gram_list=list(two_gram_set)
for v in two_gram_set:
    # print v
    two_gram_dict[v]=0
for v in two_gram:
    two_gram_dict[v]+=1
for k in two_gram_dict.keys():
    two_gram_dict[k]=(two_gram_dict[k]*0.1/len(two_gram))*pow(10,1)
# for k in two_gram_dict.keys():
#
#     if k[0].isdigit() and k[1].isalpha():
#         two_gram_dict[k]=1.0
#     if k[1].isdigit() and k[0].isalpha():
#         two_gram_dict[k]=1.0
#     if k.isdigit():
#         two_gram_dict[k]=1.0

file_two_gram="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph.txt"
with codecs.open(file_two_gram,'w') as f:
    f.write('two_gram_name'+'\t'+'probability'+'\n')
    for k in two_gram_dict.keys():
        f.write(k+'\t'+str(two_gram_dict[k])+'\n')
list_comb=[]
s=""

x_list=string.lowercase
for i in range(10):
    x_list+=str(i)
x_list+='.'
x_list+='_'
x_list+='-'
y_list=x_list
for x in x_list:
    for y in y_list:
        s=x+y
        list_comb.append(s)
list_comb_set=set(list_comb)
two_gram=[]
for line in lines:
    tokens=line.strip().split("\t")
    s=""
    name=tokens[0].split('@')
    name[0]=name[0].lower()
    name_s=''
    name_e=''
    for i in range(len(name[0])-1):
        # if name_s=='' or name_s=='0':
        if name[0][i]>='0'and name[0][i]<='9':
            name_s='0'
        else:
            name_s = name[0][i]
        # if name_e=='' or name_e=='0':
        if name[0][i+1]>='0'and name[0][i+1]<='9':
            name_e='0'
        else:
            name_e = name[0][i + 1]
        # if name_s!='0' and name_e!='0':
        s=name_s+name_e
        if s in list_comb_set :
            two_gram.append(s)
            name_s=''
            name_e=''
            # print s,name[0]
            # two_gram.append(s)
# file_temp= "d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_list.tx
# with open(file_temp,'w') as f:
#     for m in two_gram:
#           f.write(m+'\n')
#

two_gram_set=set(two_gram)
two_gram_dict={}
two_gram_list=list(two_gram_set)
for v in two_gram_set:
    # print v
    two_gram_dict[v]=0
for v in two_gram:
    two_gram_dict[v]+=1
for k in two_gram_dict.keys():
    two_gram_dict[k]=(two_gram_dict[k]*0.1/len(two_gram))*pow(10,1)
for k in two_gram_dict.keys():
    if k.isdigit():
        two_gram_dict[k]=1.0

file_two_gram="d:\\Users\\xw_zhang\\Desktop\\job\\data\\two_gram_probability_alph_num_1_sp.txt"
with codecs.open(file_two_gram,'w') as f:
    f.write('two_gram_name'+'\t'+'probability'+'\n')
    for k in two_gram_dict.keys():
        f.write(k+'\t'+str(two_gram_dict[k])+'\n')