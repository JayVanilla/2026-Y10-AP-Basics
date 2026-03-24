def num_check (question):

    error = "Please enter a number that is more than zero, yes this is a human that wrote this dude\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

print("(In meters)\n")

keep_going = ""
while keep_going == "":

    # Get width, height, cost of fence per meter
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("Cost of fence per meter: ")

    # Calculate cost of fence & Perimeter
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price = {price}$")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit \n")

print("Thank you for using the area / perimeter calculator\n")
