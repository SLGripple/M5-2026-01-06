class Calculator:
    def __init__(self,num1,num2,surname = 'Lake'):
        self.num1 = num1
        self.num2 = num2
        self.name = 'Sam'
        self.surname = surname

    def get_sum(self):
        return self.num1 + self.num2
    
    def get_differrence(self):
        return self.num1 - self.num2
    
    def get_product(self):
        return self.num1 * self.num2
    
    def get_quotitent(self):
        return self.num1 / self.num2
    
if __name__ == '__main__':
    myCalc = Calculator(num1= 10, num2 = 20)
    print(myCalc.get_differrence())

    