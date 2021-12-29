pltxt_alp = 'abcdefghijklmnopqrstuvwxyz'
fstrot13,sndrot13 = pltxt_alp[:14],pltxt_alp[14:]

def encrypt(input="hello world"):
    cptxt = ""
    for elem in input:
        if elem in fstrot13:
            indx = fstrot13()
            cptxt += cptxt + fstrot13[indx]
        elif elem in sndrot13:
            cptxt += cptxt + sndrot13[indx]
    print(cptxt)

encrypt()