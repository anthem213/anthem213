
#remove duplicates from string
str1='Substrrrringgg'

s= set()
l=[]
f=""
for i in str1.lower():
    if i not in s:
        f = f + "".join(i)
        s.add(i)


print(f) #o/p: subtring


c = ['a','b', 'c','d']
print("".join(c))  #o/p: abcd