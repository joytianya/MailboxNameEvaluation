#coding:utf-8
import os
import string
import pattern_check as pc
file_cheat_0="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_0_20160401_20160531.txt"
file_cheat_1="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_1_20160401_20160531.txt"
file_domain_rate="d:\\Users\\xw_zhang\\Desktop\\job\\data\\domain_rate_20160401_20160531.txt"
file_pattern_probability="d:\\Users\\xw_zhang\\Desktop\\job\\data\\pattern_probability.txt"
with open(file_pattern_probability,'r') as f1:
    lines=f1.readlines()
pattern_probability={}
for line in lines:
    tokens=line.strip().split('\t')
    pattern_probability[tokens[0]]=float(tokens[1])
    print tokens[0],tokens[1]
with open(file_domain_rate,'r') as f:
    lines=f.readlines()
i=0
domain_rate_dic={}
for line in lines:
    line=line.strip().split('\t')
    if i==0:
        i=1
        continue
    domain_rate_dic[line[0]]=float(line[1])

# vocabSet_domainList=[]
vocabList=[]
for i in range(10):
    vocabList.append(str(i))
    # vocabSet_domainList.append(str(i))
# print len(vocabList)
for w in string.lowercase:
    vocabList.append(w)
    # vocabSet_domainList.append(w)
other=['.','-','_']
vocabList.extend(other)
# vocabSet_domainList.extend(other)
vocabSet_domainList=vocabList
vocabList_set=set(vocabList)
vocabSet_domainList_set=set(vocabSet_domainList)
# print len(vocabList)
print "变量名：",vocabList
file_vocabList="d:\\Users\\xw_zhang\\Desktop\\job\\data\\vocabList.txt"
with open(file_vocabList,'w') as f1:
    for v in vocabList:
        f1.write(v+' ')

print "extracting eigenvalue ..."
BOW=[]
vec=[]
for i in range(len(vocabList)):
    vec.append("freq_"+str(vocabList[i]))
# print len(vocabList)
vec.append("domain_degree")
vec.append("name_degree")
vec.append("name_probability")
vec.append("num_change")
vec.append("length")
vec.append("prob_prefix_num_no_1")
vec.append("prob_prefix_num_1")
vec.append("prob_prefix_alp")
vec.append("lable")
# print len(vec)
BOW.append(vec)
# print len(BOW[0])
with open(file_cheat_0,'r') as f2:
    lines_nor=f2.readlines()
flag=0
# print len(vocabList),vocabList
for line_nor in lines_nor:
    # vec_l=[]

    vec=[0]*len(vocabList)

    line_nor=line_nor.split("\t")
    if flag==0:
        flag=1
        continue
    # print len(vec)
    name=line_nor[0].split('@')
    if len(name)==2:
        for v in name[0]:
            if v.lower() in vocabList_set:
                vec[vocabList.index(v.lower())] += 1
        # print name[1]
        # print len(vec),len(vocabList)

        if name[1] in domain_rate_dic:
            vec.append(domain_rate_dic[name[1]])
        else:
            vec.append(0)

        s = name[0].lower()
        # if s.isupper():
        #     print s
        # print s
        if s.isalpha():
            vec.append(0.0114)
            vec.append(pattern_probability["is_alpha"])
            # pattern_probability[]
            # vec =[item*1.1 for item in vec]
        elif s.isdigit():
            vec.append(0.0138)
            vec.append(pattern_probability["is_digit"])
            # vec =[item * 1.3 for item in vec]
        elif pc.is_num_alpha(s):
            vec.append( 0.004)
            vec.append(pattern_probability["is_num_alpha"])
            # vec =[item * 1.2 for item in vec]
        elif pc.is_alpha_num(s):
            vec.append(0.0161)
            vec.append(pattern_probability["is_alpha_num"])
            # vec =[item * 2.7 for item in vec]
        else:
            vec.append(0.0090)
            vec.append(pattern_probability["other"])
            # vec =[item * 1.1 for item in vec]
        vec.append(pc.count_change(s))
        vec.append(len(s))
        vec.append(pc.probably_alp_num_no_1_sp_s(s))
        vec.append(pc.probably_alp_num_1_sp_s(s))
        vec.append(pc.probably_alp_s(s))
        # if pc.probably_s(s)==1:
        #     print s,len(s)
        # for i in range(len(vec_l),30):
        #     vec_l.append(0)
        # vec=vec+vec_domain
        vec.append(line_nor[1].strip())
        # vec.append(line_nor[2].strip())
        # print len(vec)
        BOW.append(vec)
f2.close()
cheat_0_count=len(BOW)


flag=0
with open(file_cheat_1,'r') as f3:
    for line in f3.readlines():
        vec=[0]*len(vocabList)
        line = line.split("\t")
        if flag==0:
            flag=1
            continue
        name = line[0].split('@')
        if len(name)==2:
            for v in name[0]:
                if v.lower() in vocabList_set:
                    vec[vocabList.index(v.lower())] += 1
            if name[1] in domain_rate_dic:
                vec.append(domain_rate_dic[name[1]])
            else:
                vec.append(0.0)
            s = name[0].lower()

            if s.isalpha():
                vec.append(0.0114)
                vec.append(pattern_probability["is_alpha"])
            # vec =[item*1.1 for item in vec]
            elif s.isdigit():
                vec.append(0.0138)
                vec.append(pattern_probability["is_digit"])
                # vec =[item * 1.3 for item in vec]
            elif pc.is_num_alpha(s):
                vec.append(0.004)
                vec.append(pattern_probability["is_alpha_num"])
                # vec =[item * 1.2 for item in vec]
            elif pc.is_alpha_num(s):
                vec.append(0.0161)
                vec.append(pattern_probability["is_alpha_num"])
                # vec =[item * 2.7 for item in vec]
            else:
                vec.append(0.0090)
                vec.append(pattern_probability["other"])
            vec.append(pc.count_change(s))
            vec.append(len(s))
            vec.append(pc.probably_alp_num_no_1_sp_s(s))
            vec.append(pc.probably_alp_num_1_sp_s(s))
            vec.append(pc.probably_alp_s(s))
            # if pc.probably_s(s) == 1:
            #     print s
            # vec =[item * 1.1 for item in vec]
            # vec=vec
            vec.append(line[1].strip())
            # vec.append(line[2].strip())
            BOW.append(vec)
f3.close()
cheat_1_count=len(BOW)-cheat_0_count

print "extracting eigenvalue is completed"
print "cheat_flag=0:",cheat_0_count
print "cheat_flag=1:",cheat_1_count,'\n',"writing data ..."
file_cheat_sample="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_eigenvalue_sample_20160401_20160531.txt"
i=0
j=0
with open(file_cheat_sample,"w") as f4:
    for w in BOW:
        i+=1
        if i<=100000 or i>219639:
            j+=1
        # if i <= 20000 or i > 222116:
        # if i <= 20000 or i >= 129888:
            for v in w:
                f4.write(str(v)+' ')
            f4.write("\n")
        if i%10000==0:
            print "finish %d"%i
print "all data count:%d"%i
f4.close()
print "样本维度：",len(BOW[0])-1
print "样本量：",j


print "案件样本量：",cheat_1_count
print "非案件样本量：",cheat_0_count