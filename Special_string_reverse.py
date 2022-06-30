strSample=input()
listSample=list(strSample)
i=0
j=len(listSample)-1
while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        listSample[i],listSample[j]=listSample[j],listSample[i]
        i+=1
        j-=1
strOut='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'.join(listSample)
print(strOut)
