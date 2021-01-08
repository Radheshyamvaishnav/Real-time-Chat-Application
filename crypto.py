from Crypto.Cipher import AES

key = b'some' * 4  # Use a stored / generated key

# data_to_encrypt = 'This is the message i want to send'  # This is your data

cipher_encrypt = AES.new(key, AES.MODE_CFB)
iv = cipher_encrypt.iv


def encryption(data_to_encrypt):
    data = data_to_encrypt
    ciphered_data = cipher_encrypt.encrypt(data)
    return ciphered_data


def decryption(ciphered_data):
    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
    deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)
    decrypted_data = deciphered_bytes
    return decrypted_data

# print(decryption(encryption(data_to_encrypt)))
