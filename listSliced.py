list=[2,3,4,5,6,7,8]

print("Original List",list)
print("Printing list from 2 to 4 number",list[0:4])
print("Printing till 6",list[:5])
print("Printing from 4 till last element",list[2:])

#Now with jump
print("printing from number 2 number 7 with jump of 2(skipping one element)",list[0:6:2])
print("Printing reverse list",list[::-1])
print("printing reverse list till number 3 from 8",list[-1:-7])
