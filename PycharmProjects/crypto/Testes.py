__author__ = 'thais'
#Pollard p-1 algorithm
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
    
#Pollard rho algorithm
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

#Tests for Pollard p-1
#B = 15
#n = 9478477
#print(pollard(n, B))

#Tests for Pollard rho
n = 170508763
print rho(n)
