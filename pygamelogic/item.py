class Item:
    def __init__(self, name, rarity, value, stackable=False, quantity=1, max_quantity=99, cooldown=0):
        self.name = name
        self.rarity = rarity
        self.value = value
        self.stackable = stackable
        self.quantity = quantity
        self.max_quantity = max_quantity
        self.cooldown = cooldown

    def __str__(self):
        if self.stackable == True:
            return f"{self.name} x{self.quantity} ({self.rarity}) - {self.value}"
        else:
            return f"{self.name} ({self.rarity}) - {self.value}"

    def get_value_with_rarity(self):
        if self.rarity.lower() == "common":
            return self.value * 1
        elif self.rarity.lower() == "rare":
            return self.value * 2
            
        elif self.rarity.lower() == "epic":
            return self.value * 3
        elif self.rarity.lower() == "legendary":
            return self.value * 4
        elif self.rarity.lower() == "mythical":
            return self.value * 5
        else:
            raise ValueError(f"Invalid rarity: {self.rarity}")
    def use(self, target):
        raise NotImplementedError("This item cannot be used.")
    
class Potion(Item):
    def __init__(self, name, rarity, value, heal_amount, quantity=1, cooldown=0):
        super().__init__(name, rarity, value, stackable=True, quantity=quantity, cooldown=cooldown)
        self.heal_amount = heal_amount
    def use(self, target):
        target.heal_health(self.heal_amount)
        print(f"{self.name} used! Healed {self.heal_amount} HP.")

class Weapon(Item):
    def __init__(self, name, rarity, value, damage, cooldown=0):
        super().__init__(name, rarity, value, stackable=False, cooldown=cooldown)
        self.damage = damage
    def use(self, target):
        target.take_damage(self.damage)
        print(f"{self.name} used! Dealt {self.damage} damage.")

class Armor(Item):
    def __init__(self, name, rarity, value, defense, cooldown=0):
        super().__init__(name, rarity, value, stackable=False, cooldown=cooldown)
        self.defense = defense
    def use(self, target):
        print(f"{self.name} equipped! Defense +{self.defense}")
        
