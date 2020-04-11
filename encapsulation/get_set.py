"""
Using getter and setter methods to access private variables
To access and change private variables accessor (getter) methods and
mutator (setter methods) should be used which are part of the class.

"""
class Account:

    def __init__(self):
        self.cust_name = 'Abhishek'  # public
        self.__account_no = '101'  # private

    def show_details(self):
        print(f'customer name : {self.cust_name}')
        print(f'account num : {self.__account_no}')

    def get_acc(self):
        print(self.__account_no)

    def set_acc(self, account_num):
        self.__account_no = account_num


obj = Account()

obj.show_details()  # can access using class method

obj.set_acc(202)
obj.get_acc()  # accessing private variable account_num using get method

