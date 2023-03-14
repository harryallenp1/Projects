# Harry Allen
# ID ;991680235
class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def calculateCost(self):
        cost = self.price * self.quantity
        tax = 0.13 * cost
        total_cost = cost + tax
        return total_cost
        
    def __str__(self):
        cost = self.calculateCost()
        return f"{self.name} ({self.quantity} @ ${self.price:.2f}) = ${cost:.2f}"

p1 = Product("Apple", 0.75, 3)
print("----------------------------------------------------")
print("Buying 3 Apples at the price of 0.75 in Ontario would cost you ",p1)
print("----------------------------------------------------")
print("----------------------------------------------------")

p2 = Product("Orange", 1.25)
print("Buying 1 Orange at the price of 1.25 in Ontario would cost you ",p2)
print("----------------------------------------------------")
print("----------------------------------------------------")

p3 = Product("Banana", 0.50, 5)
print("Buying 5 Bananas at the price of 0.50 in Ontario would cost you ",p3)
print("----------------------------------------------------")