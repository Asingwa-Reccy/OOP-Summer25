class Ingredient:
    def __init__(self, name, quantity, unit, threshold):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.threshold = threshold

    def is_low_stock(self):
        return self.quantity <= self.threshold
