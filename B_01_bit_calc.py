# Generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

    print('''
Enter a valid file type from:
    - integer
    - image
    - text
To exit bits calculator enter:
    - xxx
    ''')


# asks users for file type (integer / image / text / xxx)
def get_filetype():
    while True:
        response = input("File type: ").lower()

        # check for 'i' or exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if its text
        elif response in ['text', 't', 'txt']:
            return "text"

        # check if it's an image
        elif response in ['image', 'p', 'img']:
            return "image"

        # if the response is invalid output error
        else:
            print("Sorry, please choose an integer, text or image")
            get_filetype()


# Calculates number of bits needed to represent text in ascii
def calc_text_bits():
    # Get text from user
    response = input("Enter text to convert: ")

    # Calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"'{response}' has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it,"
              f"\nwhich is {num_bits} bits.\n")

    return answer


# checking if answer was integer
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


# calculates how many bits are needed to represent an image
def image_calc():
    # get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}\n")

    return answer


# calculates how many bits are needed to represent an integer
def integer_calc():
    # get the image dimensions
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # set up answer and return it
    answer = (f"{integer} in binary is: {binary}. "
              f"\nWe need {num_bits} bits to represent it.")

    return answer


# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue. ")

if want_instructions == "":
    instructions("Instructions", "*")

# Main routine goes here


while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    # choose image or integer when entered 'i'
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"\nYou chose {file_type}\n")

    # Ask for text to convert
    if file_type == "text":
        text_ans = calc_text_bits()
        print(text_ans)

    # ask for image to convert
    elif file_type == "image":
        image_ans = image_calc()
        print(image_ans)

    # ask for integer to convert
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
