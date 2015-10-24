alphabet = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","y","z","x","q","w"]

def mNumber(a):
    number = []
    i = 0
    n = 0
    while i < len(a):
        while n < len(alphabet):
            if a[i] == alphabet[n]:
                number = number + [(n+1)]
                i += 1
                n = 0
                break
            else:
                n += 1
    return number
def mText(a):
    text = []
    i = 0
    n = 0
    while i < len(a):
        while n < len(alphabet):
            if a[i] == (n+1):
                text = text + [alphabet[n]]
                i += 1
                n = 0
                break
            else:
                n += 1
    return text
