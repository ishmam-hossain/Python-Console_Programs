import random as rnd

n = 510

j = 0

for i in range(n):
    
    r = rnd.randint(1,2)  
    if r==1:
        print('/',end='')
    else:        
        print('\\',end='')
    #ʚ ɷ
    j += 1
    
    if j > 50:
        j = 0
        print()
    