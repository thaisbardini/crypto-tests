__author__ = 'thais'
def pollard(n, B):
    a = 2
    for j in range(2, B+1):
        a = (a**j) % n
        print "a: ", a

    d = gcd(a-1,n)
    print "d:", d
    if 1<d<n:
        return d
    else:
        return 0

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

def rho(n):
    x = 2
    y = 2
    d = 1
    i=1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
        print x, y, d, i
        i = i+1
    if d==n:
        return 0
    else:
        return d


def f(x):
    return ((x**2)+1) % n

#B = 15
#n = 9478477
#print(pollard(n, B))

n = 170508763
print rho(n)