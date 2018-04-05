
import sys

def timeConversion(s):
    # Complete this function
    
    if 'AM' in s:
        s = s.replace('AM','')
        return s
    else:
        tm_str = s.replace('PM','')
        tm = tm_str.split(':')
        hr = int(tm[0])
        
        if hr < 12:
            hr +=12
        
        return str(hr)+':'+tm[1]+':'+tm[2]
        
        elif hr == 12:
            return str(00)+':'+tm[1]+':'+tm[2]
        
        
        

s = input().strip()
result = timeConversion(s)
print(result)