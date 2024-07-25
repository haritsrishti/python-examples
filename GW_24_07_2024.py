#create a tupple with elements of people in this meeting,
# starting the index with 5< print index and name together
students=("devansh","gagan","pari","harshit","vishaka","shristi")
for i,j in enumerate(students):
    print(i+5,j)


#create a tupple with intergers and print the output as sum of those integers
# in the tupple
int=(1,2,3)
print(sum(int))

#OR

j=0
for i in int:
    j=j+i
print(j)


'''take tupple=(4,5,6,7)
print the number of odd and even number in the tupple
expexted output
odd:2
even:2'''

tup=(4,5,6,8,7,5)
evenno=0
oddno=0
for i in tup:
    if i%2==0:
        evenno+=1
    else:
        oddno+=1
print("odd = ",oddno)
print("even = ",evenno)