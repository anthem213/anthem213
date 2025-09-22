

my_list = ["apple", "banana", "orange", "apple", "mango", "banana", "grape"]

d = dict()
b=[]
for i in my_list:
    if i not in b:
        d[i]=1
        b.append(i)
    else:
        d[i] =d[i]+1


print(d)