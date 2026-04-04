from pygamelogic.cooldown import CooldownManager
class InventorySystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.cooldown_manager = CooldownManager()
    def add_item(self, item):
        if item.stackable:
            
            for existing_item in self.items:
                
                    
                if (existing_item.name.lower() == item.name.lower() and  existing_item.stackable):
                        
                    new_quantity = existing_item.quantity + item.quantity
                        
                    if new_quantity > existing_item.max_quantity:
                        raise ValueError(f"Cannot exceed max stack size ({existing_item.max_quantity})")

                    existing_item.quantity = new_quantity
                    return

        if len(self.items) == self.capacity:
            raise ValueError("The Inventory items capacity is full.")
            
        self.items.append(item)
            
    def remove_item(self, item, quantity=1):
        for current_item in self.items:
            
            if current_item.name.lower() == item.name.lower():

                # If stackable → reduce quantity
                if current_item.stackable:
                    if current_item.quantity > quantity:
                        current_item.quantity -= quantity
                        return
                    elif current_item.quantity == quantity:
                        self.items.remove(current_item)
                        return
                    else:
                        raise ValueError("Not enough items to remove")

                # If NOT stackable → remove directly
                else:
                    self.items.remove(current_item)
                    return

        raise ValueError("Item not found in the list.")
            
        
    def get_items(self):
        return self.items

    def get_total_value(self):
        total = 0
        for item in self.items:
            total += item.get_value_with_rarity()

        return total
    
    def get_items_sorted_by_value(self):
        
        sorted_items = sorted(self.items, key=lambda item: item.get_value_with_rarity(), reverse=True)
        return sorted_items
    
    def get_items_by_rarity(self, rarity):
        rarity_list = []

        for item in self.items:
            if item.rarity.lower() == rarity.lower():
                rarity_list.append(item)
                
        if rarity_list == []:
            raise ValueError(f"{rarity} rarity was not found in inventory")

        return rarity_list
            
    def find_items_by_name(self, name):
        results = []
        for item in self.items:
            if item.name.lower() == name.lower():
                results.append(item)

        if results == []:
            raise ValueError(f"Name '{name}' was not found in inventory")
        else:
            return results

    def use_item(self, item, target):
        for current_item in self.items:
            if current_item.name.lower() == item.name.lower():
                
                if self.cooldown_manager.is_on_cooldown(current_item.name):
                    remaining = self.cooldown_manager.get_remaining_time(current_item.name)
                    raise ValueError(f"{current_item.name} is on cooldown for {remaining}s")

                current_item.use(target)
                # Setting cooldown timer.
                if current_item.cooldown > 0:
                    self.cooldown_manager.set_cooldown(current_item.name, current_item.cooldown)
                
                # If stackable → reduce quantity
                if current_item.stackable:
                    current_item.quantity -= 1
                    if current_item.quantity == 0:
                        self.items.remove(current_item)
                else:
                    self.items.remove(current_item)

                return

        raise ValueError("Item not found in inventory.")
        
