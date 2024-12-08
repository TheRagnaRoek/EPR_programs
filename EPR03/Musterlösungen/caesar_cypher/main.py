"""Main function for en- and decryption of messages.

This module handles the user input for a message and desired shift, to apply
the so-called Shift- or Caesar-Cypher on the message. A given message can either
be en- or decrypted with a given shift."""

__author__ = "van Reem, 7003725"
__email__ = "drvanreem@stud.uni-frankfurt.de"

from message_cypher import encrypt_message, decrypt_message
import random as r

print("*" * 20)
print("CAESAR-CYPHER v1.0")
print("*" * 20)

print("\nThis program can en- or decypher a given message by a desired shift.\n"
      "Each letter in the message is shifted by the given number of places.\n"
      "Non-alphabet symbols are excluded in the encryption.\n")

def main() -> None:
    """Main function for user input and en-/decryption"""

    while True:
        user_option = input("Do you want to [E]ncrypt or [D]ecrypt a message?\n"
                            "Type the according bracketed letter and hit return\n"
                            "or type 'exit' to exit the program.\n")

        match user_option.lower():
            case "e":
                print("You have selected an encryption of a message.\n")
                message = input("Please enter your message to be encrypted:\n")
                while True:
                    try:
                        shift = int(input("By how much shift should the message be encrypted?\n"
                                        "(Please only enter integers.)\n"))
                    except ValueError:
                        print("What did I JUST say? Only integers!")
                    else:
                        encrypted = encrypt_message(message, shift)
                        print("Your encrypted message:\n",
                            encrypted, sep="")

                        input("Hit <return> to return to menu...")
                        print("*" * 20)
                        print("RETURNING TO MENU")
                        print("*" * 20)

                        break

            case "d":
                print("You have selected a decryption of a message.\n")
                message = input("Please enter your message to be decrypted:\n")
                while True:
                    try:
                        shift = int(input("By how much shift is the message encrypted?\n"
                                        "(Please only enter integers.)\n"))
                    except ValueError:
                        print("What did I JUST say? Only integers!")
                    else:
                        decrypted = decrypt_message(message, shift)
                        print("Your decrypted message:\n",
                            decrypted, sep="")

                        input("Hit <return> to return to menu...")
                        print("*" * 20)
                        print("RETURNING TO MENU")
                        print("*" * 20)

                        break

            case "exit":
                print("Exiting Program. Goodbye!")
                break

            case _:
                print("Unknown option. Please try again.")

if __name__ == "__main__":
    main()
