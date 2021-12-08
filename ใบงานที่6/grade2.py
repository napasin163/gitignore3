from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('โปรแกรม คำนวนเกรด')
root.geometry('200x100')
root.resizable(0,0)

def process():
    if get_data.get() == '':
        messagebox.showerror('ล้มเหลว', 'กรุณาใส่คะแนนของคุณ!')
    else:
        score = float(get_data.get())
        if score < 60:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด F')
        elif score < 65:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด D')
        elif score < 70:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด D+')
        elif score < 75:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด C')
        elif score < 80:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด C+')
        elif score < 85:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด B')
        elif score < 90:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด B+')
        elif score <= 100:
            messagebox.showinfo('ผลลัพธ์', 'คุณได้เกรด A')
        else:
            messagebox.showerror('ล้มเหลว', 'คุณกรอกคะแนนไม่ถูกต้อง')

Label(root, text='กรอกคะแนนของคุณ', font='BOLD').pack()
get_data = StringVar()
Entry(root, textvariable=get_data).pack(pady=10)
Button(root, text='คำนวน', font='BOLD', command=process).pack()

root.mainloop()