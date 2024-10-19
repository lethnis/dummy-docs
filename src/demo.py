class Dummy:
    """Dummy for training. You can beat it, or shoot it with arrows."""

    def __init__(self, height=180, material="straw"):
        """Creation of the dummy. For now it has no health.

        Args:
            height (int, optional): height of the dummy. Defaults to 180.
            material (str, optional): what is it made of. Wood, metal, etc. Defaults to "straw".
        """
        self.height = height
        self.material = material

    def do_nothing(self) -> None:
        """Well, what else can it does?"""
        pass


def make_dummies(self, amount: int, materials: str | list[str] | None = None) -> list[Dummy]:
    """Creates dummies for training.

    Args:
        amount (int): how much dummies do you want.
        materials (str | list[str] | None): what dummies are made of.
            One value to use for all dummies. If you use list it should be of
            length amount. Defaults to None - will use default dummy material.

    Returns:
        list[Dummy]: list of dummies of size amount with provided materials.
    """

    dummies = []

    for i in range(amount):
        if not materials:
            dummies.append(Dummy())
        elif isinstance(materials, str):
            dummies.append(Dummy(material=materials))
        elif isinstance(materials, list):
            dummies.append(Dummy(material=materials[i]))

    return dummies


def clean_the_floor():
    pass
