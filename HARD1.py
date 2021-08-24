#Output: [1,1,2,3,4,4,5,6]

n = [[1,4,5],[1,3,4],[2,6]]
i=0
a=[]
while i<len(n):
    if type(n[i])==list:
        j=0
        while j<len(n[i]):
            a.append(n[i][j])
            j+=1
    i+=1
s=0
while s<len(a):
    k=0
    while k<len(a):
        if a[s]<a[k]:
            a[s],a[k]=a[k],a[s]
        k+=1
    s+=1
print(a)

        

