def fib(n):
    f1 = 1
    f2 = 2
    fn = 3
    if n < 0:        
        print("Khong the tao duoc day Fibonacci")
        return n
    elif (n == 0):
        return 1
    elif n == 1:
        return 2
    else:
        for i in range(2, n):
            f1 = f2
            f2 = fn
            fn = f1 + f2
        return fn
n = int(input("Nhap n: "))
for i in range(0, n):
    print(fib(i))