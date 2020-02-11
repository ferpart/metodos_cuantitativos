n = int(input() or "0")
x = input() or "0"
w = input() or "0"

x = x.split(" ")
x = [int(i) for i in x]

w = w.split(" ")
w = [int(i) for i in w]

def list_expander_sorted(n,x,w):
    if (n!=0):
        final_list=[]
        for i in range(n):
            for _ in range(w[i]):
                final_list.append(x[i])
        final_list.sort()
        return final_list
    return

def interquartile_range(n, x):
    if (n!=0):
        if(n%2==0):
            return float(
                median(int(n/2),x[int(n/2):])-
                median(int(n/2),x[:int(n/2)]))
        else:
            return float(
                median(int(n//2),x[int(n//2)+1:])-
                median(int(n//2),x[:int(n//2)]))
    return

def median(n, x):
    r = 0
    if(n%2==0):
        r=(x[int(n//2)-1]+x[int(n//2)])/2
    else:
        r=x[int(n/2)]
        
    return round(r, 0)

print(interquartile_range(len(list_expander_sorted(n,x,w)), 
    list_expander_sorted(n,x,w)))
