def pseudo_rand(x):
    a = 1000
    b = 12
    m = 2 ** 31
    new_x = (a * x + b) % m
    return new_x

seed = 100
x = pseudo_rand(seed)
print(x)
x = pseudo_rand(x)
print(x)
