pltxt_alp1, pltxt_alp2= 'abcdefghijklm12865','nopqrstuvwxyz47390'
input_string = 'GLOBAL Hello world for test string 2021-12-29 Thursday'
key = 7

def shiftOrder(pltxt_alp, key = key):
    shifted = []
    indxcounter = 0
    while True:
        if indxcounter >= len(pltxt_alp)-key:
            key, indxcounter = 0, 0
        shifted.append(pltxt_alp[indxcounter+key])
        indxcounter+=1
        if len(shifted) == len(pltxt_alp):
            return "".join(shifted)




def encrypt(input=input_string):
    pltxt_alpA = shiftOrder(pltxt_alp1)
    pltxt_alpB =shiftOrder(pltxt_alp2)
    cptxt = ""
    for char in input:
        if char in pltxt_alp1:
            indx  = pltxt_alp1.find(char)
            cptxt += pltxt_alpB[indx]
        elif char in pltxt_alp2:
            indx = pltxt_alp2.find(char)
            cptxt += pltxt_alpA[indx]
        elif char.upper() in pltxt_alp1.upper():
            indx = pltxt_alp1.upper().find(char.upper())
            cptxt += pltxt_alpB.upper()[indx]
        elif char.upper() in pltxt_alp2.upper():
            indx = pltxt_alp2.upper().find(char.upper())
            cptxt += pltxt_alpA.upper()[indx]
        elif char == ' ':
            cptxt += ' '
        else:
            cptxt += char
    return cptxt
    print(cptxt)


def decrypt(cptxt = encrypt()):
    pltxt = ""
    pltxt_alpA = shiftOrder(pltxt_alp1)
    pltxt_alpB = shiftOrder(pltxt_alp2)

    for char in cptxt:
        if char in pltxt_alpA:
            indx = pltxt_alpA.find(char)
            pltxt += pltxt_alp2[indx]
        elif char in pltxt_alpB:
            indx = pltxt_alpB.find(char)
            pltxt += pltxt_alp1[indx]
        elif char.upper() in pltxt_alpA.upper():
            indx = pltxt_alpA.upper().find(char.upper())
            pltxt += pltxt_alp2[indx].upper()
        elif char.upper() in pltxt_alpB.upper():
            indx = pltxt_alpB.upper().find(char.upper())
            pltxt += pltxt_alp1[indx].upper()
        elif char == " ":
            pltxt += ' '
        else:
            pltxt += char
    return pltxt
    print(pltxt)


enctxt = encrypt()
dectxt = decrypt()

print(f'\n Input string: {input_string} \
    \n\n Encrypted: {enctxt} \
    \n\n Decrypted: {dectxt}\n')

