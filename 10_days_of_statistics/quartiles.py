n = int(input() or "0")
x = input() or "0"

x = x.split(" ")
x = [int(i) for i in x]
x.sort()


def quartile(n, x):
    if (n!=0):
        if(n%2==0):
            median(int(n/2),x[:int(n/2)])
            median(n, x)
            median(int(n/2),x[int(n/2):])
        else:
            median(int(n//2),x[:int(n//2)])
            median(n, x)
            median(int(n//2),x[int(n//2)+1:])
    return

def median(n, x):
    r = 0
    if(n%2==0):
        r=(x[int(n//2)-1]+x[int(n//2)])/2
    else:
        r=x[int(n/2)]
        
    print(int(round(r, 0)))

quartile(n,x)
