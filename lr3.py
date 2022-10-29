text = input().lower()
beforeTCHKA = text.split('.')[0]
alf = []
for i in range(97,123):
    alf.append(chr(i))

kmax=0
letter=''
for i in range(26):
    if beforeTCHKA.count(alf[i])>kmax:
        kmax= beforeTCHKA.count(alf[i])
        letter = alf[i]
print(letter, kmax)
