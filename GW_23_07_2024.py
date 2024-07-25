""" write a program to ask the user to enter name of their 3 movies
 and store them in a list
"""


movies = []
m1 = input("Enter your first movie name")
m2 = input("Enter your second movie name")
m3 = input("Enter your third movie name")

movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)

'''' WAP to count the number of students with the 'A' grade in the following list.
#[c,d,a,a,b,b,a]'''

grade=["c","d","a","a","b","b","a"]
# count function
print(grade.count('a'))

#Reverse
grade.reverse()
print(grade)


#LENGTH
print(len(grade))
#or
x=len(grade)
print(x)
