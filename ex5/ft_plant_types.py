class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"""Invalid operation attempted: age {new_age}
days [REJECTED]""")
            print("Security: Negative age rejected")
            return
        self._age = new_age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"""Invalid operation attempted: height
{new_height}cm [REJECTED]""")
            print("Security: Negative height rejected")
            return
        self._height = new_height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def grow_action(self) -> int:
        self.set_height(self.get_height() + 1)
        return 1

    def age_action(self) -> int:
        self.set_age(self.get_age() + 1)
        return 1

    def get_info(self) -> None:
        print(f"{self.name}: {self._height}cm; {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    # On crée 2 instances de chaque type comme demandé
    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 30, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 1200, 3650, 80)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "beta-carotene")

    # Affichage conforme à l'exemple de l'exercice
    # Flower
    print(f"{rose.name} (Flower), {rose.color} color")
    rose.bloom()

    # Tree
    print(f"{oak.name} (Tree), {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    # Vegetable
    print(f"{tomato.name} (Vegetable), {tomato.harvest_season} harvest")
