##OP=123

n = [1,1,2,3,3]
i=0
a=[]
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    i+=1
print(a)

    
