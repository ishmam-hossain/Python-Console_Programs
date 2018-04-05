"""
@author: Ishmam Hossain
@date and time: March 7, 2018 at 5:42 PM 
"""



def testing():
    eq = input("Enter: ")
    if not eq.startswith('-'):
        eq_ = list(map(float, eq.split('-')))
    else:
        eq = eq[1:]
        eq_ = list(map(float, eq.split('-')))
        eq_[0] *= -1
    
        print(eq_)


def multiples_of_3():
    
    for i in range(200,2,-1):
        
        if i % 3 == 0:
            print(i,end=' ')
    

def reverse_str(s):
    """
    It simply reverse the string char by char.
    """ 
    return s[::-1]


def reverse_str_words(s):
    """
    It's done with the split built in function.
    This program takes in a string and prints out the words in reverse order.
    
    eg.-
    input: "this program takes in a string and prints out the words in reverse order"
    output: "order reverse in words the out prints and string a in takes program this" 
    
    """     
    s = s.split(' ')    
    return ' '.join(s[::-1])



def reverse_str_words_manual(s): 
    
    """
    It's done without any built in function.
    This program takes in a string and prints out the words in reverse order.
    
    eg.-
    input: "this program takes in a string and prints out the words in reverse order"
    output: "order reverse in words the out prints and string a in takes program this" 
    
    """
    
    
    res = ''
    end = len(s) - 1
    strt = -5
    
    for i in range(len(s)-1, -1, -1):
                
        if s[i] == ' ':
            
            strt = i
             
            for x in range(strt,end+1):
                res += s[x]
            
            end = strt - 1
        
        if i == 0:
            res += ' '
            for x in range(0,end+1):
                res += s[x]        
    
    return res
    



#print(reverse_str_words_manual(input("Enter string: ").strip()))
testing()



