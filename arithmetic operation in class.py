class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def func(self):
       print("Addition :",self.a+self.b)
       print("Sub:",self.a-self.b)
       print("Mult:",self.a*self.b)
       print("Div:",self.a/self.b)
p1= calculator(4,3)
p1.func()