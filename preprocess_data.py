#coding:utf-8

file_cheat_flag_0_row_data = "d:\\Users\\xw_zhang\\Desktop\\job\\data\\cheat_flag_0_20160601_20160701_fraud_flag.txt"
file_cheat_flag_1_row_data = "d:\\Users\\xw_zhang\\Desktop\\job\\data\\cheat_flag_1_20160601_20160701_fraud_flag.txt"
file_cheat_flag_0_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_0_20160601" \
                                     "_20160701_fraud_flag.txt"
file_cheat_flag_1_no_repetition_data="d:\\Users\\xw_zhang\\Desktop\\job\\data\\no_repetiton_cheat_flag_1_20160601" \
                                     "_20160701_fraud_flag.txt"
print "reading data ..."
with open(file_cheat_flag_0_row_data,"r") as f1:
    lines_0=f1.readlines()
f1.close()
with open(file_cheat_flag_1_row_data,"r") as f1:
    lines_1=f1.readlines()
f1.close()
print "reading data is completed\n","start processing..."
s=set()


with open(file_cheat_flag_0_no_repetition_data,"w") as f2:
    for line in lines_0:
        line= line.split('\t')

        if line[0] not in s:
            s.add(line[0])
            f2.write(line[0])
            f2.write("\t")
            f2.write(line[1])
            f2.write("\t")

            f2.write(line[2])
f2.close()
count_cheat_flag_0=len(s)-1
s=set()
with open(file_cheat_flag_1_no_repetition_data,"w") as f2:
    for line in lines_1:
        line= line.split('\t')
        if line[0] not in s:
            s.add(line[0])
            f2.write(line[0])
            f2.write("\t")
            f2.write(line[1])
            f2.write("\t")
            # print line
            f2.write(line[2])
f2.close()
count_cheat_flag_1=len(s)-1
print "processing data is finished"
print "cheat_flag_0_no_repetition data:",count_cheat_flag_0
print "cheat_flag_1_no_repetition data:",count_cheat_flag_1