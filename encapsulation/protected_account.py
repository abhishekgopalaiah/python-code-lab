class Account:

    def __init__(self):
        self.cust_name = 'Abhishek'  # public
        self._account_no = '101'  # private

    def show_details(self):
        print(f'customer name : {self.cust_name}')
        print(f'account num : {self._account_no}')


obj = Account()
obj.show_details()  # can access using class method

# accessing public attribute
print(obj.cust_name)

# accessing protected attribute
print(obj._account_no)