#This function gets userinput then prints answer function
def main():
    uinput = input("File name: ").strip().lower()
    print(answer(uinput))

def answer(txt):

    if txt.endswith(".gif"):
        return "image/gif"
    elif txt.endswith(".jpg") or txt.endswith(".jpeg"):
        return "image/jpeg"

    elif txt.endswith(".png"):
        return "image/png"

    elif txt.endswith(".pdf"):
        return "application/pdf"

    elif txt.endswith(".txt"):
        return "text/plain"

    elif txt.endswith(".zip"):
        return "application/zip"

    else:
        return "application/octet-stream"

main()
