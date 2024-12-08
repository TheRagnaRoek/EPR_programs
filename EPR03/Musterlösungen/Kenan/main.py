"""
main.py
"""
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"

import message_cipher

def main():
    """
    Main function that asks the user to choose between encryption and decryption,
    and then performs the chosen operation on the input message.
    
    Parameters:
        None
    
    Returns:
        None
    """
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    
    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (e.g., 3): "))
        encrypted_message = message_cipher.encrypt_message(message, shift)
        print("Encrypted Message:", encrypted_message)
    
    elif choice == 'D':
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value used for encryption: "))
        decrypted_message = message_cipher.decrypt_message(encrypted_message, shift)
        print("Decrypted Message:", decrypted_message)
    
    else:
        print("Invalid choice! Please choose 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()