## Given a string s, find the length of the longest substring without repeating characters

s="abcabcbb"
a=" "
count=0
i=0
while i<len(s):
    if s[i] not in a:
        a=a+s[i]
        count+=1
    i+=1
print(count,a)

