class Product:
    # properties/attributes represented using variable

    # __init__() inbuilt function to initialize variables
    # constructor or initializer
    # called automatically when object is created for this class
    def __init__(self):
        self.id = 0 #int
        self.pName = "Unknown" #string
        self.price = 0.0 #float

    def __init__(self, pid: int, pname : str, pprice : float):
        self.id = pid
        self.pName = pname
        self.price = pprice

    # behavior represented using functions/methods
    # def displayProductInfo(self):
    #     print(f'Product ID : {self.id} Product Name : {self.pName} Product Price : {self.price}')

    #inbuilt method to describe object content
    #returns string
    def __str__(self) -> str:
        return f'{self.id} -- {self.pName} -- {self.price}'
