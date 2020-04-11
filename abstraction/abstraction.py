from abc import ABC, abstractmethod


class Bank(ABC):

    @abstractmethod
    def get_rate_of_interest(self):
        pass


class SBI(Bank):

    def get_rate_of_interest(self):
        print('interest rate in sbi is 11%')


class HDFC(Bank):
    def get_rate_of_interest(self):
        print('interest rate in hdfc is 14%')


# b = Bank() # Can't instantiate abstract class
obj_sbi = SBI()
obj_sbi.get_rate_of_interest()

obj_hdfc = HDFC()
obj_hdfc.get_rate_of_interest()
