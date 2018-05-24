
def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    count = 0
    while count != n:
        text = encrypted_text[1::2] + encrypted_text[::2]
        count += 1
    return text


print(decrypt("This is a test!", 0))
print(decrypt("This is a test!", 1))
print(decrypt("This is a test!", 2))
print(decrypt("This is a test!", 3))
print(decrypt("This is a test!", 4))
print(decrypt("This is a test!", -1))
