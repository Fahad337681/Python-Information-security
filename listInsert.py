list=[2,3,6,7]
list.insert(2,45)
print(list)

#extend method(Adds each element as individual)
list.extend([8,'Fahad','Python'])
print(list)

#Remove method
print("List after removing an element")
list.remove(45)
print(list)

#removing using an iterator
for i in range(6,8,1):
    list.remove(i)
print("List after removing a range by using an iterator")
print(list)

#removing element from the list using pop method
list.pop()
print("List after popping the last element")
print(list)
