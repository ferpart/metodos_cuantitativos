n = int(input() or "0")
x = input() or "0"
w = input() or "0"

x = x.split(" ")
x = [int(i) for i in x]

w = w.split(" ")
w = [int(i) for i in w]

def weighted_mean(n, x, w):
    upper = 0
    lower = 0
    if (n!=0):
        for i in range(n):
            upper+=(x[i]*w[i])
            lower+=w[i]
        return float(round(upper/lower, 1))
    return 0

print (weighted_mean(n,x,w))