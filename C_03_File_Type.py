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
            return "integer"

        # if the response is invalid output error
        else:
            print("Sorry, please choose an integer, text or image")
            get_filetype()


# Main routine goes here
while True:
    file_type = get_filetype()

    # choose image or integer when entered 'i'
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"\nYou chose {file_type}\n")

    if file_type == "xxx":
        break
