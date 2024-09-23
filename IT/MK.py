def w1():
    print("Викликана 1 функція")
    return True

def w2():
    print("Викликана 2 функція")
    return False

result1 = w1() and w2()
print("Результат:", result1)
result2 = w1() or w2()
print("Результат:", result2)
