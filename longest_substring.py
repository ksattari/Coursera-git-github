
s = 'abaabcdefghijaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
start = 0
if len(s) > 0:
    longestSub = s[0]
else:
    longestSub = "no input"
for x in range(1,len(s)):
    if s[x-1] > s[x]:
       longestSub = s[start:x] if len(s[start:x]) > len(longestSub) else longestSub
       start = x
    
longestSub = s[start:len(s)] if len(s[start:len(s)]) > len(longestSub) else longestSub
print('Longest substring in alphabetical order is: %s' %longestSub)
