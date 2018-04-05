
row = int(input("Enter row:  "))
num = 1
row += 3


for i in range(3,row):
    print(' '*(row-i+1),end='')
    
    for s in range(2,i):
        
        print(str(num),end=' ')
        num += 1

    
    print()
        
