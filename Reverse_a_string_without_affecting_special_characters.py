

s = list('a!bcd.e*f/g?h')

r = []
indices = []


for c in s[::-1]:
    if c.isalpha():
        r.append(c)
    else:
        indices.append(s.index(c))
        continue

for i in indices[::-1]:
    r.insert(i,s[i])


print(''.join(s) + ' ---'+ str(len(s)))
print(''.join(r) + ' ---'+ str(len(r)))
