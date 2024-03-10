while True:
    zip_code = input("Enter zip code: ")
    length = len(zip_code)

    if length == 5 and zip_code.isdigit():
        print("Your entry is valid.")
        break
    else:
        print("Please enter a valid entry.")




  