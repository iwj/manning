name = []
for i in range(0,5):
    name.append(raw_input("Input name: "))
print "The names are",
for i in range(0, 5):
    print name[i],
delete_num = int(raw_input("Which name you want to replace?(1-5)"))
replace_name = raw_input("Input the new name:")
name[delete_num-1] = replace_name

print "The renew name list:"
for i in range(0, 5):
    print name[i],
