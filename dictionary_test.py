
s = input().replace(" ", "")

dic = {}

    
for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
        
print(dic)
sums = 0
for k in dic:
    sums += dic[k]
    
print(sums)    
    
