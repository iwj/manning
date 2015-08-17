def print_them(them_list):
    print "name: ", them_list[0]
    print "address: ", them_list[1]
    print "street: ", them_list[2]
    print "city: ", them_list[3]
    print "province: ", them_list[4]
    print "stamp: ", them_list[5]
    print "country: ", them_list[6]

input_list = []
print "name, address, street, city, province, stamp, country:"
for i in range(7):
    input_list.append(raw_input())

print_them(input_list)
