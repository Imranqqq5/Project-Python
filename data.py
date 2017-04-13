from employee import Employee
from kanditat import Kanditat,Soiskatel
import datetime
#Часть 1

print('|'*55)        
print('***ДЕЙСТВУЮЩИЕ СОТРУДНИКИ КОМПАНИИ: "РОГА И КОПЫТА"***')
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("***************Сотрудник № 1******************")    
t1= Employee ("Виктор","Петрович", "Иванов", "8903-555-55-55")
year1 = datetime.date.today()
year2 = datetime.date(1990, 2, 2)
result = (year1 - year2).days//365
print("Возраст: %s лет" % (result))

job1 = datetime.date.today()
job2 = datetime.date(2010, 2, 2)
result = (job1 - job2).days//365

print("Работает в компании: %s лет" % (result)) 

print("***************Сотрудник № 2******************")
t2= Employee ("Иван","Хреновкич", "Петров", "8903-222-23-23")
year1 = datetime.date.today()
year2 = datetime.date(1933, 2, 2)
result = (year1 - year2).days//365
print("Возраст: %s лет" % (result))

job1 = datetime.date.today()
job2 = datetime.date(1955, 2, 2)
result = (job1 - job2).days//365

print("Работает в компании: %s лет" % (result))

print("***************Сотрудник № 3******************")

t3= Employee ("Ирина","Тупая", "Викторовна", "8903-565-66-26")
year1 = datetime.date.today()
year2 = datetime.date(1999, 2, 2)
result = (year1 - year2).days//365
print("Возраст: %s лет" % (result))

job1 = datetime.date.today()
job2 = datetime.date(2005, 2, 2)
result = (job1 - job2).days//365

print("Работает в компании: %s лет" % (result))




# ЧАСТЬ 2
print('|'*55)		
print('***ГРУППА КАНДИДАТОВ НА ДОЛЖНОСТЬ: ТРУБОЧИСТОВ***')
print("|||||||||||||||||||||||||||||||||||||||||||||||||")		
print("***************Кандидат № 1******************")
d1= Soiskatel ("Александр","Тупица", "Иванович", "8903-123-16-16")
print("***************Кандидат № 2******************")   
d2= Soiskatel ("Валера","Говнюк", "Рихордович", "8902-121-11-12")
print("***************Кандидат № 3******************")
d3= Soiskatel ("Исаак","Ублюдок", "Абрамов", "8900-222-11-20")
print("***************Кандидат № 4******************")
d4= Soiskatel ("Ирина","Стерва", "Викторовна", "8922-122-12-22")
print("***************Кандидат № 5******************")
d5= Soiskatel ("Елена","Овца", "Ивановна", "8901-323-12-22")