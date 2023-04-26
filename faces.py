#This function converts emoticons into emoji and returns it
def convert():
    emoticon = input("type some emoticon and see the magic ")
    emoticon = emoticon.replace(':)','🙂').replace(':(','🙁')
    return emoticon
#This function prints emoji
def main():
    print(convert())

main()
