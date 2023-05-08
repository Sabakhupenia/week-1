
# create an empty dictionary to store the grocery list
grocery_list = {}

# continuously prompt the user to input fruits until they press Ctrl-D or a KeyError is raised
while True:
    try:
        # read in a fruit from the user and convert it to uppercase
        fruit = input("").upper()

        # if the fruit is not already in the grocery list, add it with a count of 1
        if fruit not in grocery_list:
            grocery_list[fruit] = 1
        # if the fruit is already in the grocery list, increment its count by 1
        else:
            grocery_list[fruit] += 1
    except (EOFError, KeyError):
        # stop prompting for input if the user presses Ctrl-D or a KeyError is raised
        break

# sort the grocery list by fruit name (keys) in alphabetical order and print the results
for key, value in sorted(grocery_list.items()):
    # print the fruit count and name in the format "count fruit"
    print(value, key)
