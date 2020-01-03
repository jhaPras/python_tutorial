#items = [(i,j) for i in range(20) for j in range(20) if i%2==0 and if j%3==0]

n = int(input())
arr = list(set([input() for i in range(n)]))
print(arr)
arr.sort()
print(arr[-2])
