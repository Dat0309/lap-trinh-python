def sumNFirstInteger(n):
    sum = 0
    for i in range(0,n+1):
        sum+=i**2
    return sum

n = int(input("Nhap so nguyen duong n = "))
print(sumNFirstInteger(n))