"""
    Author: Ophir Nevo Michrowski
    Date: 22/09/2023
    Description: Encryption to help dear old Romeo send a secret message to his chosen one without being found.
"""

# Imports #
from typing import List

# Constants #
ENCRYPTION_TABLE = {
    'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 'g': 18, 'h': 19, 'i': 30, 'j': 31,
    'k': 32, 'l': 33, 'm': 34, 'n': 35, 'o': 36, 'p': 37, 'q': 38, 'r': 39, 's': 90, 't': 91, 'u': 92, 'v': 93, 'w': 94,
    'x': 95, 'y': 96,
    'z': 97, 'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46,
    'L': 47, 'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63, 'S': 64, 'T': 65, 'U': 66, 'V': 67, 'W': 68, 'X': 69,
    'Y': 10, 'Z': 11,
    ' ': 98, ',': 99, '.': 100, ';': 101, "'": 102, '?': 103, '!': 104, ':': 105,
}


# Functions #
def encrypt(msg: str) -> List[int]:
    """
      Takes a str message and uses transposition encryption to encrypt said message
      :param msg: the message that is to be encrypted
      :return List[int]: returns the encrypted message in the format of an int list
    """

    # translating the letters to the compatible symbol into a list of the cipher text
    return [ENCRYPTION_TABLE[x] if x in ENCRYPTION_TABLE.keys() else x for x in msg]


def decrypt(cipher: List[int]) -> str:
    """
      Takes an int list cipher and uses transposition decryption to decrypt said cipher text
      :param cipher: the cipher text that is to be decrypted
      :return str: returns the encrypted message in the format of an int list
    """

    # taking the elements from the cipher list and translate them into the string

    return "".join([list(ENCRYPTION_TABLE.keys())[list(ENCRYPTION_TABLE.values()).index(x)]
                    if x in ENCRYPTION_TABLE.values() else str(x) for x in cipher])
