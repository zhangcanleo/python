my_split_object = open(r'test.txt','a+')

my_split_object.write('testwrite')

#s = my_split_object.read().strip('\n')
#print(s)
#my_split_object.close()
my_split_object.seek(0)

#my_split_object = open(r'test.txt','r')
s = my_split_object.read().strip('\n')
print(s)
print(len(s))
my_split_object.close()


my_split_object = open(r'test.txt','a+')

#my_split_object.write('testwrite')

#s = my_split_object.read().strip('\n')
#print(s)
#my_split_object.close()

my_split_object.seek(0)
#my_split_object = open(r'test.txt','r')
s = my_split_object.read().strip('\n')
print(s)
print(len(s))
my_split_object.close()
