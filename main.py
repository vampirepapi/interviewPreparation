#convert decimal to binary
dec=10
bin_list = []
while dec > 0:
    bin_list.append(dec % 2)
    dec = dec // 2
bin_list.reverse()
print("Binary Equivalent is: ",*bin_list, sep='')
count = bin_list.count(1)
print("Numbers of 1 in the Binary Number: ",count)