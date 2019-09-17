# Write a program that examines three variables—x, y, and z— and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.
#
# Python provides a built-in function called len that returns the length of a string, so the value of len('Cigna') is 5.
# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
#
# >>> right_justify('Cigna')
# 																	 Cigna
# Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.
#
# Practice using the Python interpreter as a calculator:
#
# a) The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere with radius 5?
# Hint: 392.7 is wrong!
# b) Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
# Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
# 60 copies?
# c) If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
#
# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.
#
# Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.
#
# Write a function isIn() that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.
#
# Implement a function that satisfies the specification. Use a try-except block.
#
# def getRatios(vect1, vect2):
# 	"""Assumes: vect1 and vect2 are lists of equal length of numbers
# 	Returns: a list containing the meaningful values of
# 	vect1[i]/vect2[i]"""
# Assume that we execute the following assignment statements: width = 17 height = 12.0 delimiter = '.'
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# >>> width/2
# >>> width/2.0
# >>> height/3
# >>> 1 + 2 * 5
# >>> delimiter * 5
# Use the Python interpreter to check your answers
# Observe the Code Snippet
# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
# print 'low =', low, 'high =', high, 'ans =', ans
# numGuesses += 1
# if ans**2 < x:
# low = ans
# else:
# high = ans
# ans = (high + low)/2.0
# print 'numGuesses =', numGuesses
# print ans, 'is close to square root of', x
# a. What would the code above return if the statement x = 25 were replaced by x = -25?
#
# b. What would have to be changed to make the code above for finding an approximation to the cube root of both negative and positive