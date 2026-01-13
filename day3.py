age = int(20)
height = float(184)
complex_number = complex(1+1j)

base = int(input('Enter base: '))
height= int(input('Enter height: '))
area_of_triangle = 0.5 * base * height
print('The area of the triangle is:', area_of_triangle)

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter of the triangle is:', perimeter_of_triangle)

length = int(input('Enter length: '))
width = int(input('Enter width: '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('The area of the rectangle is:', area_of_rectangle, 'and the perimeter of the rectangle is:', perimeter_of_rectangle)

radius = int(input('Enter radius: '))
area_circle = 3.14 * radius ** 2
circumference_circle = 2 * 3.14 * radius
print('The area of the circle is:', area_circle, 'and the circumference of the circle is:', circumference_circle)

m = 2
b = -2
slope_y = m
y_intercept = b
x_intercept = -b / m
print('The slope (m) is:', slope_y, 'the y-intercept (b) is:', y_intercept, 'and the x-intercept is:', x_intercept)

y_1= 2
y_2= 10
x_1= 2
x_2= 6
d= (y_1 - y_2) / (x_1 - x_2)
distance=((y_2 - y_1) ** 2 + (x_2 - x_1) ** 2)**0.5
print('The slope between the points (2,2) and (6,10) is:', distance, 'and the slope is:', d)

print('the slope y and d are equal: ',slope_y == d,
      'the slope y and d are unequal:',slope_y != d,
      'slope_y < d:',slope_y < d,
      'slope_y > d:',slope_y > d,
      'slope_y <= d:',slope_y <= d,
      'slope_y >= d:',slope_y >= d)

for x in range(-10, 10):
    y = x**2 + 6*x + 9
    print(f' when x = {x}, y = {y}')
    if y == 0:
        print(f'The value of x that makes y zero is: {x}')
        break

len_python = len('Python')
len_dragon = len('Dragon')
print('Length of Python and Dragon are equal:', not(len_python == len_dragon))

if 'on' in 'Python' and 'on' in 'Dragon':
    print("on is in both dragon and python:")
else:
    print("on is not in both dragon and python:")

if 'jargon' in 'I hope this course is not full of jargon':
    print("jargon is in the sentence")
else:
    print("jargon is not in the sentence")

float_python=float(len_python)
string_python=str(float_python)
print(string_python)

for num in range(0, 10):
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')

if int(2.7) == 7 // 3:
    print('int(2.7) and 7//3 are equal')
else:
    print('int(2.7) and 7//3 are not equal')

print("the type of '10' and 10 are equal:", type('10') == type(10))

print("the int of '9.8' and 10 are equal:", int(float('9.8')) == 10)

hours = int(input('Enter hours per week: '))
rate_per_hour = int(input('Enter rate per hour: '))
salary = hours * rate_per_hour
print('Your weekly earning is:', salary)

age= int(input('Enter your age: '))
print('You have lived for', age * 365 * 24 * 60 * 60, 'seconds')


num_rows = 5
print("Number | One| Number| Square|Cube")
print("-------|----|-------|-------|----")
for i in range(1, num_rows + 1):
    square = i * i
    cube = i * i * i
    print(f"{i:>6} | {1:>3} | {i:>5} | {square:>6} | {cube:>4}")

