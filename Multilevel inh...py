class Dad():
    basketball = 2

class Son(Dad):
    dance = 1
    guitar = 1
    basketball = 4
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
class Grandson(Son):
    hockey = 4
    dance = 6
    def isdance(self):
        return f"Yes i dance very awesomely {self.dance} no of times"
darry = Dad()
larry = Son()
harry = Grandson()
print(larry.isdance())