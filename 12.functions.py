def say_hello():
    print("hello world")


say_hello()


def calculate_factorial(a):
    s = 1
    for x in range(1, a + 1):
        s *= x
    return s

print(calculate_factorial(4))

n= 5
r=2
v = calculate_factorial(n) / (calculate_factorial(r)* calculate_factorial(n-r))
print(v)
