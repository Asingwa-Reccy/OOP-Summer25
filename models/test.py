from models.inventory import Inventory

inv = Inventory()
inv.add_ingredient("Flour", 10, "kg", 5)
inv.add_ingredient("Sugar", 3, "kg", 5)
inv.use_ingredient("Flour", 4)
inv.use_ingredient("Sugar", 2)

print("Current Inventory:")
print("\n".join(inv.list_inventory()))

print("\nLow Stock Items:")
print("\n".join(str(item) for item in inv.get_low_stock_items()))