my_age = 20

user_age = int(input('Enter your age: '))
if user_age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need to wait {18-user_age} more year(s) until you can drive')

if my_age > user_age:
    print(f'I am {my_age-user_age} year(s) older than you')
elif my_age < user_age:
    print(f'You are {user_age-my_age} year(s) older than me')
else:
    print('We are the Same Age')

number_a = int(input('Input Number One'))
number_b = int(input('Input Number Two'))

if number_a > number_b:
    print("A is greater than B")
elif number_a < number_b:
    print("A is less than B")
else:
    print("A and B are equal")


int_grade = int(input('Enter the number of points from 0-100: '))

if int_grade >= 90:
    print("Your Grade is an A")
elif int_grade >= 80:
    print("Your Grade is an B")
elif int_grade >= 70:
    print("Your Grade is an C")
elif int_grade >= 60:
    print("Your Grade is an D")
else:
    print('Your Grade is an F')

season_map = {
    'Spring':['March', 'April', 'May'],
    'Summer':['June','July','August'],
    'Autumn':['September', 'October', 'November'],
    'Winter':['December', 'January','February']
}

inputted_season = str(input('Enter the season ')).capitalize().strip()
for keys, values in season_map.items():
    if inputted_season in values:
        found_season = keys
        print(f'The season for {inputted_season} is {found_season}')
        break
else:
        print('Check the season input')


fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input('Enter a new fruit '))
fruits.append(new_fruit) if new_fruit not in fruits else print('Already in list')
print(fruits)


me = {
    'first_name':'Danel',
    'last_name':'Rahmani',
    'age':20,
    'country':'The Netherlands',
    'is_married':False,
    'skills':['JavaScript', 'Linux', 'Node', 'HTML', 'Python'],
    'City': 'Groningen',
    'address':{
        'street':'DummyStreet',
        'zipcode':'0000'
    }
    }

if me.get('skills') is not None:
    print(me['skills'][len(me['skills'])//2])
    if 'Python' in me['skills']:
        print('This Person Knows Python')
    else:
        print('No python bozo')
else:
    print('No skills')
    
if me['country'] == 'The Netherlands' and me['first_name'] == 'Danel' and me['is_married'] == False:
    print(f'{me['first_name']} {me['last_name']} lives in {me['country']} and is unmarried')
else:
    print('This message shouldnt even be')

          
          

