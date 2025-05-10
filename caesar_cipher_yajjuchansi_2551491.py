"""
Student Name: Yajju Chansi
Student ID: NP03CS4S250097
University ID: 2551491

Caesar Cipher Program
"""
import os


def welcome():
    """Displaying  welcome message."""
    print("Welcome to the Caesar Cipher")
    print("\nThis program encrypts and decrypts text using the Caesar Cipher.\n")


def enter_message():
    """Prompt user to enter the mode, message, and shift value. // local variable"""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ('e', 'd'):
            break
        print("Invalid Mode. Please enter 'e' or 'd'.")

    message = input(
        f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
    message = message.upper()

    while True:
        shift_input = input("What is the shift number: ")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        print("Invalid Shift. Please enter a number.")

    return mode, message, shift


def encrypt(message, shift):
    """Encrypt the given message by shifting  letters."""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift):
    """Decrypt the given message by reversing the shift."""
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message


def is_file(filename):
    """Check if a file exists."""
    return os.path.isfile(filename)


def process_file(filename, mode, shift):
    """Process a file line by line and encrypt/decrypt each line."""
    processed_messages = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            message = line.strip().upper()
            if mode == 'e':
                processed_messages.append(encrypt(message, shift))
            else:
                processed_messages.append(decrypt(message, shift))
    return processed_messages


def write_messages(messages):
    """Write a list of messages to results.txt."""
    with open('results.txt', 'w', encoding='utf-8') as file:
        for message in messages:
            file.write(message + '\n')


def message_or_file():
    """Prompt user to choose between file input or console input."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ('e', 'd'):
            break
        print("Invalid Mode. Please enter 'e' or 'd'.")
# Encryption/Decryption Mode:
    while True:
        source = input(
            "Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ('f', 'c'):
            break
        print("Invalid choice. Please enter 'f' or 'c'.")

    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            print("Invalid Filename. Please try again.")

        while True:
            shift_input = input("What is the shift number: ")
            if shift_input.isdigit():
                shift = int(shift_input)
                break
            print("Invalid Shift. Please enter a number.")

        return mode, None, filename, shift

    message = input(
        f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ")
    message = message.upper()

    while True:
        shift_input = input("What is the shift number: ")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        print("Invalid Shift. Please enter a number.")

    return mode, message, None, shift


def main():
    """Main function of the program."""
    welcome()

    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            results = process_file(filename, mode, shift)
            write_messages(results)
            print("Output written to results.txt")
        else:
            if mode == 'e':
                result = encrypt(message, shift)
            else:
                result = decrypt(message, shift)
            print(result)

        while True:
            again = input(
                "Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if again in ('y', 'n'):
                break
            print("Invalid Input. Please enter 'y' or 'n'.")

        if again == 'n':
            print("Thanks for using the program, goodbye!")
            break


main()
