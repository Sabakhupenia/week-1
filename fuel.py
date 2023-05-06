def main():
    fraction()

def fraction():
    while True:
        # Ask the user to input the fuel fraction
        fuel = input("Fraction: ")
        try:
            # Split the input into numerator and denominator
            x, y = list(fuel.split("/"))
            # Convert the numerator and denominator to integers
            n_x = int(x)
            n_y = int(y)

            # Calculate the decimal value of the fraction
            z = n_x / n_y

            # If the fuel level is equal to 1, break out of the loop
            if   z <= 1:
                break
        except (ValueError, ZeroDivisionError):
            # If the input is invalid, continue the loop
            pass

    # Calculate the percentage of fuel
    percent = z * 100

    # Check if the fuel level is empty (less than or equal to 1 percent)
    if percent <= 1:
        # Print "E" to indicate the fuel level is empty
        print("E")
    # Check if the fuel level is full (greater than or equal to 99 percent)
    elif percent >= 99:
        # Print "F" to indicate the fuel level is full
        print("F")
    else:
        # Print the percentage of fuel rounded to the nearest whole number
        print(f"{round(percent)}%")

# Call the main function to start the program
main()
