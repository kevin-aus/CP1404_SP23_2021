class Person(object):
    def __init__(self, name='Unknown', age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} ({})".format(self.name, self.age)


if __name__ == '__main__':
    person1 = Person('Cue', 50)
    person2 = Person('Anand', 20)
    person3 = Person('Amandeep', 20)
    print(person1)
    print(person2)
    print(person3)
    print(type(person1))
    print(person1.__class__)

