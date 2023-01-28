"""
given a 2n x 2n array. uses 4 corners approach to get the
maximum values in the top left n x n section
returns the sum of the n * n sections values
"""
def flip_matrix(matrix) -> int:

    s = len(matrix)
    n = s // 2
    maxval = 0
    total = 0
    for r in range(n):
        for c in range(n):
          maxval = max(matrix[r][c], matrix[s - (1+r)][c], matrix[s - (1+r)][s - (1+c)], matrix[r][s-(c+1)])
          total += maxval

    return total

if __name__ == "__main__":

    a = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
    b = ([1,4],[2,3])
    for x in a:
        print(x)
        
    print("Total is %d" %flip_matrix(a))

    
   
