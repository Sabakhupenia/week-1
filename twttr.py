
def main():
    txt=input("Input: ").strip()
    print(ovowels(txt))

def ovowels(txt):
    vowels = ["a", "e", "i", "o", "u",]
    for letter in txt:
        if letter.lower() in vowels:
            txt = txt.replace(letter, "")

    return txt

main()

