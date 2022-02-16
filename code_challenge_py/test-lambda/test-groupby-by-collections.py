from collections import Counter
ar=[1,1,1,1,2,2,2,3,3,4]
c = Counter(ar)
print(c)
def f1(x):
    print(x,c[x])
    return x
r=filter(lambda x:c[x]<=2 , ar)
# r=map(f1 , ar)
print(list(r))
