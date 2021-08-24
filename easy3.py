##Output: [1,1,2,3,4,4]

l1 = [1,2,4]
l2 = [1,3,4]
a=[]
i=0
while i<len(l1) and len(l2):
    a.append(l1[i])
    a.append(l2[i])
    i+=1
print(a)


