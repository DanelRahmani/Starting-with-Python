# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update('Nvidia', 'AMD','Intel')
it_companies.remove('Apple')
# Discard will not give an error if the discarded item doesn't exist in the set

joint_set = A.union(B)
print(A.intersection(B))
print(f'A is a subset of B is: {A.issubset(B)}')
print(f'Are A and B disjoint: {A.isdisjoint(B)}')
A.update(B)
print("The Symmetric difference is: ", A.symmetric_difference(B))
del A, B

age_set = set(age)

print((len(age)), len(age_set)) # age set smaller as duplicates removed
# string is just text, list is collection of data( may be different types), tuple is similair to list BUT cannot be changed after being made, set is somewhat similair but doesnt have an order, and does not contain dupes)
string = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
sentence = 'I am a teacher and I love to inspire and teach people'
cleaned_sentence = sentence.lower()
word_list = cleaned_sentence.split()
unique_words = set(word_list)

print(len(unique_words))



      
