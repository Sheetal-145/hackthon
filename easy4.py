##Count of prime number till 10

i=1
c=0
while i<=10:
    j=1
    fac=0
    while j<=i:
        if i%j==0:
            fac=fac+1
        j+=1
    if fac==2:
        c+=1
        print(i)
    i+=1
print("Total count is" ,c)
