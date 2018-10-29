# fibonacci series
def function(n):
    result=[0,1]
    a=0
    b=1
    for i in range(0,n-1):
        b = a + b
        a = b - a
        result.append(b)
    return result, sum(result)

print(function(4))
