import difflib as dl

file = "student.txt"
with open(file, "a", encoding="UTF-8") as f:
    myInput = input("Enter String 'ID:Name:Grade' ('\\' to exit) : ")
    while myInput != "\\":
        print(f"write {myInput} to file")
        f.write(f"{myInput}\n")
        myInput = input("Enter String 'ID:Name:Grade' ('\exit' to exit) : ")

d = {}
with open(file,encoding="UTF-8") as f:
    for line in f:
        (ID, Name,Grade) = line.split(':')
        d[ID] = Name,Grade
        
n = input("Enter String to search ('\\' to exit): ")
while n.strip() != "\\":
    select = dl.get_close_matches(n,d,cutoff=1)
    if len(select) > 0:
        for i in select:
            ID = n
            Name,Grade = d[ID]
            print(f"รหัสนักศึกษา : {ID}\n")
            print(f"ชื่อ-สกุล : {Name}\n")
            print(f"เกรดเฉลี่ย : {Grade}")
            print("-----------------------------------------------------------\n")
    else:
        print("No word matched")
    n = input("Enter ID to search ('\\' to exit): ")
