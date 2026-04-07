from pygamelogic import InventorySystem, Potion, HealthSystem

def test_add_item():
    inventory = InventorySystem(5)
    potion = Potion("Potion", "common", 5, heal_amount=20)

    inventory.add_item(potion)

    assert len(inventory.get_items()) == 1


def test_use_potion():
    player = HealthSystem(100)
    inventory = InventorySystem(5)

    potion = Potion("Potion", "common", 5, heal_amount=20)
    inventory.add_item(potion)

    player.take_damage(30)  # now 70
    inventory.use_item(potion, player)

    assert player.current_health == 90
