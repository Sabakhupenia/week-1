def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    for c in range(len(s)):
        if s[c].isdigit():
            if not s[c:].isdigit():
                if not s[c:].isdigit():
                    return False
    for _ in s:
        if s in [","," ","!","?","."]:
            return False
    if s[2] == "0":
        return False
    return True

main()
