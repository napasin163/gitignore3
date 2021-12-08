import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x120')
window.title("คำนวณเกรด")
lbl1 = tk.Label(window,text="ป้อนคะแนนของคุณ",font=(12))
lbl1.pack(pady=5)
txt1 = tk.Entry(window,width=15)
txt1.pack(pady=5)

def grade():
    score = txt1.get()
    if score == '':
        messagebox.showerror('Error', 'กรุณาใส่คะแนนของคุณ!')
    else:
        score = float(txt1.get())
        if score>=80:
            messagebox.showinfo("ผลลัพธ์",f"คุณได้เกรด A คะแนนของคุณคือ {score}")
        elif score>=70:
            messagebox.showinfo("ผลลัพธ์",f"คุณได้เกรด B คะแนนของคุณคือ {score}")
        elif score>=60:
            messagebox.showinfo("ผลลัพธ์",f"คุณได้เกรด C คะแนนของคุณคือ {score}")
        elif score>=50:
            messagebox.showinfo("ผลลัพธ์",f"คุณได้เกรด D คะแนนของคุณคือ {score}")
        else:
            messagebox.showinfo("ผลลัพธ์",f"คุณได้เกรด F คะแนนของคุณคือ {score}")

btn = tk.Button(window,text="Result",width=12,command=grade)
btn.pack(pady=5)

window.mainloop()