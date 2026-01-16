dog = {
    'Name':'Blufo',
    'Colour':'Black',
    'Breed':'Husky',
    'Legs':4,
    'Age': 5
}
print(dog)

me = {
    'first_name':'Danel',
    'last_name':'Rahmani',
    'age':20,
    'country':'The Netherlands',
    'is_marred':False,
    'skills':['JavaScript', 'Linux', 'Node', 'HTML', 'Python'],
    'City': 'Groningen',
    'address':{
        'street':'DummyStreet',
        'zipcode':'0000'
    }
    }
print(me)
print(len(me))
print(me['skills'])
print(type(me['skills']))
me['skills'].append('Excel')
me_keys = me.keys()
me_values = me.values()
me.items()

del me['is_marred']

del dog