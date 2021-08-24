##Reverse

sen=input("enter any sentence: ")
i=-1
a=sen.split()
b=" "
while i>=-len(a):
    b=b+" "+a[i]
    i=i-1
print(b)



