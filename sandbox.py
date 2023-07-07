my_list=[]
my_list.append(["dell", "$1000","256GB","5"])
my_list.append(["Lenox","$399","2TB","3"])
my_list.append(["HP","$399","2TB","4"])
my_list.append(["IBM","$399","2TB","7"])
my_list.append(["Lenox","$399","2TB","3"])

print(my_list)

my_tuple= set(map(tuple,my_list))
print(my_tuple)