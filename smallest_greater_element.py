real = [ 6, 3, 9, 8, 10, 2, 1, 15, 7 ]
#real = [13, 6, 7, 12]
#real = [ 1, 1, 2, 3, 4, 5, 6, 7, 8 ]

duplic = sorted(real)
res = ''


for i in real:
    if duplic.index(i) + 1 < len(duplic):
        ind = duplic.index(i)+1
        res += str(duplic[ind]) + ' '

    else:
        res += '- '

print(res)

# expected output: 7 6 10 9 15 3 2 - 8
# actual output:   7 6 10 9 15 3 2 _ 8