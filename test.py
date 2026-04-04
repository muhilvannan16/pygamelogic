from pygamelogic import HealthSystem
from pygamelogic import InventorySystem
from pygamelogic import Item
from pygamelogic import Potion
from pygamelogic import Weapon
from pygamelogic import Armor
from pygamelogic import CooldownManager
"""
This is the testing file for my library pygamelogic
Created by Muhilvannan
"""
# Testing the HealthSystem class.
p = HealthSystem(100) # Parameter for max_healh and current_health

print(p.max_health) # This is the max health.
# Has Parameters amount, critical = False.
p.take_damage(25)
print(p.current_health)

p.heal_health(10)
print(p.current_health)
# Now testing the InventorySystem class with the Item class.
item_1 = Item("Sword", "common", 10)
item_2 = Item("Armor", "rare", 20)
item_3 = Item("Shield", "epic", 30)
item_4 = Item("Binoculars", "legendary", 10)
item_5 = Item("Map", "Mythical", 20)
item_6 = Item("Cursed Sword", "Godly", 20)
inventory = InventorySystem(5)
inventory.add_item(item_1)
#inventory.add_item(item_1) # Trying to add a duplicate item in the list.
inventory.add_item(item_2)
inventory.add_item(item_3)
inventory.add_item(item_4)
inventory.remove_item(item_1)
for item in inventory.get_items():
    print(item)
# Testing the Item class paired with the InventorySystem class.
# inventory.remove_item(item_5)
inventory.remove_item(item_4)
for item in inventory.get_items():
    print(item)
print()
# Testing the rarity function of the Item class.
print("-----Testing the rarity system-----")
print(item_1.get_value_with_rarity())
print(item_2.get_value_with_rarity())
print(item_3.get_value_with_rarity())
print(item_4.get_value_with_rarity())
print(item_5.get_value_with_rarity())
#print(item_6.get_value_with_rarity())
print()
# Testing the total value function of Inventory class.
print("-----Testing the get_total_value function-----")
print(inventory.get_total_value())
# Testing the sorting by value function in inventory class.
print("-----Testing get_value_by_sorted_items function")
for item in inventory.get_items_sorted_by_value():
    print(item)
# Testing filtering function of the inventory class.
print("----Testing filter system----")

for item in inventory.get_items_by_rarity("rare"):
    print(item)
print()
# Testing the searching item by name function in inventory class.
print("-----Testing search system-----")

for item in inventory.find_items_by_name("Armor"):
    print(item)
# Testing the stacking in add_items function in Inventory class.
"""
print("---Testing stacking items----")
potion_1 = Item("Potion", "common", 5, True)
Sword = Item("Sword", "common", 10, False)
inventory.add_item(potion_1)
inventory.add_item(potion_1)
inventory.add_item(potion_1)
for item in inventory.get_items():
    print(item)
# Testing removeing stacked items.
print("----Testing remove with stacks----")

for item in inventory.get_items():
    print(item)

print("Removing 2 potions...")
inventory.remove_item(potion_1, 2)

for item in inventory.get_items():
    print(item)
"""
# Testing the subclasses Weapons, Potion and Armor in Inventory class.
print("----Testing potion subclass in Item class")
player = HealthSystem(100)
potion = Potion("Potion", "common", 5, heal_amount=20, quantity=3, cooldown=3)

inventory.add_item(potion)

print("Before using potion:", player.current_health)

# Testing Potion class further.
# Testing the CooldownManager class.
print("---Testing the cooldown system---")
player.take_damage(30)
print(player.current_health)  # should be 70

inventory.use_item(potion, player)
print(player.current_health)  # should be 90
remaining = inventory.cooldown_manager.get_remaining_time("Potion")
print(f"Remaining cooldown: {remaining}")
# inventory.use_item(potion, player)
print("After using potion:", player.current_health)
print(f"Is on cooldown: {inventory.cooldown_manager.is_on_cooldown("Potion")}")

print("----Manual cooldown test----")

inventory.cooldown_manager.set_cooldown("TestItem", 5)

print(inventory.cooldown_manager.is_on_cooldown("TestItem"))
print("Remaining:", inventory.cooldown_manager.get_remaining_time("TestItem"))
