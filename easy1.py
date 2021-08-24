#length of last word

sentence=input("enter any sentence: ")
s=sentence.split()
i=-1
while i>-len(s):
    j=0
    c=0
    while j<len(s[i]):
        c+=1
        j+=1
    break
print(c)

