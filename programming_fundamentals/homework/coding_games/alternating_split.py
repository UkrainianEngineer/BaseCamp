
def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    count = 0
    while count != n:
        encrypted_text = encrypted_text[1::2] + encrypted_text[::2]
        count += 1
    return encrypted_text


def encrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    count = 0
    while count != n:
        encrypted_text = encrypted_text[1::2] + encrypted_text[::2]
        count += 1
    return encrypted_text


def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    text_list = list(encrypted_text)
    list_leght = len(text_list)
    if list_leght % 2 == 0:
        splitted_text = list_leght//2
    else:
        splitted_text = (list_leght-1)//2
    first = text_list[0:splitted_text]
    second = text_list[splitted_text:list_leght]

    result_in_list = [ second[i//2] if i % 2 == 0 else first[(i-1)//2] for i in range(0,list_leght) ]
    result = ''.join(result_in_list)
    return decrypt(result,n-1)

def encrypt(text, n):
    if n <= 0 :
        return text
    text_list = list(text)
    first = text_list[::2]
    second = text_list[1::2]
    encrypted = second + first
    result = ''.join(encrypted)
    return encrypt(result,n-1)


print(decrypt("This is a test!", 0))
print(decrypt("This is a test!", 1))
print(decrypt("This is a test!", 2))
print(decrypt("This is a test!", 3))
print(decrypt("This is a test!", 4))
print(decrypt("This is a test!", -1))
print("================================")
print(encrypt("This is a test!", 0))
print(encrypt("hsi  etTi sats!", 1))
print(encrypt("s eT ashi tist!", 2))
print(encrypt(" Tah itse sits!", 3))
print(encrypt("This is a test!", 4))
print(encrypt("This is a test!", -1))

# encrypted_text = "This is a test!"
# text = "1234567890"
# text3 = text[1::2]    # [a::c]
# print(text3)

# text = encrypted_text[1::2] + encrypted_text[::2]
# print(text)
