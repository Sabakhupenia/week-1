def calculate(str):
    x, y, z = str.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        return x+z
    elif y == "-":
        return x-z
    elif y == "*":
        return x*z
    elif y == "/":
        return x/z

main()
