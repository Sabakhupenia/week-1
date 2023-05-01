
def main():

    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
#this function call takes x,y,z as parameters
    calculate(x,y,z)

def calculate(x,y,z):

    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))

main()
