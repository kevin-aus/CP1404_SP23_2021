vowels = "aieou"
name = input("Enter fullname: ")
cleaned_name = name.strip().lower()
while len(cleaned_name) == 0:
    name = input("Enter fullname: ")
    cleaned_name = name.strip().lower()
num_of_vowels = 0
for i in range(len(cleaned_name)):
    if cleaned_name[i] in vowels:
        num_of_vowels += 1
print("Out of {} letters, {} has {} vowels".
      format(len(cleaned_name), cleaned_name.title(), num_of_vowels))

