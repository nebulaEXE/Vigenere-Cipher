from itertools import cycle
import sys

def decrypt(cipher,key):
    key_chars = cycle(key)
    msg = ''
    for char in cipher:
        if char.isalpha():
            if(char.islower()):
                value = ((ord(char) - 32) - ord(next(key_chars))) % 26
                msg += chr(value + 65).lower()
            else:
                value = (ord(char) - ord(next(key_chars))) % 26
                msg += chr(value + 65)
        else:
            msg +=char
    print(msg)

def main():
    cipher = input()
    key = input().upper()
    decrypt(cipher,key)
    sys.exit()

if __name__ == "__main__":
    main()