from abc import ABC, abstractmethod

class PaymentGatewayStd(ABC):
    @abstractmethod
    def PayViaGateway(self):
        pass;

class RazorPay(PaymentGatewayStd):
    def ClassicPay(self):
        print("Payment via Razor ")
    def PayViaGateway(self):
            print("Payment via Razor ")
        
class Zelle(PaymentGatewayStd):
    def Pay(self):
        print("Payment via Zelle")
        
    def PayViaGateway(self):
        print("Payment via Zelle")
        
class UPI(PaymentGatewayStd):
    def Pay(self):
        print("Payment via UPI")
    
    def PayViaGateway(self):
        print("Payment via UPI")
         
class Purchase:
    def __init__(self, paymentGateway):
        self._paymentGateway = paymentGateway

    def checkout(self):
        print("Checking out ...")
        self._paymentGateway.PayViaGateway();
     
oGateway = [RazorPay(), Zelle(), UPI() ]

# Will not work for RazorPay as it does not have a Pay method (It has ClassicPay 
# method instead). This issue is fixed in Abstraction_3.py by using an 
# abstract class to define a common interface for all payment gateways.
oPayment = Purchase(oGateway[0])
oPayment.checkout()