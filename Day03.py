'''
Created on Saturday Oct 10 23:12:06 2024
author: @righCirith
'''


import math

age = 100 #1.int
height = 5.4 #2.float
complex = 4j #3.complex 


#4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print('Triangle Area and Perimeter Calculator')
triangle_b = float(input('Enter the base: '))
triangle_h = float(input('Enter the height: '))
triangle_area = (triangle_b*triangle_h)/2
triangle_side_a = float(input('Type side a: '))
triangle_side_b = float(input('Type side b: '))
triangle_side_c = float(input('Type side c: '))
triangle_perimeter = triangle_side_a + triangle_side_b + triangle_side_c
print(f'Triangle Perimeter = {triangle_perimeter}')
print(f'Triangle Area = {triangle_area}')


#6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('Rectangle Perimeter and Area Calculator')
rectangle_l = float(input('Type the length: '))
rectangle_w = float(input('Type the width: '))
rectangle_area = rectangle_l*rectangle_w
rectangle_perimeter = 2*(rectangle_l + rectangle_w)
print(f'Rectangle Area = {rectangle_area}, Rectangle Perimeter = {rectangle_perimeter}')


#7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print('Circle Radius and Area Calculator')
pi = 3.14
radius = float(input('Type the radius: '))
circle_area = pi*(radius**2)
circle_circumference = 2*pi*radius
print(f'Area = {circle_area}, Circumference = {circle_circumference}')


#8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
A = (0, -2)
B = (1, 0)
y1 = 0
y2 = -2
x1 = 1
x2 = 0
slope1 = (y2 - y1) / (x2 - x1)
print('First function (y = 2x - 2)')
print(f'A = {A}, B = {B}')
print(f'Slope = {slope1}')


#9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
P = (2, 2)
Q = (6, 10)
x1 = P[0]
x2 = Q[0]
y1 = P[1]
y2 = Q[1]
slope2 = (y2 - y1) / (x2 - x1)
#euclidean distance formula: d = √[(x2 – x1)^2 + (y2 – y1)^2].
euclidean_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('Second function')
print(f'P = {P}, Q = {Q}')
print(f'Euclidean distance = {euclidean_distance}')
print(f'Slope = {slope2}')


#10.Compare the slopes in tasks 8 and 9.
print('Are both slopes the same?:', slope1 == slope2)


#11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6*x + 9
print(y)


#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') < len('dragon'))


#13.Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Is "on" in both "python" and "dragon"?:', 'on' in 'python' and 'on' in 'dragon')


#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)


#15.There is no 'on' in both dragon and python
print(not('on' in 'pyton' and 'on' in 'dragon'))


#16.Find the length of the text python and convert the value to float and convert it to string
text = 'python'
print(str(int(len(text))))
print(type(text))


#17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = float(input('Type a number to check if it is divisible by 2: '))
if num%2 == 0:
    print(f'Your number {num} is divisble by 2')
else:
    print(f'Your number {num} is not divisible by 2')


#18.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))


#19.Check if type of '10' is equal to type of 10
print(type('10') == type(10))


#20.Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)


#21.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print('Payment calculator')
hours = int(input('Type the hours: '))
rate_per_hour = int(input('Type the rate per hour: '))
payment = hours*rate_per_hour
print('Weekly payment is', payment)


#22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
persons_age = int(input('How old are you: '))
one_second = 1
seconds_in_one_minute = one_second*60
seconds_in_one_hour = seconds_in_one_minute*60
one_day =  seconds_in_one_hour*24
seconds_in_one_year = one_day*365
seconds_lived = persons_age*seconds_in_one_year
print(f'You have lived for: {seconds_lived} seconds')


#23.Write a Python script that displays the following table1 #1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

#simple
#print(1, 1, 1, 1)
#print(2, 1, 2, 4, 8)
#print(3, 1, 3, 9, 27)
#print(4, 1, 4, 16, 64)
#print(5, 1, 5, 25, 125)


#this was my first idea
#v2 = 2
#v3 = 3
#print(v2, v2-v2+1, v2, v2**2, v2**3)
#print(v3, v3-v3+1, v3, v3**2, v3**3)

#using a for loop
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
