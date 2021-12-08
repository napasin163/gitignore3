txt = input("Input String: ")
lower_check = []
for i in txt:
    if i.islower():
        lower_check.append(i)
print(f'ตัวอักษรพิมพ์เล็ก เท่ากับ {len(lower_check)} ตัว')
