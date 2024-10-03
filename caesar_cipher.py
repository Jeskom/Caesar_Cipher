alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encodes any message to an offset of your choice, default offset is 10
def caesar_encode(message, offset=10):
    coded_letters = []
    coded_message = ""

    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            coded_index = index - offset
            if coded_index < 0:
                new_index = coded_index + len(alphabet)
                coded_letters.append(alphabet[new_index])
            else: coded_letters.append(alphabet[coded_index])
        else: coded_letters.append(i)
    
    for i in coded_letters:
        coded_message += i
    return coded_message

#decodes any message to an offset of your choice, default offset is 10
def caesar_decode(message, offset=10):
    cracked_let = []
    cracked_msg = ""
    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            decoded_index = index + offset
            if decoded_index >= len(alphabet):
                new_index = decoded_index - len(alphabet)
                cracked_let.append(alphabet[new_index])
            else: cracked_let.append(alphabet[decoded_index])
        else: cracked_let.append(i)
        
    for i in cracked_let:
        cracked_msg += str(i)
    return cracked_msg

print(caesar_encode("this is a test :)", 7))
print(caesar_decode("jxyi yi q juij :)", 7))