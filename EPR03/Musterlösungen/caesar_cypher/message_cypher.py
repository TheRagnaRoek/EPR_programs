"""En- and Decryption-Functions for Caesar-Encryption (aka Shift-Encryption)"""

__author__ = "7003725, van Reem"
__email__ = "drvanreem@stud.uni-frankfurt.de"


def encrypt_message(message: str, shift: int) -> str:
    """Encrypts a given message by a set shift (Caesar-Cypher)"""

    shift_base: int = 0
    encrypted_message: str = ""

    for char in message:  # for i in range(len(message))
        if 64 < ord(char) < 123:  # ASCII-range for upper- and lowercase letters
            if char.isupper():  # base depends on character case
                shift_base = 65  # ord("A")
            else:
                shift_base = 97  # ord("a")

            # encryption formula
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

def decrypt_message(encrypted_message: str, shift: int) -> str:
    """Decrypts a given message encrypted through a Caesar-Cypher"""

    shift_base: int = 0
    decrypted_message: str = ""

    for char in encrypted_message:
        if 64 < ord(char) < 123:
            if char.isupper():  # base depends on character case
                shift_base = 65  # ord("A")
            else:
                shift_base = 97  # ord("a")
            
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    return decrypted_message

def decrypt_smart(message: str, shift: int) -> str:
    """If you want to be really smart"""
    return encrypt_message(message, -shift)

if __name__ == "__main__":
    print("***TESTSTRINGS***\n")

    TESTSTRING1 = "ABCDEF, abcdef + OP?"
    TESTSTRING2 = "Peter Piper picked a pack of pickled peppers."
    TESTSTRING3 = "ALWAYS look on the BRIGHT 51d3 0f /_1F3"

    print(TESTSTRING1)
    print(TESTSTRING2)
    print(TESTSTRING3)

    print("\n***ENCRYPTION TESTING***\n")

    TESTENCRYPT1 = encrypt_message(TESTSTRING1, 7)
    TESTENCRYPT2 = encrypt_message(TESTSTRING2, 1)
    TESTENCRYPT3 = encrypt_message(TESTSTRING3, 11)

    print(TESTENCRYPT1)
    print(TESTENCRYPT2)
    print(TESTENCRYPT3)

    print("\n***DECRYPTION TESTING***\n")

    print(decrypt_message(TESTENCRYPT1, 7))
    print(decrypt_message(TESTENCRYPT2, 1))
    print(decrypt_message(TESTENCRYPT3, 11))

    print("\n***TESTING END***")
    input("Press <return> to continue...")
