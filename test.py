
s = 'abcbcd'
start = 0
if len(s) > 0:
    longestSub = s[0]
else:
    longestSub = ""
for x in range(1,len(s)):
    if s[x-1] > s[x]:
       start = x
    else:
        longestSub = s[start:x+1] if len(s[start:x+1]) > len(longestSub) else longestSub
      
    
print('Longest substring in alphabetical order is: %s' %longestSub)
