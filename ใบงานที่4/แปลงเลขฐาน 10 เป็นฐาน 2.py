decimal_input = int(input("ป้อนตัวเลขฐานสิบ : "))
binary = []
decimal = decimal_input
 
while decimal > 0:
    binary.append(str(decimal % 2))
    decimal = int(decimal / 2)
 
binary.reverse()
 
print(f"{decimal_input} ฐานสิบ แปลงเป็นเลขฐานสองเท่ากับ {''.join(binary)}")
