with open("data.txt", "w", encoding="utf-8") as f: # คำสั่งเปิดไฟล์ โดยใช้ UTF-8 ** คำสั่ง as เป็นคำสั่งไว้เปลี่ยนตัวแปรที่ชื่อ file เป็น f เพื่อง่ายต่อการใช้งาน
    myInput = input("Enter Line ('\\' to exit) : ") # Input ข้อความ
    while myInput != "\\": # เช็คว่า myInput != "\\" หรือไม่
        print(f"write {myInput} to file") # แสดงข้อความ write {myInput} to file เพื่อแจ้ง user ว่าเขียนข้อความลงบนไฟล์
        f.write(f"{myInput}\n") # คำสั่ง เขียนข้อความลงบนไฟล์
        myInput = input("Enter Line ('\exit' to exit) : ") # Input อีกรอบว่า myInput != "\\" หรือไม่ ถ้าใช่ ไปลูปใหม่

d = {} # สร้างตัวแปร dict ไว้เก็บ ข้อมูลจากไฟล์
with open("data.txt", "r", encoding="utf-8") as f: # คำสั่งเปิดไฟล์ โดยใช้ UTF-8 ** คำสั่ง as เป็นคำสั่งไว้เปลี่ยนตัวแปรที่ชื่อ file เป็น f เพื่อง่ายต่อการใช้งาน
    for line in f: # ลูป เพื่อนำข้อความไปเก็บในตัวแปร line
        (key, val) = line.split(':') # คำสั่งดึงข้อมูลจากตัวแปร line มาใส่ในตัวแปร key และ val โดยแยกข้อความจาก คำสั่ง split(':') ** แยกข้อความโดยใช้ :
        d[key] = val # กำหนดให้ d[key] เก็บข้อมูลจากตัวแปร val

n = input("Enter word to search ('\\' to exit): ") # Input ข้อความ
while n != "\\": # เช็คว่า n != "\\" หรือไม่
    print(f"{n} = {d[n]}") # แสดงข้อมูล n = d[n]
    n = input("Enter word to search ('\\' to exit): ") # Input อีกรอบว่า n != "\\" หรือไม่ ถ้าใช่ ไปลูปใหม่

f.close() # ปิดไฟล์