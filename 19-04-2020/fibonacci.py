def fibo(n):
    a = 0;
    b = 1
    if a == n:
        print(a)
    elif b==n:
        print(a, b, end=" ")
    else:
        print(a, b, end=" ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end=" ")

n = int(input("Enter your fibonacci rang: "))
fibo(n)