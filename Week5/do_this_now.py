def name_of_oldest(names, ages):
    oldest_age = max(ages)
    oldest_age_index = ages.index(oldest_age)
    return names[oldest_age_index]


names = ["Cue Nguyen", "Hellene Clinton", "Sarah Edison"]
ages = [50, 60, 20]
print(name_of_oldest(names, ages))
contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
print(contacts)
print(contacts['bill'])
contacts['cue'] = '233-1234'
print(contacts)
contacts['cue'] = '111-1234'
print(contacts)
for key in contacts:
    print(contacts[key])

my_contacts = contacts.copy()
print(my_contacts)
print(my_contacts.pop('cue'))
print(my_contacts)
print(contacts)

print(contacts.items())
print(contacts.keys())
print(contacts.values())

for key, value in contacts.items():
    print(key, value)



















