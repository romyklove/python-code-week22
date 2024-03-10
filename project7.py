_zip_code=input("Enter your zip code: ")

try:
    # check if the entry is a number
    _zip_code_cast=int(_zip_code)
    if len(_zip_code) == 5 :
        print("Your entry is valid")
    else:
        print("Please enter a valid entry")
except ValueError:
    print("ValueError !!! Please enter a zip code")