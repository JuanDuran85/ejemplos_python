s = input("Frase: ")
s = s.lower()
words = s.split(" ")
palindroms = set()
for w in words:
    isPalindrom = True
    l = []
    for c in w:
        l.append(c)
    n = len(l)
    for i in range(int(n / 2)):
        if l[i] != l[n - (i + 1)]:
            isPalindrom = False
    if isPalindrom:
        palindroms.add(w)   
print(palindroms)
