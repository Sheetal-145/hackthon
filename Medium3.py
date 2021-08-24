##sorting in ascending order

n=[-4,2,0,1,3,6]
i=0
while i<len(n):
    j=0
    while j<len(n):
        if n[i]<n[j]:
            n[i],n[j]=n[j],n[i]
        j+=1
    i+=1
print(n)
