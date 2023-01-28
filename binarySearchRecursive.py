# precondition: String is in lexical order
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
      return char == ""
    #if len(aStr) == 1:
    #   return char == aStr
    mid = len(aStr) // 2
    if char == aStr[mid]:
       return True
    elif char < aStr[mid]:
       return isIn(char, aStr[0:mid])
    else:
       return isIn(char, aStr[mid+1:])

if __name__ == '__main__':

   print(isIn('f'.lower(),'abcdeg'))
   print(isIn('Q'.lower(),'bcdefghijklmnopqrstuvwxyz'))
