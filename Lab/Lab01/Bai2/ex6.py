def fibonacci_with_recursive(n):
    if(n<0):
        return -1
    elif (n==0 or n==1):
        return n
    else:
        return fibonacci_with_recursive(n-1) + fibonacci_with_recursive(n-2)

list_fibonacci = []
n = int(input("Nhập số nguyên dương n: "))
for i in range(0, n+1):
    list_fibonacci.append(fibonacci_with_recursive(i))

print(f"Tổng của dãy {n} số fibonacci là {sum(list_fibonacci)}")