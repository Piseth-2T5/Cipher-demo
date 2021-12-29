pltxt_alp1, pltxt_alp2= 'abcdefghijklm12865','nopqrstuvwxyz47390'
input_string = 'Hello world for test string 2021-12-29 Wednesday'

def encrypt(input=input_string):
    cptxt = ""
    for char in input:
        if char in pltxt_alp1:
            indx  = pltxt_alp1.find(char)
            cptxt += pltxt_alp2[indx]
        elif char in pltxt_alp2:
            indx = pltxt_alp2.find(char)
            cptxt += pltxt_alp1[indx]
        elif char.upper() in pltxt_alp1.upper():
            indx = pltxt_alp1.upper().find(char.upper())
            cptxt += pltxt_alp2.upper()[indx]
        elif char.upper() in pltxt_alp2.upper():
            indx = pltxt_alp2.upper().find(char.upper())
            cptxt += pltxt_alp1.upper()[indx]
        elif char == ' ':
            cptxt += ' '
        else:
            cptxt += char
    return cptxt
    print(cptxt)


def decrypt(cptxt = encrypt()):
    pltxt = ""
    for char in cptxt:
        if char in pltxt_alp1:
            indx = pltxt_alp1.find(char)
            pltxt += pltxt_alp2[indx]
        elif char in pltxt_alp2:
            indx = pltxt_alp2.find(char)
            pltxt += pltxt_alp1[indx]
        elif char.upper() in pltxt_alp1.upper():
            indx = pltxt_alp1.upper().find(char.upper())
            pltxt += pltxt_alp2[indx].upper()
        elif char.upper() in pltxt_alp2.upper():
            indx = pltxt_alp2.upper().find(char.upper())
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