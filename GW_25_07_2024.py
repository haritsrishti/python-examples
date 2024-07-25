#Write a Python function that takes an array of integers and
# returns the sum of all the elements in the array

intarray=[1,2,3,4]
output=[sum(intarray)]
print(output)

#or

def sum1(x):
    print([sum(x)])
array1=[1,2,3]
sum1(array1)

#Write a Python function that takes an array of integers
# and returns a new array with each element doubled.


intarray=[1,2,3]
new=[]
for i in intarray:
    new.append(i*2)
    i=i+1
print(new)

#append

intarray.append(4)
print(intarray)


#Write a Python function count_odd_numbers(arr) that takes a list of integers arr
#as input and returns the count of odd numbers in the list.

def odd_no(x):
    count=0
    for i in x:
        if i%2!=0:
            count+=1
    print(count)
arr=[11,3,6,7,9]
odd_no(arr)
