#1.uzd izvada sveicinājumu
def Sveika(name):
    print(f'Sveika,{name}!')
    
Sveika("Violeta")
    
#2.uzd atgriež divu skaitļu summu (izvadas 8)
def sum_numbers(a, b):
    result = a+b
    return result

print(sum_numbers(5,3))

#3.uzd true false
def is_even(n):
    return n % 2 ==0

result_4 = is_even(4)
result_7 = is_even(7)

print("4", result_4)
print("7", result_7)

#4.uzd apreķ/ina dotā skaitļa faktoriāllu
def factorial(n):
    result = 5 * 4 * 3 * 2 * 1
    return result

print(factorial(5))
