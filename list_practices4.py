#loop list
list =["apple", "banana", "kiwi"]
for x in list:
    print(x)

a =["ankesh", 3465,True]
for i in range(len(a)):
    print(a[i])

#while loop
a =["mobile", "tab","computer"]
i =0
while i< len(a):
    print(a[i])
i =i+1

#loop using in comprehension
teacher =["what is your name"]
[print(x) for i in teacher]