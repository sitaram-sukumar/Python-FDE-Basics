from abc import ABC, abstractmethod

class RazorPay:
    def ClassicPay(self):
        print("Payment via Razor ")
        
class Zelle:
    def Pay(self):
        print("Payment via Zelle")
        
class UPI:
    def Pay(self):
        print("Payment via UPI")
        
class Purchase:
    def __init__(self, paymentGateway):
        self._paymentGateway = paymentGateway

    def checkout(self):
        print("Checking out ...")
        self._paymentGateway.Pay();
     
oGateway = [RazorPay(), Zelle(), UPI() ]

# Will not work for RazorPay as it does not have a Pay method (It has ClassicPay 
# method instead). This issue is fixed in Abstraction_3.py by using an 
# abstract class to define a common interface for all payment gateways.
oPayment = Purchase(oGateway[2])
oPayment.checkout()