


def print_numbers(n):
    res = ''
    for i in range(1,n+1):
        res += str(i)+' '
        
    return res


def floyd_triangle():
    
    rows = int(input("Enter row number: "))
    n = 1
    
    for i in range(1,rows+1):

        print(' '*(rows - i) + print_numbers(n))
        n += 1



floyd_triangle()


