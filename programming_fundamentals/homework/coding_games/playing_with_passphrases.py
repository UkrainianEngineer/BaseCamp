
def play_pass(s, n):
    new_sentence = ''
    for index, letter in enumerate(s):
        if letter.isdigit():
            letter = 9 - int(letter)
            new_sentence += str(letter)
        elif letter.isalpha():
            letter = shift_char(letter, n)
            if index % 2 == 0:
                new_sentence += letter.upper()
            elif index % 2 == 1:
                new_sentence += letter.lower()
        else:
            new_sentence += letter

    return new_sentence[::-1]


def shift_char(char, n):
    new_letter = ord(char) + n
    if new_letter > ord('Z'):
        new_letter = new_letter - ord('Z') + ord('A') - 1
    elif new_letter < ord('A'):
        new_letter = new_letter + ord('Z') - ord('A')
    return chr(new_letter)
