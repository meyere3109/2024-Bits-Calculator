# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = f"Please enter a whole number that is more than or equal to {low}\n"
    while True:

        try:
            # Ask user for Response and loop until they
            response = int(input(question))

            # enter a number that is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0, 2):
    integer = int_check("Width: ", 1)
    print(integer)

    print()

for item in range(0, 2):
    integer = int_check("Height: ", 1)
    print(integer)
