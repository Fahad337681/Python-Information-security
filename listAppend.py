list=[]
print(list)

print("\n Appended list")
list.append(34)
list.append(4)
list.append(3)

print(list)

#Adding elements to the list using iterator
for i in range(1,4):
    list.append(i)
print("List After Appending through Iteration")
print(list)

#Adding tuples to the list already present
print("List after adding tuples")
list.append((7,8))
print(list)

print("List after appending another list")
list2=[45,67]
list.append(list2)
print(list)

