"""
message_cipher.py contains two functions to encrypt and decrypt messages.
"""
__author__ = "7592047, Khauto"
__email__ = "khauto@em.uni-frankfurt.de"


def encrypt_message(message, shift):
    """
    Encrypts a message by shifting each letter by the specified shift value.
    
    Parameters:
        message (str): The message to encrypt.
        shift (int): The number of positions to shift each letter.
    
    Returns:
        str: The encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-letter characters remain the same
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    """
    Decrypts a message by shifting each letter backwards by the specified shift value.
    
    Parameters:
        encrypted_message (str): The message to decrypt.
        shift (int): The number of positions to shift each letter backwards.
    
    Returns:
        str: The decrypted message.
    """
    return encrypt_message(encrypted_message, -shift)  # Use negative shift for decryption


if __name__ == "__main__":
    
    m1 = "IloveFrankfurt"
    e_m1 = encrypt_message(m1, 3)
    d_m1 = decrypt_message(e_m1, 3)
    print(f"Message: {m1}, encrypted: {e_m1}, decrypted: {d_m1}")

    m2 = "helloThere"
    e_m2 = encrypt_message(m2, 4)
    d_m2 = decrypt_message(e_m2, 4)
    print(f"Message: {m2}, encrypted: {e_m2}, decrypted: {d_m2}")

    m3 = "what!is=going23on"
    e_m3 = encrypt_message(m3, 6)
    d_m3 = decrypt_message(e_m3, 6)
    print(f"Message: {m3}, encrypted: {e_m3}, decrypted: {d_m3}")