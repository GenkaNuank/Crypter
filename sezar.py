password = [7,29,12,21,5,19,2,11,28,16,10,1,15,24,8,25,4,13,20,18,14,3,17,22,9,23,26,27,6]
def encrypt(a):
    cipher = []
    i = 0
    n = 0
    while i < len(a):
        while n < len(password):
            if int(a[i]) == (n+1):
                cipher = cipher + [password[n]]
                i += 1
                n = 0
                break
            else:
                n += 1
    return cipher
def decrypt(a):
    solve = []
    i = 0
    n = 0
    while i < len(a):
        while n < len(password):
            if int(a[i]) == int(password[n]):
                solve = solve + [(n+1)]
                i += 1
                n = 0
                break
            else:
                n += 1
    return solve
