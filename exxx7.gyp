S=str(input('Introduceti sirul cu caractere: '))
print(S)
a=0
for i in S:
    if i=='A':
        a+=1

print('Numarul de aparitii a caracterului "A"= ',a)
C=S.replace('A','*')
print('Sirul obtinut prin substituirea caracterului "A" prin caracterul "*" este = ',C)

D=S.replace('B','')
print('Sirul obtinut prin radierea caracterului "B" este = ',D)


a=S.count('MA')
print('Numarul de aparitii a silabei "MA" este = ',a)

E=S.replace('MA','TA')
print('Sirul obtinut prin substituirea silabei "MA" prin silaba "TA" este = ',E)

F=S.replace('TO','')
print('Sirul obtinut prin radierea silabei "TO" este = ',F)

print('Sirul scris invers= ',S[::-1])