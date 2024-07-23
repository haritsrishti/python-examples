#sorting in ascending order...
glasses_quantity = [9,2,6,1,3]
glasses_quantity.sort()
print(glasses_quantity)



#sorting in descending order...
glasses_quantity = [99,4,65,223,544]
glasses_quantity.sort(reverse=True)
print(glasses_quantity)



#sorting list of strings...
books = ["Secret History", "The Break", "The Book Thief", "River Of Flesh"]
scriber = ["Donna Tartt", "Marian Keyes", "Markus Zusak", "Ruchira Gupta"]
books.sort()
scriber.sort()
print(books)
print(authors)


#Using the sorted() function to sort a list without modifying the original list:
new_list = [202,55,199,8,33]
sorted_list = sorted(new_list)
print(sorted_list)
print(new_list)








