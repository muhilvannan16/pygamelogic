class HealthSystem:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount, critical=False):
        if amount < 0:
            raise ValueError("Damage cannot be negative")

        if critical:
            amount *= 2

        self.current_health -= amount

        if self.current_health < 0:
            self.current_health = 0

    def heal_health(self, amount):
        if amount < 0:
            raise ValueError("Heal cannot be negative")
        
        self.current_health += amount

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_alive(self):
         return self.current_health > 0
           
