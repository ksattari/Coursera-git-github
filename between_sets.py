def between_sets(a,b):

    a.sort()
    b.sort()
    flag = False
    between = []
    
    for x in range(b[len(b)-1],a[len(a)-1] - 1, -1):
        print("x: ", x)
        for i in a:
            if x % i != 0:
                flag = True
                break
        if not flag:
            for j in b:
                if j % x != 0:
                    flag = True
                    break
        if not flag:
            between.append(x) 
        flag = False
    
    print(between)   
    return len(between)


if __name__ == '__main__':

    a = [2,6]
    b = [24,36]

    print(between_sets(a,b))
