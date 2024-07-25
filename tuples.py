#Create a Tuple with elements of people in the meeting, start  the index with 5 < print index and name together..
employees = ("Alice", "Joe", "Stefan", "Maria")
j=5
for i in employees:
      print(i, j)
      j+=1


#Slicing in Tuples...
print(employees[0:1])  #index : object
print(employees[1:2])
print(employees[2:3])
print(employees[3:4])


#Tuple concatenation...
more_employees = ("Nella", "Candice", "Zach", "Chris")
employees_concat = employees + more_employees
print(employees_concat)


#Tuples Multiplication...
more_employees = ("Candice", "Zach")
print(more_employees * 2)
         # OR
print(more_employees + more_employees)  # This will concatenate the tuples, not multiply them."""


#Checking if an element exists in a tuple:
employees = ("Stefan")
print(employees)


#Getting the length of a tuple:
more_employees = ("Alice", "Joe", "Stefan", "Maria")
print(len(more_employees))



#create a tupple with intergers and print the output as sum of those integers in the tupple
no = (5, 10, 15, 20)
print(sum(no))












