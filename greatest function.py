def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "All are equal"
#main program
answer = greatest(10,20,2)
print(answer)
