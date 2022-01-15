# 20ce130
# Krima Shah
# A: Write a Python program to add member(s) in a set and clear a set

Set = {'P', 'Q', 'R', 'S', 'T'}
print("set before adding :",Set)
Set.add('U')
print("Set before clear:", Set)
print("Set after clear:", Set.clear())

# B:Write a Python program to remove an item from a set if it is present in the set.

Set = {'A', 'B', 'C', 'D', 'E'}
Set.discard('A')
print(Set)

#C:Write a Python program to create an intersection, Union, difference of sets.

setA = {10, 20, 30, 40, 50}
setB = {40, 50, 60, 70, 80}
print("Union of A and B:", setA.union(setB))
print("Intersection of A and B:", setA.intersection(setB))
print("Difference of A and B:", setA.difference(setB))

# D:Write a Python program to find maximum and the minimum value in a set.
Set={100,200,300,400,500,600,700,800,900,1000}
print("maxium of set :",max(Set))
print("minium of set :",min(Set))

#E:Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

list1 = [12,8,3.4,5.6,20]
tuple1 = (12,20,10,3.4,2)
dictionary1 = {20,1,3.4,5.6}
print("List =", list1)
print("Tuple =", tuple1)
print("Dictionary =",dictionary1)
set1 =set(list1).intersection(set(tuple1))
result_set = set1.intersection(set(dictionary1))
final_list = list(result_set)
print("Common of members of list, tuple and dictionary:", final_list)