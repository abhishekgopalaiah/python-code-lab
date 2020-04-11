"""
As you can see variables can still be accessed using
the method which is part of the class but age (which is a private variable)
can’t be accessed directly from outside now.

variables can be accessed using the method of the class, but account_no which is private attribute cannot be assessed directly from outside the class

"""
class Account:

    def __init__(self):
        self.cust_name = 'Abhishek'  # public
        self.__account_no = '101'  # private

    def show_details(self):
        print(f'customer name : {self.cust_name}')
        print(f'account num : {self.__account_no}')


obj = Account()
obj.show_details()  # can access using class method

# accessing public attribute
print(obj.cust_name)

# accessing private attribute - > gives error
print(obj.__account_no)

# name mangling (object._ClassName__variable)
# print(obj._Account__account_no)