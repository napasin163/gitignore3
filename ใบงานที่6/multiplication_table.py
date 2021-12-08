import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.title("multiplication table")
lbl1 = tk.Label(window,text="Input Number")
lbl1.pack(pady=5)
txt1 = tk.Entry(window,width=15)
txt1.pack(pady=5)

def btn_clicked():
    n1 = int(txt1.get())
    answer = ""
    for l in range(1,13):
        Result = n1*l
        print("{}*{}={}".format(n1,l,Result))
        answer += str(f"{n1} * {l} = {Result}") + "\n"
        lblResult.configure(text= answer)

btn = tk.Button(window,text="Result",width=12,command=btn_clicked)
btn.pack(pady=5)

lblResult = tk.Label(window)
lblResult.pack(pady=10)

window.mainloop()