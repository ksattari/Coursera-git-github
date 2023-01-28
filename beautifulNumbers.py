# -*- coding: utf-8 -*-
"""
Spyder Editor

@author Khashayar Sattari

prints YES x, with x being the first number in the sequence.
if the input string is a beautiful number else prints NO

"""

def separateNumbers(s):
    m = len(s) // 2
    first = None
    for d in range(m):
        beautiful = True
        x = 0
        first = int(s[x:x+d+1]) 
        while x+2+2*d <= len(s):
            if s[x:x+d+1].startswith('0') and len(s[x:x+d+1]) > 1 or s[x+d+1:x+2+2*d].startswith('0'):
                beautiful = False
            if beautiful and int(s[x+d+1:x+2+2*d]) - int(s[x:x+d+1]) == 1:
                x = x+d+1     
            elif beautiful and int(s[x+d+1:x+3+2*d]) - int(s[x:x+d+1]) == 1:
                d = len(s[x+d+1:x+3+2*d])-1
                x = x+d
            else:   
                beautiful = False
                first = None
                break
        if beautiful and  x+d >= len(s)-1:
            break
    if beautiful:
        print("YES %d" %first)
    else:
        print("NO")
            
if __name__ == '__main__':
    
    separateNumbers('123456789010123456789011')
    separateNumbers("429496729542949672964294967297")
    separateNumbers("429496729542949672974294967296")
    separateNumbers("429496729542949672964294967287")
    separateNumbers("429496729542949672964294967197")
    separateNumbers("42949672954294967296429496729")
    separateNumbers("42949672954294967296429496729")
    separateNumbers("429496729500000000000000000001")
    separateNumbers("42949672950123456789")
    separateNumbers("4294967295000010020030000456789")
    separateNumbers("4294967295000102003004005")
   
   
          
   