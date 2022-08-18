import math
from os import system
from turtle import rt

from numpy import append

list = [2,5,9,20,10,11,13,14,8]

def check_perfect_square (m):
    n = int (math.sqrt (m)) 
    return n * n == m 

def check_fibo (m ): 
    return check_perfect_square (5 * m * m + 4) or check_perfect_square (5 * m * m - 4) 

def XuatSoLeKhongChiaHetCho5(list):
    sb=""
    for i in list:
        if i%5!=0:
            sb = sb + str(i) + ""
    print(sb) 
            
def XuatTatCaFibonacci(list):
    sb = ""
    for i in list:
        if check_fibo(i) == True:
            sb = sb + str(i) + ","
    print(sb)
    
def TimSoNguyenToLonNhat(list):
    result = []
    for i in list:
        if i<2:
            return False
        if i%len(list)==0:
            result.append(i)
    max(result)

while True:
    print('Chọn chức năng muốn thực hiện: ')
    print('Nhập 1: Xuât tất cả các số lẻ không chia hết cho 5')
    print('Nhập 2: Xuất tất cả các số Fibonacci')
    print('Nhập 3: Tìm số nguyên tố lớn nhất')
    print('Nhập 4: Tìm số Fibonacci bé nhất')
    print('Nhập 5: Tính trung bình các số lẻ')
    print('Nhập 6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
    print('Nhập 7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
    print('Nhập 8: Đảo ngược trật tự các phần tử của danh sách')
    print('Nhập 9: Xuất tất cả các số lớn thứ nhì của danh sách')
    print('Nhập 10: Tính tổng các chữ số của tất cả các số trong danh sách')
    print('Nhập 11: Đếm số lần xuất hiện của một số trong danh sách')
    print('Nhập 12: Xuất các số xuất hiện n lần trong danh sách')
    print('Nhập 13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
    print('Nhập 14: Thoát chương trình')
    try:
        action = int(input())
        if action == 0:
            break
        elif type(action) != int:
            print('XIN MỜI NHẬP LẠI')
            action = int(input())
            system("CLS")
            print('Chọn chức năng muốn thực hiện: ')
            print('Nhập 1: Xuât tất cả các số lẻ không chia hết cho 5')
            print('Nhập 2: Xuất tất cả các số Fibonacci')
            print('Nhập 3: Tìm số nguyên tố lớn nhất')
            print('Nhập 4: Tìm số Fibonacci bé nhất')
            print('Nhập 5: Tính trung bình các số lẻ')
            print('Nhập 6: Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng')
            print('Nhập 7: Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ')
            print('Nhập 8: Đảo ngược trật tự các phần tử của danh sách')
            print('Nhập 9: Xuất tất cả các số lớn thứ nhì của danh sách')
            print('Nhập 10: Tính tổng các chữ số của tất cả các số trong danh sách')
            print('Nhập 11: Đếm số lần xuất hiện của một số trong danh sách')
            print('Nhập 12: Xuất các số xuất hiện n lần trong danh sách')
            print('Nhập 13: Xuất các số xuất hiện nhiều lần nhất trong danh sách')
            print('Nhập 14: Thoát chương trình')
    except:
        print('CHÚNG TÔI HIỆN CHƯA PHÁT TRIỂN TÍNH NĂNG ĐÓ, XIN MỜI NHẬP LẠI')
        action = 0

    match action:
        case 1:
            system("CLS")
            print('===========================')
            print("Xuât tất cả các số lẻ không chia hết cho 5")
            print('===========================')
            XuatSoLeKhongChiaHetCho5(list)
            print('===========================')

        case 2:
            system("CLS")
            print('===========================')
            print("Xuất tất cả các số Fibonacci")
            print('===========================')
            XuatTatCaFibonacci(list)
            print('===========================')

        case 3:
            system("CLS")
            print('===========================')
            print("Tìm số nguyên tố lớn nhất")
            print('===========================')
            TimSoNguyenToLonNhat()
            print('===========================')

        case 4:
            system("CLS")
            print('===========================')
            print("Thiết lập lại trạng thái visited của các đỉnh trên đồ thị")
            print('===========================')
            print('===========================')

        case 5:
            system("CLS")
            print('===========================')
            print("Kiểm tra 2 đỉnh có kề nhau hay không")
            print('===========================')
            print('===========================')

        case 6:
            system("CLS")
            print('===========================')
            print("Đọc đô thị từ file")
            print('===========================')
            print('===========================')
        case 7:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 8:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 9:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 10:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 11:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 12:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 13:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')
        case 14:
            system("CLS")
            print('===========================')
            print("Duyệt đồ thị theo chiều rộng")
            print('===========================')
            print('===========================')