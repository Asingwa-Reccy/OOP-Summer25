from .ingredient import Ingredient

class Inventory:
    def __init__(self):
        self.items = {}

    def add_ingredient(self, name, quantity, unit, threshold):
        if name in self.items:
            self.items[name].add_stock(quantity)
        else:
            self.items[name] = Ingredient(name, quantity, unit, threshold)

    def use_ingredient(self, name, amount):
        if name in self.items:
            try:
                self.items[name].reduce_stock(amount)
            except ValueError as e:
                print(e)
        else:
            print(f"{name} not found in inventory.")

    def get_low_stock_items(self):
        return [item for item in self.items.values() if item.is_low_stock()]

    def list_inventory(self):
        return [str(item) for item in self.items.values()]
