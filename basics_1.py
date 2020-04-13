"""
print message like below

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


"""
Compute the area of a circle, take side from input and calculate area
 """
side = int(input("Please enter the value of side "))
PI = 3.142
print("Area of the square is {} ".format(PI*side**2))

"""
Write a Python program which 
accepts the user's first and last name 
and print them in reverse order with a space between them
"""
first_name = input("Enter your first name  ")
last_name = input("Enter your last name  ")

print("your name in reverse is {} ".format(last_name[::-1]+" "+first_name[::-1]))

"""
Write a Python program which accepts a sequence of comma-separated numbers from user
 and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""
seq_numbers = input("Enter numbers followed with comma ")
print(list(seq_numbers.split(",")))
print(tuple(seq_numbers.split(",")))

"""
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""
file_name = input("Enter file name with extension ")
print("extension of the file_name is {} ".format(file_name.split(".")[-1]))

"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date)
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

import datetime 

st_date = datetime.datetime.now()
print(str(st_date.year)+"/"+str(st_date.month)+"/"+str(st_date.day))

"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
 """
date1 = (2014, 7, 2)
date2= (2014, 7, 11)
print(date2[-1]-date1[-1])

from datetime import date  
f_date = date(2014,4,12)
l_date = date(2015,1,12)
delta = l_date - f_date
print(delta.days)