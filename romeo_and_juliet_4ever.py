"""
    Author: Ophir Nevo Michrowski
    Date: 22/09/2023
    Description: The encryption & user input handler
"""

# Imports #
import sys, os, transposition_cipher
from typing import List


# Constants #


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


# Main Code #
if __name__ == '__main__':
    # print(transposition_cipher.encrypt("My bounty"))
    # print(transposition_cipher.decrypt([48, 96, 98, 13, 36, 92, 35, 91, 96]))

    if not os.path.isfile("text.txt"):
        file_handler(file_path=r"C:\Users\ophir\Desktop\text.txt", msg="Hello World!", read_or_write='w')
