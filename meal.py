def main():
    time = input("What time is it? ")
    converttime= convert(time)
    if 7.0 <= converttime <= 8.0:
        print("Breakfast time")
    elif 12.0 <= converttime <= 13.0:
        print("Lunch time")
    elif 18.0 <= converttime <= 19.0:
        print("Dinner time")
    else:
        pass
#split will assign for example 7:30  "7" to hours and "30" to minutes.
def convert(time):
    hours, minutes = time.split(":")
    convertminutes = float(minutes) / 60
    converthours = float(hours)
    time = convertminutes + converthours
    return float(time)


if __name__ == "__main__":

    main()
