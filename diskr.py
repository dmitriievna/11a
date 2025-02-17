
    
    #diskriminants
    
def rootFinder(a=0,b=0,c=0):
    D = b**2 - 4*a*c
    x1 = (-b - D**0.5)/(2 * a)
    x2 = (-b + D**0.5)/(2 * a)
    return x1,x2

s1,s2 =rootFinder(3,4,1)
print(s1,s2)


   #y = (2x + 3)/0.5

def y(x):
    result = (2 * x + 3)/ 0.5
    return result
    