

def reverse_string(a):
    r=""
    for i in a:
        r= i + r
    return r

print(reverse_string("jack")) # o/p: kcaj




#Max mark from tuple

students=[('DAVID',78),('SAM',76),('MAY',99)]
marks =[]
for k,v in students:
    marks.append(v)

max_mark = max(marks)
for k,v in students:
    if v == max_mark:
        print(k)


fruits=['apple','grape','pineapple']
for index, fruit in enumerate(fruits):
                  print(f"index:{index},fruit:{fruit}")



# remove dupes from list

l1=[1,2,3,4,4,5,2,1]

print(list(set(l1)))


set_A = {'x', 'y', 'z'}
set_B = {1, 2, 3}

# Convert sets to sorted lists to ensure consistent order
list_A = sorted(set_A)
list_B = sorted(set_B)

# Generate the expected output
result = list(zip(list_A, list_B))

print(result)


# check prime

def prime_number(n):
    flag = False
    if n < 2:
        return "it is not  a prime number"
    for i in range(2,n):
        if n%i==0:
            flag= True
            break


    if flag:
        return "Not a prime"
    else:
        return "Its a prime"


print(prime_number(11))
