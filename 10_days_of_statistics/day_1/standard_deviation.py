from math import sqrt, pow

n = int(input() or "0")
x = input() or "0"

x = x.split(" ")
x = [int(i) for i in x]

def mean(n, x):  
    r=sum(x)
    return round(r/n, 1)

def standard_deviation(n, x):
    if (n!=0):
        avg = mean(n,x)
        summatory = 0
        for i in range(n):
            summatory+=(pow((x[i]-avg), 2))
        return float(round(sqrt(summatory/n), 1))
    return

print (standard_deviation(n,x))