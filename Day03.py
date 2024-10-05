import time
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


time.sleep(2)
#6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('Rectangle Perimeter and Area Calculator')
rectangle_l = float(input('Type the length: '))
rectangle_w = float(input('Type the width: '))
rectangle_area = rectangle_l*rectangle_w
rectangle_perimeter = 2*(rectangle_l + rectangle_w)
print(f'Rectangle Area = {rectangle_area}, Rectangle Perimeter = {rectangle_perimeter}')


time.sleep(2)
#7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print('Circle Radius and Area Calculator')
pi = 3.14
radius = float(input('Type the radius: '))
circle_area = pi*(radius**2)
circle_circumference = 2*pi*radius
print(f'Area = {circle_area}, Circumference = {circle_circumference}')


time.sleep(2)
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


time.sleep(2)
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


time.sleep(2)
#10.Compare the slopes in tasks 8 and 9.
print('Are both slopes the same?:', slope1 == slope2)


time.sleep(2)
#11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6*x + 9
print(y)


time.sleep(2)
#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') < len('dragon'))


time.sleep(2)
#13.Use and operator to check if 'on' is found in both 'python' and 'dragon'
on_py = 'on' in 'python'
on_dr = 'on' in 'dragon'
print('Is on in python and dragon?:', on_dr and on_py)



time.sleep(2)
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)
