def is_palindrome():
    print("Palindrome Checker")
    # Input from the user
    text = input("Enter a string to check if it is a palindrome: ").strip()

    # Remove non-alphanumeric characters and convert to lowercase
    processed_text = ''.join(char.lower() for char in text if char.isalnum())

    # Check if the processed string is the same as its reverse
    if processed_text == processed_text[::-1]:
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

# Run the palindrome checker
is_palindrome()
