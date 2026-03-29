class Plant:
    # --- Classe Imbriquée pour les Statistiques (Exigence Exo 6) ---
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        # On utilise tes méthodes de validation dès l'init
        self.set_height(height)
        self.set_age(age)
        self._stats = self._Stats()

    # --- Méthodes Statiques et de Classe (Exigence Exo 6) ---
    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    # --- Tes méthodes de Sécurité (Exo 4) ---
    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Error, age can't be negative\nAge update rejected")
            return
        self._age = new_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"Error, height can't be negative\nHeight update rejected")
            return
        self._height = new_height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    # --- Tes actions mises à jour avec les Stats ---
    def grow_action(self) -> None:
        self.set_height(self.get_height() + 8.0)
        self._stats.grow_calls += 1

    def age_action(self, days: int = 1) -> None:
        self.set_age(self.get_age() + days)
        self._stats.age_calls += 1

    def get_info(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        super().get_info()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower): # Héritage en chaîne (Exigence Exo 6)
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42 # Apparaît après le bloom

    def get_info(self) -> None:
        super().get_info()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0 # Stat spécifique demandée pour les arbres

    def produce_shade(self) -> None:
        self._shade_calls += 1
        shade_len = self._height
        print(f"Tree {self.name} now produces a shade of "
              f"{shade_len}cm long and {self.trunk_diameter}cm wide.")

    def get_info(self) -> None:
        super().get_info()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


# --- Fonction Unique de Statistiques (Exigence Exo 6) ---
def display_any_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


# --- Zone de Test ---
if __name__ == "__main__":
    print("=== Garden statistics ===")
    
    # Test Statique
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    # Test Flower
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.get_info()
    display_any_plant_stats(rose)
    rose.grow_action()
    rose.bloom()
    rose.get_info()
    display_any_plant_stats(rose)

    # Test Tree
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.get_info()
    display_any_plant_stats(oak)
    oak.produce_shade()
    display_any_plant_stats(oak)

    # Test Seed
    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.get_info()
    sun.grow_action()
    sun.age_action(20)
    sun.bloom()
    sun.get_info()
    display_any_plant_stats(sun)

    # Test Anonymous
    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.get_info()
    display_any_plant_stats(anon)
