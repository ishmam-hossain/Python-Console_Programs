
def count_char(s):
    
    dic = {}
    
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    
    return dic


def calculate_vals(s1, s2):
    
    dic1 = count_char(s1)
    dic2 = count_char(s2)
    
    for k in dic1:
        if k in dic2:            
            diff = abs(dic1[k] - dic2[k])
                       
            if diff > 0:
                print('Delete: '+ str(diff) + ' ' + k)
        else:
            print('Delete: '+ str(dic1[k]) + ' ' + k)


def check_anagram(s1, s2):
    
    calculate_vals(s1, s2)


s1 = input("Enter the first string: ").replace(' ','')
s2 = input("Enter the second string: ").replace(' ','')

print("\nTo make Anagram of these two strings: ")

check_anagram(s1, s2)




