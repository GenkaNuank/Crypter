def encrypt(key,nText):
    encryptedNumber = []
    klength = len(key)
    i = 0
    n = 0
    while i < len(nText):
        encryptedNumber = encryptedNumber + [(int(key[n]) + int(nText[i])) % 32]
        if klength == (n+1):
            n = 0
        else:
            n += 1
        i += 1
    return encryptedNumber

def decrypt(key,cipher):
    decryptedNumber = []
    kLength = len(key)
    i = 0
    n = 0
    while i < len(cipher):
        decryptedNumber = decryptedNumber + [round(((int(cipher[i]) - int(key[n]))) % 32)]
        if kLength == (n+1):
            n = 0
        else:
            n += 1
        i += 1
    return decryptedNumber
