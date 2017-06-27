#Project Euler
#Problem 1
def mult3and5():
    ans=0
    for each in range(1000):
        if each%3==0 or each%5==0:
            ans += each
    return ans
print mult3and5()

#Problem 2
def evenfib():
    ans = 0
    x = 0
    a=0
    b=1
    while x < 4000000:
        if a%2==0:
            ans += a
        if b%2==0:
            ans += b #adds the values twice
        if x%2 == 0:
            a += b
        else:
            b += a
        if a >= 4000000 or b >= 4000000:
            x = max(a,b)
        x += 1
    return ans
print evenfib()
