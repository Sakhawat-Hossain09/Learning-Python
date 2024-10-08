import time
class SmartPhone:
    def __init__(self, name:str, brand: str, price: float, is_turned_on: bool = False) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.is_turned_on: bool = is_turned_on

        
        
    def __str__ (self) -> str:
        return f"{self.name} is from {self.brand}. It's price at ${self.price}."
        
        
    def __repr__ (self) -> str:
        return f'SmartPhone(name="{self.name}", brand="{self.brand}", price={self.price}, is_turned_on={self.is_turned_on}'
        
        
    def turn_on(self) -> None:
        if self.is_turned_on == False:
            print(f"Turning on your {self.name}.")
            time.sleep(3)
            print(f"Your {self.name} is now turned on.")
            self.is_turned_on = True
        else:
            print(f"Your {self.name} is already turned on.")
            
            
    def turn_off(self) -> None:
        if self.is_turned_on == True:
            print(f"Turning off your {self.name}.")
            time.sleep(2)
            print(f"Your {self.name} is now turned off.")
            self.is_turned_on = False
        else:
            print(f"Your {self.name} is already turned off.")
            
            
    
        
iPhone: SmartPhone = SmartPhone(name="iPhone", brand="Apple", price=1199.00)

s24_ultra: SmartPhone = SmartPhone(name="S24 Ultra", brand="Samsung", price=1000.00)

print(iPhone)
print(repr(iPhone))
print(iPhone.brand)
print(iPhone.price)
print(iPhone.is_turned_on)
iPhone.turn_on()
iPhone.turn_off()


print()
print()


print(s24_ultra)
print(repr(s24_ultra))
print(s24_ultra.brand)
print(s24_ultra.price)
print(s24_ultra.is_turned_on)
s24_ultra.turn_on()
s24_ultra.turn_off()















