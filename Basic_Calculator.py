# This program is to build a basic calculator
# Calculator will be built on a GUI

class Calculator:

    def __init__(self):
        self.a = float(input('Enter first number:'))
        self.b = float(input('Enter second number:'))
        self.op = input('Enter operation(add/sub/mul/div):')
        self.result()

    def result(self):  
        if self.op == 'add':
            print('The sum is: ', self.a+self.b)
        elif self.op == 'sub':
            print('The subtraction is: ', self.a-self.b)
        elif self.op == 'mul':
            print('The multiplication is: ', self.a*self.b)
        elif self.op == 'div':
            print('The division is: ', self.a/self.b)
        else:
            print('Invalid Syntax')

Calculator()