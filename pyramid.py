
def pyramid():
    
    rows = int(input("Enter row number: "))
    _ch = input("Enter the char: ")        
    
    for i in range(rows):
        print (' '*(rows-i-1) + _ch*(2*i+1))  
        


pyramid()     






