class Product:

def __init__(self, name, price = 10, weight = 20, flammability = 0.5, indentifier):
  self.name = name
  self.price = price
  self.weight = weight
  self.flammability = flammability
  self.indentifier = random.randint(1000000,10000000)
