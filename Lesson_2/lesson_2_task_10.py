def bank(x, y):
    for i in range(y):
        x = x * 1.1
    return x
print(bank(100, 5))
