from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, balance: int):
        pass


class PayPal(PaymentProcessor):
    def pay(self, balance: int):
        print(f'оплачено {balance} при помощи PayPal')

class CreditCard(PaymentProcessor):
    def pay(self, balance: int):
        print(f'оплачено {balance} при помощи CreditCard')

class Crypto(PaymentProcessor):
    def pay(self, balance: int):
        print(f'оплачено {balance} при помощи Crypto')



class Payment:
    def __init__(self, paymentprocessor:PaymentProcessor):
        self.paymentprocessor = paymentprocessor

    def payment_process(self, balance: int):
        self.paymentprocessor.pay(balance)

    


pp = PayPal()
cc = CreditCard()
cr = Crypto()

pay1 = Payment(pp)
pay1.payment_process(1000)

pay2 = Payment(cc)
pay2.payment_process(5000)

pay3 = Payment(cr)
pay3.payment_process(50000)







