# function to encode
def encode(string):
    # initializing resut variable to empty string
    result = ''

    # initializing with first character
    characterone = string[0]

    # looping through the string character by character
    for letter in string:
        #key = ord(first_char)
        result += chr(ord(characterone) + ord(letter))

    # return the resulted string
    return result


# function to decode
def decode(string):
    # initializing result variable to empty string
    result = ''

    # initializing with first character
    characterone = string[0]

    # looping through the string character by character
    for letter in string:
        # decoding
        result += chr(ord(letter) - ord(characterone) // 2)

    # return the resulted string
    return result


# main function
def main():
    # string input
    string = input('Enter the string: ')

    # call cipher functoin
    cipher = encode(string)
    print('The ciphered string is :', cipher)

    # call decipher function
    decipher = decode(cipher)
    print('The deciphered string is:', decipher)


# calling main function
main()
