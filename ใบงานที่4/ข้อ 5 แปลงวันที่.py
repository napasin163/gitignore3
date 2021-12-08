from datetime import datetime
x = datetime.strptime(input('enter date (1-2-2564): '), '%d-%m-%Y')
print(x.strftime('%d-%B-%Y'))
