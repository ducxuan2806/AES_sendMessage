from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

# Tạo khóa và cipher
key = get_random_bytes(32)
iv = get_random_bytes(AES.block_size)

def messageEncrypt(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = message.encode('utf-8')
    padded_data = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def messageDecrypt(message, key, iv):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(decipher.decrypt(message), AES.block_size)
    return decrypted_data.decode('utf-8')


message = "an com khong"
d = message.encode('utf-8')
print(d)
print(d.decode('utf-8'))
