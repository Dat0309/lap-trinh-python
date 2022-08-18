'''
Khong dung de quy
'''
def fibonacci_without_recursive(n):
    a=0;
    b=1;
    c=1;
    
    if(n<0):
        return -1
    else:
        for i in range(2,n):
            a = b
            b = c
            c = a + b
        return c
    
'''
Dung de quy
'''
def fibonacci_with_recursive(n):
    if(n<0):
        return -1
    elif (n==0 or n==1):
        return n
    else:
        return fibonacci_with_recursive(n-1) + fibonacci_with_recursive(n-2)
    
n = int(input("Nhap so nguyen duong n = "))
print(f"So fibonacci thu {n} khong dung de quy la: {str(fibonacci_without_recursive(n))}")

print(f"So fibonacci thu {n} dung de quy la: {str(fibonacci_with_recursive(n))}")

