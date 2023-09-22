"""
    Author: Ophir Nevo Michrowski
    Date: 22/09/2023
    Description: The encryption & user input handler
"""

# Imports #
import sys
import transposition_cipher
import ascii_art
from typing import List

# Constants #
FILE_PATH = "encrypted_msg.txt"


# Functions #
def file_handler(file_path, msg=None, read_or_write: str = 'w'):
    """
        Handles the writing and reading of a file containing a message or cipher text
        :param read_or_write: whether the software needs to read or write from a file
        :param file_path: the path to the file where the message or cipher text will be written or read from
        :param msg: the msg to be written within the file
        :return text_read: text read if there was text read from the file else the function will return None
    """

    def write_to_file() -> None:
        """
            Writes a message to a file
            :return: None
        """

        # Opening file #
        try:
            with open(file_path, 'w') as file:
                file.write(msg)

        # Other Exception handling #
        except Exception as error:
            print(error)

    def read_from_file() -> List[int]:
        """
            reads cipher text from a given file
            :return List[int]: the encrypted message to be decrypted
        """

        # Opening file #
        # noinspection PyBroadException
        try:
            with open(file_path, 'r') as file:
                res = [int(x) for x in file.read().split(",")]
                return res

        # Other Exception handling #
        except Exception:
            return []

    # File Handling #
    match read_or_write:
        # Read from file #
        case 'r':
            try:
                # Return text read from file #
                return read_from_file()

            # Exception handling #
            except Exception as err:
                print(err)

        # Write to file #
        case 'w':
            try:
                # Write to file #
                write_to_file()

            # Exception handling #
            except Exception as err:
                print(err)


def input_handler():
    """
    Handles the user input
    :return str: returns the message to encrypt
    :return None: if user chose decrypt
    """

    # Check the argument given by the user #
    try:
        match sys.argv[1].lower():
            # Encrypt message #
            case 'encrypt':
                print(ascii_art.ENCRYPT_ASCII)

                # Input Handling #
                msg = input("Oh dear Romeo. Enter thy message: ")

                # Empty message #
                if msg == "":
                    file_handler(FILE_PATH, msg=msg)

                # Nonempty message #
                else:
                    file_handler(FILE_PATH, ",".join([str(x) for x in transposition_cipher.encrypt(msg)]))

            # Decrypt message #
            case 'decrypt':
                print(ascii_art.DECRYPT_ASCII)

                cipher = file_handler(FILE_PATH, read_or_write='r')
                if not cipher:
                    print("empty message")
                else:
                    print(transposition_cipher.decrypt(cipher))

            # Unknown argument #
            case _:
                print("Invalid Input!")
    except IndexError:
        print("Oh Romeo Romeo...\n\n\nENTER AN ARGUMENT!!!!!!")


# Main Code #
if __name__ == '__main__':
    input_handler()
