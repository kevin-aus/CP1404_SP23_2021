valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:
        print("Not a number")

if age % 2 == 0:
    print("{} is even".format(age))
else:
    print("{} is odd".format(age))
