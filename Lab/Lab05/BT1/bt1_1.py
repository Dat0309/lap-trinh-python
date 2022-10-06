from lib2to3.pgen2 import driver
from msilib.schema import Error
import pyodbc

def mktable(dic, header=None):
    # get max col width
    col_widths = list(map(max, zip(*(map(lambda x: len(str(x)), (k,*v))
                                     for k,v in dic.items()))))

    # default numeric header if missing
    if not header:
        header = range(1, len(col_widths)+1)
    
    header_widths = map(lambda x: len(str(x)), header)
    
    # correct column width if headers are longer
    col_widths = [max(c,h) for c,h in zip(col_widths, header_widths)]
    
    # create separator line
    line = '+%s+' % '+'.join('-'*(w+2) for w in col_widths)
    #line = '-' * (sum(col_widths)+(len(col_widths)-1)*3+4)
    
    # create formating string
    fmt_str = '| %s |' % ' | '.join(f'{{:<{i}}}' for i in col_widths)
    
    # header
    print(line)
    print(fmt_str.format(*header))
    print(line)
    
    # data
    for k, v in dic.items():
        print(fmt_str.format(k, *v))
    
    # footer
    print(line)

def get_connection():
    conn = pyodbc.connect(driver='{SQL Server}',host='.\SQLEXPRESS', database='QLSinhVien',
                      trusted_connection='yes',encrypt='no')
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        print("Danh sach cac lop: ")
        for row in records:
            print("*"*50)
            print("Ma lop: ", row[0])
            print("Ten lop: ", row[1])
            
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)
        
def get_all_class_with_format():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        select_sinhVien = "select * from SinhVien"
        cursor.execute(select_sinhVien)
        records_sv = cursor.fetchall()
        print("Danh sach tat ca sinh vien la: ")
        student_dict = {}
        
        for row in records_sv:
            student_dict[row[0]]["id"]=row[0]
            student_dict[row[0]]["hoTen"]=row[1]
            student_dict[row[0]]["MaLop"]=row[2]
            for lop in records:
                if(row[2] == lop[0]):
                    student_dict[row[0]]["Ten lop"]=lop[1]
            close_connection(connection)
            
        mktable(student_dict, header=('Ma so', 'Ho ten', 'Ma lop', 'Ten lop'))
    except(Exception, pyodbc.Error) as error:
        print("Da co loi xay ra khi thuc thi. Thong tin loi: ", error)
        
get_all_class_with_format()

