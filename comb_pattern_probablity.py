import codecs
import pattern_check as pc
file_cheat_flag_0_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_" \
                                     "repetiton_cheat_flag_0_20160401_20160531.txt"
with codecs.open(file_cheat_flag_0_no_repetition_data,'r') as f:
    lines=f.readlines()
pattern_dict={}
pattern_list=["is_alpha","is_digit","is_num_alpha","is_alpha_num","other"]
for v in pattern_list:
    pattern_dict[v]=0
for line in lines:
    tokens=line.strip().split("\t")
    name=tokens[0].split('@')
    if len(name)==2:
        s = name[0].lower()
        # if s.isupper():
        #     print s
        # print s
        if s.isalpha():
            pattern_dict[pattern_list[0]]+=1
            # vec =[item*1.1 for item in vec]
        elif s.isdigit():
            pattern_dict[pattern_list[1]] += 1
            # vec =[item * 1.3 for item in vec]
        elif pc.is_num_alpha(s):
            pattern_dict[pattern_list[2]] += 1
            # vec =[item * 1.2 for item in vec]
        elif pc.is_alpha_num(s):
            pattern_dict[pattern_list[3]] += 1
            # vec =[item * 2.7 for item in vec]
        else:
            pattern_dict[pattern_list[4]] += 1
            # vec =[item * 1.1 for item in vec]
sum_pattern=0
for v in pattern_list:
    sum_pattern+=pattern_dict[v]
for v in pattern_list:
    pattern_dict[v]=pattern_dict[v]*1.0/sum_pattern
file_pattern_probability="d:\\Users\\xw_zhang\\Desktop\\job\\data\\pattern_probability.txt"
with open(file_pattern_probability,'w') as f1:
    for v in pattern_dict:
        f1.write(v+'\t'+str(pattern_dict[v])+'\n')
