#This function gets userinput then prints answer function
def main():
    uinput = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    print(answer(uinput))
#This function takes some text and if true returns Yes if false returns No as a string
#Note: 42 here is a string
def answer(txt):

    match txt:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()
