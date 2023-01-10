# creating an empty set
b=set()
print(type(b))
# addding values to an empty sets
b.add(4)
b.add(56)
b.add(4)           
b.add(567)
b.add((454,895,688))     #tuples can be added because they are addable(immutable)
# accesing elements of the sets
# b.add({4:5})   #cannot add list and dictionery in sets because list and dictionery are mutable
print(b)
# length of the sets
print (len(b))  #printing the length of the sets
# removal of  an item
b.remove(4)   #remove 4 from the sets
# b.remove(34)  # throws an error when u tries to remove any no which is not in sets
print(b)
print(b.pop)
print(b)
