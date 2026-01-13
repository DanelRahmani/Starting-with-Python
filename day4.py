word_1 = 'thirty'
word_2 = 'days'
word_3 = 'of'
word_4 = 'python'
space = ' '
result = word_1.capitalize() + space + word_2.capitalize() + space + word_3.capitalize() + space + word_4.capitalize()
print(result)  # Output: Thirty Days Of Python

word_5 = 'coding'
word_6 = 'for'
word_7 = 'all'
result_2 = word_5.capitalize() + space + word_6 + space + word_7
print(result_2)  # Output: Coding for all

company = result_2
print(company)
print(len(company))  # Output: 14
print(company.upper())  # Output: CODING FOR ALL
print(company.lower())  # Output: coding for all
print(company.capitalize())  # Output: Coding for all
print(company.title())  # Output: Coding For All
print(company.swapcase())  # Output: cODING FOR ALL
print(company.startswith('Coding'))  
print(company.index("Coding"))  

print(company.replace('coding', 'python'))
print(company.replace('all', 'everyone'))
python_string = company.replace('coding', 'python').replace('all', 'everyone')
print(company.split())  # Output: ['coding', 'for', 'all']

string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies = string.split(', ')
print(companies)

print(company[0])  
print(company[-1])
print(company[10])

Acronmym = ''
for char in python_string:
    if char.isupper():
        Acronmym += char
print(Acronmym)  # Output: CFA

Acronym_2 = ''
for word in company.split():
    Acronym_2 += word[0].upper()

print(company.index('C'))
if company.find('F') != -1:
    print(company.index('F'))
print(company.rindex('l'))

sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
if sentence.index('because') != -1:
    print(sentence.index('because'))
if sentence.find("'because'") != -1:
    print(sentence.index("'because'"))
else:
    print("Substring not found.")

if company.find('Coding') != -1:
    print("Yes, 'Coding' is found in the string.")
else:
    print("No, 'Coding' is not found in the string.")

if company.endswith('coding'):
    print("The string ends with 'coding'.")
else:
    print("The string does not end with 'coding'.")

space_remove = '   Coding For All      '
print(space_remove.strip())  # Output: 'Coding For All'

identifier1 = '30DaysOfPython'
identifier2 = 'thirty_days_of_python'
print(identifier1.isidentifier())  
print(identifier2.isidentifier())  

list =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))  # Output: Django# Flask# Bottle# Pyramid# Falcon

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
eight = 8
six = 6
print(f"{eight} + {six} = {eight + six}")
print(f"{eight} - {six} = {eight - six}")
print(f"{eight} * {six} = {eight * six}")
print(f"{eight} / {six} = {eight / six:.2f}")
print(f"{eight} % {six} = {eight % six}")
print(f"{eight} // {six} = {eight // six}")
print(f"{eight} ** {six} = {eight ** six}")
