import change
import sezar
import vigenere

print("######################")
print("------Cyrpter1.0------")
print("######################")

def test(number, cipher, key):
    i = 0
    print("Decrypting the code process is getting started...")
    solve = vigenere.decrypt(key, sezar.decrypt(cipher))
    while i <= len(number):
        if i == len(number):
            print("Mission complated")
            break
        elif i < len(number) and number[i] == solve[i]:
            i += 1
        else:
            print("Mission failed")
            break

text = input("Enter the text:")
number = change.mNumber(text)
key = input("Enter the key:")
nKey = change.mNumber(key)
cipher = sezar.encrypt(vigenere.encrypt(nKey, number))
test(number, cipher, nKey)
