class DataBase:

    def __init__(self, first_name, last_name, patronymic_name,phone):
        print("User: %s %s %s %s" % (first_name,patronymic_name,last_name,phone))
        print('DataBase: %s Работает в компании "Рога и Копыта":' % (self.__class__.__name__))
		
class Employee(DataBase):

    def __init__(self, first_name, last_name, patronymic_name,phone):
        DataBase.__init__(self, first_name, last_name, patronymic_name, phone)
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic_name = patronymic_name
        self.phone = phone
        

		

