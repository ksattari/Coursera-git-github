"""
Sums up a binary tree's (represented as an array) left and right branches and returns
Left, Right or "", based on which side has greater sum,
or nothing if array is empty or has only one node.
"""
#time complexity O(nlogn)
def solution(arr):
    # Type your solution here 
    lsp = 1 #level start position
    left = right = 0
    x = 1 #level

    while lsp < len(arr):
      half = 2**x // 2 #halfway point based on tree level
      mid = lsp+half if lsp+half < len(arr) else len(arr)
      end = lsp + 2*half if lsp + 2*half < len(arr) else len(arr)
      for i in range(lsp,mid):
        left  = left if arr[i] == -1 else left + arr[i]
      for i in range(mid,end):
        right  = right if arr[i] == -1 else right + arr[i]
      lsp = lsp + 2**x
      x += 1
      
    if len(arr) <= 1 or left == right:
      return ""
    elif left > right:
      return "Left"
    return "Right"

print(solution([3,2,1]))
