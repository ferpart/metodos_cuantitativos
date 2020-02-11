n = int(input() or "0")
x = input() or "0"
x = x.split(" ")
x = [int(i) for i in x]
x.sort()
n=len(x)

def mean(x,n):
    r = 0
    if (len(x)==1 and x[0]==0):
        return r
    for i in range(n):    
        r+=x[i]
    return round(r/n, 1)

def median(x,n):
    r = 0
    if (n==0):
        return r
    if(n%2==0):
        r=(x[int(n//2)-1]+x[int(n//2)])/2
    else:
        r=x[int(n/2)]
    return round(r, 1)

def mode(x,n):
    count = 0
    index = 0
    if (len(x)==1 and x[0]==0):
        return 0

    for i in range(n):
        if (x.count(x[i]) > count):
            count = x.count(x[i])
            index = i
    return x[index]

print(mean(x,n))
print(median(x,n))
print(mode(x,n))