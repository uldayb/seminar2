def first(x):
    try:
        return a[x]
    except SyntaxError:
        return "wrong syntax"
    except IndexError:
        return "no such index"
    except FloatingPointError:
        return "re-enter number"

a=[12,0,-8,9,12,45,96,18]
n=int(input())
print(first(n))
    
