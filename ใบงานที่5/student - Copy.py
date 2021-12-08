file = "student.txt" # กำหนดชื่อไฟล์
f = open(file, "a", encoding="UTF-8") # เปิดไฟล์ที่ชื่อ file = "student.txt" โดยใช้ UTF-8

myInput = input("Enter String 'ID:Name:Grade' ('\\' to exit) : ") # Input ข้อความ
while myInput != "\\": # เช็คว่า myInput != "\\" หรือไม่
    print(f"write {myInput} to file") # แสดงข้อความ write {myInput} to file เพื่อแจ้ง user ว่าเขียนข้อความลงบนไฟล์
    f.write(f"{myInput}\n") # คำสั่ง เขียนข้อความลงบนไฟล์
    myInput = input("Enter String 'ID:Name:Grade' ('\exit' to exit) : ") # Input อีกรอบว่า myInput != "\\" หรือไม่ ถ้าใช่ ไปลูปใหม่

d = {} # สร้างตัวแปร dict ไว้เก็บ ข้อมูลจากไฟล์
with open(file,encoding="UTF-8") as f: # คำสั่งเปิดไฟล์ โดยใช้ UTF-8 ** คำสั่ง as เป็นคำสั่งไว้เปลี่ยนตัวแปรที่ชื่อ file เป็น f เพื่อง่ายต่อการใช้งาน
    for line in f: # ลูป เพื่อนำข้อความไปเก็บในตัวแปร line
        (ID, Name,Grade) = line.split(':') # คำสั่งดึงข้อมูลจากตัวแปร line มาใส่ในตัวแปร ID Name และ Grade โดยแยกข้อความจาก คำสั่ง split(':') ** แยกข้อความโดยใช้ :
        d[ID] = Name,Grade # กำหนดให้ d[ID] เก็บข้อมูลจากตัวแปร Name และ Grade

n = input("Enter String to search ('\\' to exit): ") # Input ข้อความ

while n != "\\": # เช็คว่า n != "\\" หรือไม่
    ID = n
    Name,Grade = d[ID]
    print(f"รหัสนักศึกษา : {ID}\n")
    print(f"ชื่อ-สกุล : {Name}\n")
    print(f"เกรดเฉลี่ย : {Grade}\n")
    print("-----------------------------------------------------------\n")
    n = input("Enter ID to search ('\\' to exit): ") # Input อีกรอบว่า n != "\\" หรือไม่ ถ้าใช่ ไปลูปใหม่
