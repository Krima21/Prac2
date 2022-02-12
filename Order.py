

q = int(input())

dict = {}
for i in range(q):

    str = input() 
    if str in dict: 
        dict[str] += 1
    else:
        dict[str] = 1

print(len(dict)) 
for i in dict.values():

 print (i, end=" ")
