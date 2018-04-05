
def print_numbers(n,x):
    res = ''
    for i in range(x,x+n):
        res += str(i)+' '
        
    return res


def floyd_triangle():    
    
    
    rows = int(input("Enter row number: "))
    n = 1
    x = 1
    
    for i in range(1,rows+1):

        print(' '*(rows - i) + print_numbers(n,x))
        n += 1
        x += 1



#floyd_triangle()

a = 10
b = 5

a = a + b
b = a - b
a = a - b
print(str(a)+" "+str(b))



