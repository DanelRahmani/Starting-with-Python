# Day 2: 30 Days of Python programming
first_name = 'Danel'
last_name = 'Rahmani'
full_name = first_name + ' ' + last_name
country = 'The Netherlands'
city = 'Groningen'
age = 20
year = 2026
is_married = False
is_skilled, is_perfect, is_smart = True, True, True


print('First name:', first_name)
print('First name length:', len(first_name))
print('Type of first name:', type(first_name))

print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Type of last name:', type(last_name))

print('Full name:', full_name)
print('Full name length:', len(full_name))
print('Type of full name:', type(full_name))

print('Country:', country)
print('Type of country:', type(country))

print('City:', city)
print('Type of city:', type(city))

print('Age:', age)
print('Type of age:', type(age))

print('Year:', year)
print('Type of year:', type(year))

print('Married:', is_married)
print('Type of is_married:', type(is_married))

print('Skilled:', is_skilled, 'is_perfect:', is_perfect, 'is_smart:', is_smart)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius_of_circle = float(input('Enter radius of a circle: '))
area_of_circle = 3.14 * radius_of_circle ** 2
circum_of_circle = 2 * 3.14 * radius_of_circle
print('For a circle with a radius of', radius_of_circle, 'The Area of the circle is:', area_of_circle, 'and the Circumference of the circle is:', circum_of_circle)



# Variables in Python
first_name_user = input('What is your name: ')
last_name_user = input('What is your last name: ')
country_user = input('What is your country: ')
city_user = input('What is your city: ')
age_user = int(input('What is your age: '))
is_married_user = input('Are you married? (True/False): ')
skills_user = input('What are your skills(seperate with ,): ').split(', ')
person_info_user = {
   'firstname':first_name_user,
   'lastname':last_name_user,
   'country':country_user,
   'city':city_user,
   'age':age_user,
   'is_married':is_married_user, 
   'skills': skills_user
   }

print('First name:', first_name_user)
print('First name length:', len(first_name_user))
print('type:', type(first_name_user))

print('Last name: ', last_name_user)
print('Last name length: ', len(last_name_user))
print('type:', type(last_name_user))

print('Country: ', country_user)
print('type:', type(country_user))

print('City: ', city_user)
print('type:', type(city_user))

print('Age: ', age_user)
print('type:', type(age_user))

print('Married: ', is_married_user)
print('type:', type(is_married_user))

print('Skills: ', skills_user)
print('type:', type(skills_user))

print('Person information: ', person_info_user)
print('type:', type(person_info_user))