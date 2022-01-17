import sys
sys.setrecursionlimit(10000)
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
    print(f"Day Fibonacci duoc tao la: {fib(i)}")
test_cases = {
    50 : 12586269025,
    100 : 354224848179261915075,
    590 : 897889194859191704881857622613605161659692872156509128465291624947856903121114331700554055405737435019936805984303748490745
}
for case in test_cases.keys():
    if (fib(case) != test_cases[case]):
        print("FAIL")
        exit()
print("OK")


# get fibonacci n-th
# fib(1) = 1
# fib(2) = 2
# fib(n) = fib(n-1) + fib(n-2)