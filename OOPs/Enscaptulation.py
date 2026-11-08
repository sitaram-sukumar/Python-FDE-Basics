class Vehicle:
    def __init__(self, VName, VTemp, VACVolt):
        self.Name = VName
        self._Temp = VTemp
        self.__acVolt = VACVolt
        
    def getVoltage(self):
        return self.__acVolt
        
class Toyota(Vehicle):
    def __init__(self, VName, VTemp, VACVolt):
        super().__init__(VName, VTemp, VACVolt)
        
    def getTemp(self):
        return self._Temp
    
    def get_acVolt(self):
        return super().getVoltage()
    
ToyotaCar = Toyota("Toyota Camry", 90, 220)
print("Car Name:", ToyotaCar.Name)
print("Car Temperature:", ToyotaCar.getTemp())
print("Car AC Voltage:", ToyotaCar.get_acVolt())

print("Car Temperature (Direct Access):", ToyotaCar._Temp)  # Accessing protected member
#print("Car AC Voltage (Direct Access):", ToyotaCar.__acVolt)  # Attempting to access private member (will raise an AttributeError)