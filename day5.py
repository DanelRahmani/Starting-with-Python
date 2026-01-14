empty_list = list()

anime_list = ['Neon Genesis Evangelion', 'Code Geass', 'Your lie in April', 'Steins;Gate','Mushoku Tensei','Oshi No Ko','Death Note']
print(len(anime_list))
anime_list_length = len(anime_list)
print(anime_list[1], anime_list[(int(anime_list_length/2))], anime_list[-1])

my_data = list['Danel', '20', '184.0', 'unmarried', 'Student']

it_companies = ['Facebook', 'Google', 'microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
len_it_companies = len(it_companies)
print(len_it_companies)
print(it_companies[1], it_companies[int(len_it_companies/2)], it_companies[-1])
it_companies[3] = 'Samsung'
print(it_companies)
it_companies.append('AMD')
it_companies.insert(int(len_it_companies/2), 'Nvidia')
print(it_companies)

it_companies[2]= it_companies[2].capitalize()
print(it_companies)

seperator = '#;  '
joint_string = seperator.join(it_companies)
print(joint_string)
chosen_company = input("Which company to check: ")
company_exist = chosen_company in it_companies
print(f"The Company {chosen_company} exists in the list is {company_exist}")
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

first_three = it_companies[:3]
last_three = it_companies[-3:]
middle_company = it_companies[int(len(it_companies)/2)]
print(first_three)
print(last_three)
print(middle_company)

del it_companies[0]
del it_companies[int(len(it_companies)/2)]
del it_companies[-1]
it_companies.clear
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
full_stack = front_end.copy()

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age =ages[-1]
median_age = ages[int(len(ages)/2)]
average_age = (sum(ages))/len(ages)
range_age = (ages[-1])-(ages[0])
min_average = abs(min_age-average_age)
max_average = abs(max_age-average_age)
print(f"The minimum age is {min_age} and the maximum age is {max_age}")
print(f'The median age is {median_age}')
print(f'The average age is {average_age}')
print(f'The range of ages is {range_age}')
print(f'The absolute difference of min-average is {min_average} and the absolute difference of max-average is {max_average}')

