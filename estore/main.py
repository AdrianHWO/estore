from item import Item
from phone import Phone

item1 = Item("MyItem", 500, 50)
item1.apply_discount()

item2 = Phone("Samsung", 1200.99, 21, 2)
item2.apply_increment(0.15)

print(item1.name)
print(item1.price)
print(item2)
print(item2.price)
print(f"Broken Phones is {item2.broken_phones}")
