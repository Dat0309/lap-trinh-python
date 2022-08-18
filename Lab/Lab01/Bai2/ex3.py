from numpy import intp
from urllib3 import Retry


def isPrimeNum(i,o):
    if(o<2 or i < 2):
        return False
    for n in range(i,o+1):
        if o%n==0:
            print(n)

i = int(input("Nhap so nguyen duong i = "))
o = int(input("Nhap so nguyen duong n = "))

isPrimeNum(i,o)