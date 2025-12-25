class Hero:
    """Класс для представления героя."""
    
    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        """
        Инициализация героя.
        
        Args:
            name: Имя героя
            health: Здоровье героя (по умолчанию 100)
            attack_power: Сила атаки (по умолчанию 20)
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def strike(self, target: 'Hero') -> None:
        """
        Атакует другого героя.
        
        Args:
            target: Объект героя, который будет атакован
        """
        if self.health > 0:
            target.health -= self.attack_power
            if target.health < 0:
                target.health = 0

knight = Hero("Arthur", 100, 20)
rogue = Hero("Robin", 80, 15)
knight.strike(rogue) 
rogue.strike(knight) 
print(f"{knight.name}: {knight.health}") 
print(f"{rogue.name}: {rogue.health}")  