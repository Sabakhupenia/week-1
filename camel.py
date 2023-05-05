def main():
     camel = input("camelCase: ")
     print("snake_case:", snakec(camel))

def snakec(camelCase):
     characters =[]
     for character in camelCase:
          if character.isupper():
               characters.append("_")
               characters.append(character.lower())
          else:
               characters.append(character)
     return"".join(characters)



main()


