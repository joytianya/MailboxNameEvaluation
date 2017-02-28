#coding:utf-8
import numpy as np
file_cheat_flag_0_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_0_20160401_20160531.txt"
file_cheat_flag_1_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_1_20160401_20160531.txt"
domain={}
domain_name=[]
with open(file_cheat_flag_0_no_repetition_data,'r') as f:
    lines_0=f.readlines()
f.close()
with open(file_cheat_flag_1_no_repetition_data,'r') as f:
    lines_1=f.readlines()
f.close()
i=0
for line in lines_0:
    line=line.split('\t')
    if i==0:
        i=1
        continue
    domain_tokens=line[0].split('@')
    if len(domain_tokens)==2:
        domain_name.append(domain_tokens[1])
        # domain|=set(domain_tokens[1])
i=0
for line in lines_1:
    line=line.split('\t')
    if i==0:
        i=1
        continue
    domain_tokens=line[0].split('@')
    if len(domain_tokens)==2:
        domain_name.append(domain_tokens[1])
        # domain|=set(domain_tokens[1])
for i in range(len(domain_name)):
    domain[domain_name[i]]=[]
i=0
for line in lines_0:
    line=line.strip().split('\t')
    if i==0:
        i=1
        continue
    domain_tokens=line[0].split('@')
    if len(domain_tokens)==2:
        # domain_name.append(domain_tokens[1])
        # domain|=set(domain_tokens[1])
        domain[domain_tokens[1]].append(line[1])
i=0
for line in lines_1:
    # print line
    line=line.strip().split('\t')
    if i==0:
        i=1
        continue
    domain_tokens=line[0].split('@')
    if len(domain_tokens)==2:
        # domain_name.append(domain_tokens[1])
        # domain|=set(domain_tokens[1])
        # print line[1]
        domain[domain_tokens[1]].append(line[1])
domain_rate={}
# y=np.zero()

for i in domain.keys():
    domain_a=np.array(domain[i])
    y = np.zeros(domain_a.shape)
    # print domain_a
    y[domain_a == '1'] = 1
    domain_rate[i]=sum(y)*1.0/len(domain[i])
sort_domain_rate=sorted(domain_rate.items(), key=lambda domain_rate: domain_rate[1])
file_domain_rate="d:\\Users\\xw_zhang\\Desktop\\job\\data\\domain_rate_20160401_20160531.txt"
with open(file_domain_rate,'w') as f:
    f.write('domain_name'+'\t'+"domain_rate\n")
    for i in range(len(sort_domain_rate)):
        if sort_domain_rate[i][1]>=0.01:
            f.write(sort_domain_rate[i][0]+'\t'+str(sort_domain_rate[i][1])+'\n')
        print sort_domain_rate[i][0],sort_domain_rate[i][1],domain[sort_domain_rate[i][0]]

# print set(domain)