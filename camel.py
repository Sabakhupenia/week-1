camel = input("camelCase: ")
snake =""

for character in camel:
    if character.isupper():
         snake += "_" + character.lower()
    else:
         snake += character

print("snake_case:", snake)
