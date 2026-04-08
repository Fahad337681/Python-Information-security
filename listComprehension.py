odd_square=[]
for i in range(1,11):
    if(i%2==0):
      odd_square.append(i**2)

print(odd_square)

print("Printing odd numbers square")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=[x*x for x in nums if x%2!=0]
print(result)

#Task:
#List comprehension use karke sirf un names ko uppercase me banao jinka length 4 se zyada ho.

names = ["ali", "ahmad", "sara", "usman", "zain"]
result=[name.upper() for name in names if len(name)>3]
print("Printing words having more than 3 alphabets")
print(result)

#Task:
#List comprehension se sirf even numbers ka cube (x³) nikal kar list banao.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=[x*x*x for x in nums if x%2==0 ]
print("Printing cube of even numbers from ths given list")
print(result)


nums = [5, 10, 15, 20, 25, 30]
#List comprehension se sirf un numbers ka half nikalo jo 15 se zyada ho.

result=[x/2 for x in nums if x>15]
print("Printing half of numbers which are greater than  15")
print(result)