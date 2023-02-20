import optparse


# Takes in a plaintext message
# and an integer key and encrypts
# using the Caesar cipher approach
def encrypt(msg, key):
    # TODO implement encryption approach
    encrypt_msg = ""
    # Changeing String to Char Array
    list_ch = list(msg)
    # Encryption for Captial Letters and Small Letters
    for i in range(len(list_ch)):
        if ord(list_ch[i]) >= 65 and ord(list_ch[i]) <= 90:
            l = int(ord(list_ch[i]) - ord('A'))
            l = ((l + key) % 26) + ord('A')
        elif ord(list_ch[i]) >= 97 and ord(list_ch[i]) <= 122:
            l = int(ord(list_ch[i]) - ord('a'))
            l = ((l + key) % 26) + ord('a')
        elif list_ch[i] == " ":
            l = ord(list_ch[i])
        list_ch[i] = chr(l)

    print(encrypt_msg.join(list_ch))
    return encrypt_msg


# Takes in an encrypted message
# and an integer key and decrypts
# using the Caesar cipher approach
def decrypt(msg, key):
    # TODO implement decryption approach
    decrypt_msg = ""
    # Changeing String to Char Array
    list_ch = list(msg)
    # Decryption for Captial Letters and Small Letters
    for i in range(len(list_ch)):
        if ord(list_ch[i]) >= 65 and ord(list_ch[i]) <= 90:
            l = int(ord(list_ch[i]) - ord('A'))
            l = ((l - key) % 26) + ord('A')
        elif ord(list_ch[i]) >= 97 and ord(list_ch[i]) <= 122:
            l = int(ord(list_ch[i]) - ord('a'))
            l = ((l - key) % 26) + ord('a')
        elif list_ch[i] == " ":
            l = ord(list_ch[i])
        list_ch[i] = chr(l)

    print(decrypt_msg.join(list_ch))
    return decrypt_msg

def backtrack(msg, key):
    decrypt_msg = ""
    # Changeing String to Char Array
    list_ch = list(msg)
    # Decryption for Captial Letters and Small Letters using 26 times
    for i in range(len(list_ch)):
        if ord(list_ch[i]) >= 65 and ord(list_ch[i]) <= 90:
            l = int(ord(list_ch[i]) - ord('A'))
            l = ((l - key) % 26) + ord('A')
        elif ord(list_ch[i]) >= 97 and ord(list_ch[i]) <= 122:
            l = int(ord(list_ch[i]) - ord('a'))
            l = ((l - key) % 26) + ord('a')
        elif list_ch[i] == " ":
            l = ord(list_ch[i])
        list_ch[i] = chr(l)
    print(decrypt_msg.join(list_ch))


def main():
    parser = optparse.OptionParser("usage%prog " + "-f <decrypt | encrypt | backtrack > -m <message> -k <key>")
    parser.add_option('-f', dest='function', type='string', help='[ decrypt | encrypt | backtrack ]')
    parser.add_option('-m', dest='msg', type='string', help='message to encrypt (plaintext) or decrypt (encrypted)')
    parser.add_option('-k', dest='key', type='int', help='cipher key as an integer')
    (options, args) = parser.parse_args()
    function = options.function
    if function != "encrypt" and function != "decrypt" and function != "backtrack" or function == "None":
        print('[-] You must specify a valid function: "encrypt" or "decrypt"')
        exit(0)
    msg = str(options.msg)
    key = int(options.key)
    if msg == "None":
        print('[-] You must specify a message.')
        exit(0)
    if function == "encrypt":
        encrypt(msg, key)
    elif function == "decrypt":
        decrypt(msg, key)
    elif function == "backtrack":
        for i in range(0,26):
            backtrack(msg, i)


if __name__ == '__main__':
    main()
