from random import randint, choice, random


def select_random_char_from_list():
    
    alphas = ['a', 'f', 'Z', 'r', 'i', 'R', 'X', 'M', 'j', 'o']
    
    num = int(input("Enter number of chars: "))
    res =''
    
    for i in range (1,num+1):
        indx = randint(0,len(alphas)-1)
            
        res += str(alphas[indx])        
        
    return res


def make_random_chars():
    
    res = ''
    
    for i in range(3):
        r = choice([(65,90),(97,122)])
        res += chr(randint(*r))
    
    return res


#print('The Result is: ' + make_random_chars())


print(select_random_char_from_list())