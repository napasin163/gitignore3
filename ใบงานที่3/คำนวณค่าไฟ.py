def electro():
    x = input("ป้อนหน่วยค่าไฟ : ")
    x = int(x)
    if x>=501:
        y = 50*2
        y2 = 50*3
        y3 = 400*5
        z = x-500
        z2 = z*7
        Result = y+y2+y3+z2
        print("ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+(50x3)+(400x5)+({}x7) = {}".format(x,z,Result))
    elif x>=101:
        y = 50*2
        y2 = 50*3
        z = x-100
        z2 = z*5
        Result = y+y2+z2
        print("ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+(50x3)+({}x5) = {}".format(x,z,Result))
    elif x>=51:
        y = 50*2
        z = x-50
        z2 = z*3
        Result = y+z2
        print("ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = (50x2)+({}x3) = {}".format(x,z,Result))
    else:
        Result = x*2
        print("ใช้ไฟฟ้าไป {} หน่วย จะเป็นเงิน = ({}x2) = {}".format(x,x,Result))
electro()
            
