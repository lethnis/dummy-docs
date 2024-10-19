class Man:

    def __init__(
        self,
        health: int = 100,
        armor: int = 0,
        inventory: list | None = None,
    ) -> None:
        """Basic character for every one else.

        Args:
            health (int, optional): Amount of health. Defaults to 100.
            armor (int, optional): Armour strength. Defaults to 0.
            inventory (list | None, optional): What does man has. Defaults to None.
        """

        self.health = health
        self.armor = armor
        self.inventory = inventory

    def train(self) -> None:
        """Train to become stronger."""
        pass

    def sleep(self) -> None:
        """Sleep to rest."""
        pass


class Warrior(Man):
    """Man after year of training.

    Args:
        health (int, optional): Max amount of health. Defaults to 150.
        armor (int, optional): Max armor strength. Defaults to 50.
        inventory (list | None, optional): If None, will have sword and shield. Defaults to None.
    """

    def __init__(self, health: int = 150, armor: int = 50, inventory: list | None = None) -> None:
        super().__init__(health, armor, inventory)

        if not self.inventory:
            self.inventory = ["sword", "shield"]
