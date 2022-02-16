from collections import Counter
def solution(data,n):
    c = Counter(data)
    r=filter(lambda x:c[x]<=n , data)
    return list(r)

r1=solution([1, 2, 3], 0)
assert len(r1)==0,'n=0 must return empty'
print(r1)

r2=solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
assert r2==[1,4],'incorrect solution in case 2'
print(r2)

