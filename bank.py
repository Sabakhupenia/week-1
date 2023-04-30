def main():
    userinput = input("Greeting: ").strip().lower()
    print(Answer(userinput))

def Answer(txt):
    if txt.startswith("hello"):
        return "$0"
    elif txt.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
