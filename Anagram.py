

def check_anagram_by_sorting():
    
    if sorted(frst) == sorted(sec):
        return "Anagram!"


def check_anagram(frst, sec):

    if len(frst) != len(sec):
        return "Not an anagram!"
    
    else:
        
        for c in frst:
            if c not in sec:
                return "Not an anagram!"
        
        return "Anagram!"
            
        

frst = input("Enter first string: ").strip().lower()
sec = input("Enter second string: ").strip().lower()    
    
print(check_anagram(frst, sec))
print(check_anagram_by_sorting(frst, sec))
