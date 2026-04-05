![Python](https://img.shields.io/badge/python-3.8+-blue)
![PyPI](https://img.shields.io/pypi/v/pygamelogic)
![License](https://img.shields.io/badge/license-MIT-green)
# pygamelogic

A lightweight Python game logic library featuring inventory systems, item mechanics, and cooldown management — designed for simplicity and extensibility.

---

## 🚀 Installation

```bash
pip install pygamelogic
```

---

## ✨ Features

* 📦 Inventory system with capacity limits
* 🧪 Stackable items (e.g., potions)
* ⚔️ Item subclasses (Potion, Weapon, Armor)
* ⏳ Cooldown system to prevent repeated usage
* ❤️ Health system (damage & healing mechanics)
* 🔍 Search, filter, and sorting utilities

---

## 🧪 Quick Example

```python
from pygamelogic import InventorySystem, Potion, HealthSystem

# Create player with 100 HP
player = HealthSystem(100)

# Create inventory
inventory = InventorySystem(5)

# Create potion
potion = Potion("Potion", "common", 5, heal_amount=20, quantity=2, cooldown=3)

# Add potion to inventory
inventory.add_item(potion)

print("Before:", player.current_health)

# Use potion
inventory.use_item(potion, player)

print("After:", player.current_health)
```

---

## 📊 Example Output

```
Before: 100
Potion used! Healed 20 HP.
After: 120
```

---

## ⚙️ Core Systems

### 📦 Inventory System

* Add and remove items
* Capacity management
* Stackable item support
* Sorting and filtering

### 🧩 Item System

* Base class: `Item`
* Subclasses:

  * `Potion` → heals target
  * `Weapon` → deals damage
  * `Armor` → increases defense
* Rarity-based value scaling

### ⏳ Cooldown System

* Prevents item spamming
* Tracks cooldown per item
* Provides remaining cooldown time

---

## 🧠 Cooldown Example

```python
inventory.use_item(potion, player)
inventory.use_item(potion, player)  # ❌ Raises cooldown error
```

---

## 📁 Project Structure

```
pygamelogic/
│
├── inventory.py
├── item.py
├── cooldown.py
├── health.py
```

---

## 🎯 Use Cases

* Beginner-friendly game development
* Prototyping RPG mechanics
* Learning object-oriented design
* Building inventory-based systems

---

## 👨‍💻 Author

Muhilvannan Elavazhagan

---

## 🌐 Links

* PyPI: https://pypi.org/project/pygamelogic/
* GitHub: https://github.com/muhilvannan16/pygamelogic

---

## 📜 License

This project is licensed under the MIT License.



Copyright (c) 2026 Muhilvannan

