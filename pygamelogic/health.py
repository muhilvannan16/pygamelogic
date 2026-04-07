class HealthSystem:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health

    def __str__(self):
        return f"{self.current_health)HP" # Affects how it looks when you print it out or turn it into a string

    def take_damage(self, amount, critical=False):
        """
        Subtract the amount to the health bar. If critical is true damage * 2
        """
        if amount < 0:
            raise ValueError("Damage cannot be negative")

        if critical:
            amount *= 2

        self.current_health -= amount

        if self.current_health < 0:
            self.current_health = 0

    def heal_health(self, amount):
        """
        Adds the amount to the health bar
        """
        if amount < 0:
            raise ValueError("Heal cannot be negative")
        
        self.current_health += amount

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_alive(self):
        """
        Checks if the player is alive
        """
         return self.current_health > 0

def shift_percentage(self, percentage: str):
    """
    Nudges the health by a percentage e.g 
    health = HealthSystem(200)
    health.shift_percentage("-50%")
    print(health) #100HP
    """
    clean_pct = percentage.replace("%", "").strip()
    pct_decimal = float(clean_pct) / 100.0
    span = self.max - self.min
    shift = int(pct_decimal * span)
    self.value += shift
