from tkinter import *

root = Tk()
root.title('Test')
root.geometry('500x200')

def process():
    x = int(string_num.get())
    if x>=501:
        y = 50*2
        y2 = 50*3
        y3 = 400*5
        z = x-500
        z2 = z*7
        Result = y+y2+y3+z2
        output = "ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50 x 2) + (50 x 3) + (400 x 5) + ({} x 7) = {}".format(x,z,Result)
    elif x>=101:
        y = 50*2
        y2 = 50*3
        z = x-100
        z2 = z*5
        Result = y+y2+z2
        output = "ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50 x 2)+(50 x 3)+({} x 5) = {}".format(x,z,Result)
    elif x>=51:
        y = 50*2
        z = x-50
        z2 = z*3
        Result = y+z2
        output = "ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50 x 2) + ({} x 3) = {}".format(x,z,Result)
    else:
        Result = x*2
        output = "ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = ({} x 2) = {}".format(x,x,Result)

    my_label.configure(text=output)

string_num = StringVar()
Label(root, text='หน่วยไฟฟ้า').pack()
Entry(textvariable=string_num).pack()

Button(root, text='คำนวน', command=process).pack()
my_label = Label(root)
my_label.pack()

root.mainloop()