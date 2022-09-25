from itertools import cycle
import sys

def encrypt(msg,key):
    key_chars = cycle(key)
    ciphertext = ''
    for char in msg:
        if char.isalpha():
            if(char.islower()):
                value = ((ord(char) - 32) + ord(next(key_chars))) % 26
                ciphertext += chr(value + 65).lower()
            else:
                value = (ord(char) + ord(next(key_chars))) % 26
                ciphertext += chr(value + 65)
        else:
            ciphertext +=char
    print(ciphertext)

def main():
    msg = input()
    key = input().upper()
    encrypt(msg,key)
    sys.exit()

if __name__ == "__main__":
    main()