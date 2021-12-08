import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x120')
window.title("คำนวณค่าค่าไฟฟ้า")
lbl1 = tk.Label(window,text="ป้อนหน่วยค่าไฟ",font=(12))
lbl1.pack(pady=5)
txt1 = tk.Entry(window,width=15)
txt1.pack(pady=5)

def electro():
    unit = txt1.get()
    if unit == '':
        messagebox.showerror('Error', 'กรุณาใส่หน่วยค่าไฟ!')
    else:
        unit = int(txt1.get())
        if unit>=501:
            y = 50*2
            y2 = 50*3
            y3 = 400*5
            z = unit-500
            z2 = z*7
            Result = y+y2+y3+z2
            messagebox.showinfo("ผลลัพธ์","ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+(50x3)+(400x5)+({}x7) = {} บาท".format(unit,z,Result))
        elif unit>=101:
            y = 50*2
            y2 = 50*3
            z = unit-100
            z2 = z*5
            Result = y+y2+z2
            messagebox.showinfo("ผลลัพธ์","ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+(50x3)+({}x5) = {} บาท".format(unit,z,Result))
        elif unit>=51:
            y = 50*2
            z = unit-50
            z2 = z*3
            Result = y+z2
            messagebox.showinfo("ผลลัพธ์","ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+({}x3) = {} บาท".format(unit,z,Result))
        else:
            Result = unit*2
            messagebox.showinfo("ผลลัพธ์","ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = ({}x2) = {} บาท".format(unit,unit,Result))

btn = tk.Button(window,text="Result",width=12,command=electro)
btn.pack(pady=5)

window.mainloop()