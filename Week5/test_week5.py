name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
name = input('Enter name: ')
age = int(input('Enter age: '))
name_to_age[name] = age
for key, value in name_to_age.items():
    # print(key, '-', value)
    print('{:10s}-{:10d}'.format(key, value))

for count, key in enumerate(name_to_age):
    print(count, key)

my_list = [1, "Cue", 35.95]
for i, value in enumerate(my_list):
    print(i, value)

# result = {name: age for name, age in name_to_age.items() if age < 18}
result = {}
for name, age in name_to_age.items():
    if age < 18:
        result[name] = age

print(result)

my_set = set()
print(my_set)
my_set.add(1)
my_set.add('Cue Nguyen')
print(my_set)

my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}
print(my_subjects - your_subjects)
print(my_subjects | your_subjects)
print(my_subjects & your_subjects)
print(my_subjects ^ your_subjects)














