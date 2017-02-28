#coding:utf-8
import pattern_check as pc
import string
file_cheat_flag_0_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_0_20160401_20160531.txt"
file_cheat_flag_1_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_1_20160401_20160531.txt"

str_isalpha=[]
str_isdigit=[]
str_islower=[]
str_isupper=[]
str_istitle=[]
str_isalnum=[]
str_is_num_alpha=[]
str_is_alpha_num=[]
str_other=[]
#统计首字母的案件概率
# first_alp={}
# first_alp_set=set()
# for i in range(10):
#     first_alp[str(i)]=[]
#     first_alp_set.add(str(i))
# for w in string.lowercase:
#     first_alp[w]=[]
#     first_alp_set.add(w)
with open(file_cheat_flag_1_no_repetition_data,'r') as f1:
    lines=f1.readlines()
flag=0
# flag_domain=0

i=0
for line in lines:

    line=line.strip().split('\t')
    str = ""
    flag_domain = 0
    i+=1
    if i==1:
        continue
    for v in line[0]:
        if flag_domain==0:
            if v=="@":
                flag_domain=1
            else:
                str+=v.lower()
    # str="hanfei3508"
    # print pc.is_alpha_num(str)
    # print line[0]
    if str.isalpha():
        str_isalpha.append(int(line[1]))
    elif str.isdigit():
        str_isdigit.append(int(line[1]))
    elif pc.is_num_alpha(str):
        str_is_num_alpha.append(int(line[1]))
    elif pc.is_alpha_num(str):
        str_is_alpha_num.append(int(line[1]))
    else:
        str_other.append(int(line[1]))
f1.close()
print "str_isalpha_rate:%f in cheat_flag=1"% (len(str_isalpha)*1.0/i)
print "str_isdigit_rate:%f in cheat_flag=1"% (len(str_isdigit)*1.0/i)
print "str_is_num_alpha_rate:%f in cheat_flag=1"% (len(str_is_num_alpha)*1.0/i)
print "str_is_alpha_num_rate:%f in cheat_flag=1"% (len(str_is_alpha_num)*1.0/i)
print "str_other_rate:%f in cheat_flag=1"% (len(str_other)*1.0/i)
with open(file_cheat_flag_0_no_repetition_data,'r') as f1:
    lines=f1.readlines()
flag=0
# flag_domain=0
i=0
for line in lines:
    line=line.strip().split('\t')
    str = ""
    flag_domain = 0
    i+=1
    if i==1:
        continue
    for v in line[0]:
        if flag_domain==0:
            if v=="@":
                flag_domain=1
            else:
                str+=v
    # print line[0]
    if str.isalpha():
        str_isalpha.append(int(line[1]))
    elif str.isdigit():
        str_isdigit.append(int(line[1]))
    elif pc.is_num_alpha(str):
        str_is_num_alpha.append(int(line[1]))
    elif pc.is_alpha_num(str):
        str_is_alpha_num.append(int(line[1]))
    else:
        str_other.append(int(line[1]))
if len(str_isalpha)!=0:
    print "cheat_rate in str_isalpha:",float(sum(str_isalpha)*1.0/len(str_isalpha))
    print "\tnum_str_isalpha:", len(str_isalpha)
else:
    print "cheat_rate in str_isalpha: 0"
if len(str_isdigit) != 0:
    print "cheat_rate in str_str_isdigit:", float(sum(str_isdigit)*1.0 / len(str_isdigit))
    print "\tnum_str_isdigit:",len(str_isdigit)
else:
    print "cheat_rate in str_str_isdigit: 0"
if len(str_is_num_alpha) != 0:
    print "cheat_rate in str_is_num_alpha:", float(sum(str_is_num_alpha)*1.0 /len(str_is_num_alpha))
    print "\tnum_str_is_num_alpha:", len(str_is_num_alpha)
else:
    print "cheat_rate in str_is_num_alpha: 0"
if len(str_is_alpha_num) != 0:
    print "cheat_rate in str_is_alpha_num:", float(sum(str_is_alpha_num)*1.0 /len(str_is_alpha_num))
    print "\tnum_str_is_alpha_num:", len(str_is_alpha_num)
else:
    print "cheat_rate in str_istitle: 0"
if len(str_other) != 0:
    print "cheat_rate in str_other:", float(sum(str_other)*1.0 / len(str_other))
    print "\tnum_str_str_other:", len(str_other)
else:
    print "cheat_rate in str_other: 0"



