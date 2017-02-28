#coding:utf-8
import pattern_check as pc
file_cheat_0="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_0_20160601_20160701_fraud_flag.txt"
file_cheat_1="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_1_20160601_20160701_fraud_flag.txt"
# file_vocabSet_domainList="d:\\Users\\xw_zhang\\Desktop\\job\\data\\vocabSet_domainList.txt"
file_vocabList="d:\\Users\\xw_zhang\\Desktop\\job\\data\\vocabList.txt"
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

vocabList=[]
with open(file_vocabList,'r') as f1:
    for line in f1.readlines():
        line=line.strip().split(' ')
        for v in line:
            vocabList.append(v)
vocabList_set=set(vocabList)
f1.close()
BOW=[]
vec=[]
for i in range(len(vocabList)):
    vec.append(vocabList[i])
# print len(vec)
vec.append("domain_degree ")
vec.append("name_degree ")
vec.append("name_probability")
vec.append("num_change")
vec.append("length")
vec.append("prob_prefix_num_no_1")
vec.append("prob_prefix_num_1")
vec.append("prob_prefix_alp")
vec.append("cheat_flag ")
vec.append("fraud_flag ")
# print len(vec)
BOW.append(vec)
# print BOW[0]
# print len(BOW[0])
with open(file_cheat_0,'r') as f2:
    lines_nor=f2.readlines()
flag=0
for line_nor in lines_nor:
    # vec_l=[]
    vec=[0]*len(vocabList)
    line_nor=line_nor.split("\t")
    if flag==0:
        flag=1
        continue
    name=line_nor[0].split('@')
    if len(name)==2:
        for v in name[0]:
            if v.lower() in vocabList_set:
                vec[vocabList.index(v.lower())] += 1
        # print name[1]
        if name[1] in domain_rate_dic:
            vec.append(domain_rate_dic[name[1]])
        else:
            vec.append(0.0)
        s = name[0]
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
        vec.append(line_nor[1].strip())
        vec.append(line_nor[2].strip())
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
            s = name[0]
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
                vec.append(0.004)
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
            # vec =[item * 1.1 for item in vec]
            # vec=vec
            vec.append(pc.count_change(s))
            vec.append(len(s))
            vec.append(pc.probably_alp_num_no_1_sp_s(s))
            vec.append(pc.probably_alp_num_1_sp_s(s))
            vec.append(pc.probably_alp_s(s))
            vec.append(line[1].strip())
            vec.append(line[2].strip())
            BOW.append(vec)
f3.close()
cheat_1_count=len(BOW)-cheat_0_count

print "extracting eigenvalue is completed"
print "cheat_flag=0:",cheat_0_count
print "cheat_flag=1:",cheat_1_count,'\n',"writing data ..."
file_cheat_sample="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_eigenvalue_sample_20160601_20160701_fraud_flag.txt"
i=0

with open(file_cheat_sample,"w") as f4:
    for w in BOW:
        i+=1
        # if i<=20000 or i>219639:
        # if i <= 20000 or i >= 129888:
        for v in w:
            f4.write(str(v)+' ')
        f4.write("\n")
        if i%10000==0:
            print "finish %d"%i
print "all data count:%d"%i
f4.close()
print "样本维度：",len(BOW[1])-1
print "样本量：",len(BOW)
print "欺诈样本量：",cheat_1_count
print "非欺诈样本量：",cheat_0_count