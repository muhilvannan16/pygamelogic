import time

class CooldownManager:
    def __init__(self):
        self.cooldowns = {}

    def is_on_cooldown(self, item_name):
        if item_name in self.cooldowns:
            return time.time() < self.cooldowns[item_name]
        return False
    def set_cooldown(self, item_name, cooldown_time):
        self.cooldowns[item_name] = time.time() + cooldown_time

    def get_remaining_time(self, item_name):
        if item_name in self.cooldowns:
            remaining = self.cooldowns[item_name] - time.time()
            return max(0, round(remaining, 2))
        return 0
