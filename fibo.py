n = int(input("Enter how many Fibonacci numbers to print: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print() 