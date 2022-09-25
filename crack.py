import re, sys
from task2 import decrypt

englishLetterFreq = {'E': 0.124167, 'T': 0.0969225, 'A': 0.0820011, 'O': 0.0714095, 'I': 0.0768052, 
    'N': 0.0764055, 'S': 0.0706768, 'H': 0.0350386, 'R': 0.0668132, 'D': 0.0363709, 
    'L': 0.0448308, 'C': 0.0344391, 'U': 0.028777, 'M': 0.0281775, 'W': 0.0135225, 
    'F': 0.0235145, 'G': 0.0181188, 'Y': 0.0189182, 'P': 0.0203171, 'B': 0.0106581, 
    'V': 0.0124567, 'K': 0.00393019, 'J': 0.0019984, 'X': 0.00219824, 'Q': 0.0009325, 'Z': 0.000599}

def getNthLetters(n, keylength, message):
        NONLETTERS_PATTERN = re.compile('[^a-zA-Z]')
        message = NONLETTERS_PATTERN.sub('', message)
        i = n - 1
        letters = []
        while i < len(message):
            letters.append(message[i].upper())
            i += keylength
        return ''.join(letters)

def caesarDecrypt(shift, message):
    letters = []
    value = ''
    for char in message:
        value = ((ord(char) - shift - 65) % 26)
        value = chr(value + 65)
        letters.append(value)
    return ''.join(letters)

def calcBestChiLetters(ciphers,keylength):
    finalValues = []
    keyValue = []
    for i in range(keylength):
        caesarCiphers = []
        for j in range(26):
            caesarCiphers.append(caesarDecrypt(j,ciphers[i]))
        totalList = []
        for cipher in caesarCiphers: #for every cipher in the list of 26
            cipherLength = len(cipher)
            totalChiSqValue = 0
        
            for char in cipher: #for every character in the cipher
                freq = {i: cipher.count(i) for i in set(cipher)}
            
            for char in freq.keys(): #for every char count in the cipher, calculate chi square
                totalChiSqValue += ((freq[char] - (cipherLength * englishLetterFreq[char])) ** 2)/ englishLetterFreq[char]
            totalList.append(totalChiSqValue)
            
        indexOfLowest = 0
        lowest = totalList[0]
        for i in range(len(totalList)):
            if(totalList[i] < lowest):
                indexOfLowest = i
                lowest = totalList[i]
        finalValues.append(indexOfLowest)
    return finalValues

def convertToKey(values):
    str = ''
    for value in values:
        str += chr(value + 65)
    return str

def crack(cipher, keylength):
    ciphers = []
    for i in range(keylength):
        ciphers.append(getNthLetters(i + 1,keylength,cipher))
    finalKey = calcBestChiLetters(ciphers,keylength)
    return convertToKey(finalKey)

def main():
    cipher = input()
    keylength = int(input())
    key = crack(cipher,keylength)
    print(key)
    decrypt(cipher,key)
    sys.exit()

if __name__ == "__main__":
    main()