input_string = 'this just test string but it is real string'
key = '632415'
fill = 'a'
def encrypt(key=key, input=input_string):
    plainttxt = input.replace(" ","*")
    positionedtxt, pos_ciphertxt, ciphertxt=[],[],[]
    key_length = len(key)
    iteration = len(plainttxt)//key_length + len(plainttxt)%key_length
    for j in range(iteration):
        start,end = key_length * j, key_length * j + key_length
        positionedtxt.append(plainttxt[start:end])
        if positionedtxt[j] == "":
            del positionedtxt[j]
            break
        if len(positionedtxt[j]) < len(positionedtxt[0]):
            gap = len(positionedtxt[0]) - len(positionedtxt[j])
            positionedtxt[j]+= fill*gap

    for text in positionedtxt: #012345 632415 thisis
        text = " " + text
        for i in range(len(key)):
            pos_ciphertxt.insert(i, text[int(key[i])])  #
        ciphertxt.append("".join(pos_ciphertxt[:]))
        del pos_ciphertxt[:]
    return "".join(ciphertxt)


def decypt(key=key, ciphertxt=encrypt()):
    txt, pltxt, pos_pltxt= [],[],[]
    itr = len(ciphertxt)//len(key) + len(ciphertxt)%len(key)
    for i in range(itr):
        start, end = len(key)*i , len(key)*i + len(key)
        txt.append(ciphertxt[start:end])

    for elem in txt: #632415  thisis sihsti 
        elem = " " + elem
        for i in range(1,len(key)+1):
            pltxt.insert(i,elem[key.index(str(i))+1])
        pos_pltxt.append("".join(pltxt))
        del pltxt[:]
        num = len(ciphertxt) - len(input_string)
    result = "".join(pos_pltxt)
    final_res = result.replace(fill*num,"")
    return final_res.replace('*', " ")

ciphertxt = encrypt()
plaintxt = decypt()
print(f'\nInput string: \n=> "{input_string}"\
        \n\nEncrypted: \n=> "{ciphertxt}"\
        \n\nDecrypted: \n=> "{plaintxt}" ')