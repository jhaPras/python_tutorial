def findPairs(n,ar):

    print('level 1')
    d= {}

    print('Level 2')
    for v in ar:
        print('Level 3')
        if v not in d.keys():
            print('level 4')
            d[v] = 0
            print(d)
        else:
            d[v] += 1
            print('level 5')
        return d
    print('operation executed till this poit and the resulting dictionary is:', d)

##    for k,_ in d:
##        new = {}
##        if d[k] == 2:
##            new[k] = 1
##        else:
##            new[k] += 1
##        return new

    print(d)
        


c = 7

k = ['red','green','red','blue','black','green']

findPairs(c,k)
