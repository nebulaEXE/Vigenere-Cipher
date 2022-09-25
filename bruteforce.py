import re, sys, math
from task2 import decrypt
from task3 import crack
MAX_KEYLENGTH = 100
MIN_KEYLENGTH = 2

def getNthLetters(n, keylength, message):
        NONLETTERS_PATTERN = re.compile('[^a-zA-Z]')
        message = NONLETTERS_PATTERN.sub('', message)
        i = n - 1
        letters = []
        while i < len(message):
            letters.append(message[i].upper())
            i += keylength
        return ''.join(letters)

def calcKeyLength(cipher):
    totalICValues = []
    for i in range(MIN_KEYLENGTH, MAX_KEYLENGTH, 1): #start at 2, up to max
        sequences = []
        for j in range(i): 
            sequences.append(getNthLetters(j + 1, i, cipher))
            total = 0
        
        for sequence in sequences: #for every cipher in list of ciphers
            ICValue = 0
            ICValues = []
            length = len(sequence)
            for char in sequence: #for every char in each sequence
                freq = {c: sequence.count(c) for c in set(sequence)}
            for char in freq.keys(): #for every char in each sequence in frequency table
                ICValue += (freq[char] * (freq[char] - 1)) / (length * (length - 1))
            ICValues.append(ICValue)
            for n in range(len(ICValues)):
                total += ICValues[n]
        averageIC = total / i
        totalICValues.append(averageIC)
   
    highest = totalICValues[0]
    secondhighest = totalICValues[0]
    keyCount = 0
    secondKeyCount = 0
    for i in range(len(totalICValues)):
        if (totalICValues[i] > highest):
            highest = totalICValues[i]
            keyCount = i + 2 #we start key length at 2
    
    for i in range(keyCount - 2):
        if (totalICValues[i] > secondhighest):
            secondhighest = totalICValues[i]
            secondKeyCount = i + 2
    return math.gcd(keyCount,secondKeyCount)     

def main():
    cipher = input()
    keylength = calcKeyLength(cipher)
    key = crack(cipher,keylength)
    print(key)
    decrypt(cipher,key)
    sys.exit()

if __name__ == "__main__":
    main()