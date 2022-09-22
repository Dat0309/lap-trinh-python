from tkinter import *
from tkinter.ttk import Combobox

if __name__ =="__main__":
    root = Tk()

    root.configure(background='light green')
    root.title('ĐĂNG KÝ HỌC PHẦN')
    root.geometry('800x500')
    
    id = StringVar()
    name = StringVar()
    dob = StringVar()
    email = StringVar()
    phone = StringVar()
    course = StringVar()
    year = StringVar()
    sub = StringVar()
    
    title = Label(root, text='THÔNG TIN ĐĂNG KÝ HỌC PHẦN', fg='Red', bg='light green', font=("Arial", 20))
    
    id_lb = Label(root, text='Mã số sinh viên', bg='light green')
    name_lb = Label(root, text='Họ tên', bg='light green')
    dob_lb = Label(root, text='Ngày sinh', bg='light green')
    email_lb = Label(root, text='Email', bg='light green')
    phone_lb = Label(root, text='Số điện thoại', bg='light green')
    course_lb = Label(root, text='Học kỳ', bg='light green')
    year_lb = Label(root, text='Năm học', bg='light green')
    sub_lb = Label(root, text='Môn học', bg='light green')
    
    id_field = Entry(root,width=60, font=('Arial 11'), textvariable=id)
    name_field = Entry(root,width=60, font=('Arial 11'), textvariable=name)
    dob_field = Entry(root,width=60, font=('Arial 11'), textvariable=dob)
    email_field = Entry(root,width=60, font=('Arial 11'), textvariable=email)
    phone_field = Entry(root,width=60, font=('Arial 11'), textvariable=phone)
    course_field = Entry(root,width=60, font=('Arial 11'), textvariable=course)
    year_field = Combobox(root,width=58, font=('Arial 11'), textvariable=year)
    
    title.place(relx=0.5, rely=0.1,anchor=CENTER)
    id_lb.place(relx=0.1,rely=0.15)
    name_lb.place(relx=0.1,rely=0.2)
    dob_lb.place(relx=0.1,rely=0.25)
    email_lb.place(relx=0.1,rely=0.3)
    phone_lb.place(relx=0.1,rely=0.35)
    course_lb.place(relx=0.1,rely=0.4)
    year_lb.place(relx=0.1,rely=0.45)
    sub_lb.place(relx=0.1,rely=0.5)
    
    id_field.place(relx=0.25,rely=0.15)
    name_field.place(relx=0.25,rely=0.2)
    dob_field.place(relx=0.25,rely=0.25)
    email_field.place(relx=0.25,rely=0.3)
    phone_field.place(relx=0.25,rely=0.35)
    course_field.place(relx=0.25,rely=0.4)
    year_field.place(relx=0.25,rely=0.45)

    root.mainloop()