class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height)
        self.set_age(age)
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't "
                  "be negative\nAge update rejected")
            return
        self._age = value

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be "
                  "negative\nHeight update rejected")
            return
        self._height = value

    def grow(self) -> None:
        self.set_height(self._height + 1.0)
        self._stats.grow_calls += 1

    def age(self) -> None:
        self.set_age(self._age + 1)
        self._stats.age_calls += 1

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        status = "has not bloomed yet"
        if self._is_blooming:
            status = "is blooming beautifully"
        print(f"{self.name} {status}")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds_count}")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long "
              f"and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


def display_any_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._stats.display()
    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_any_plant_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_any_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_any_plant_stats(oak)
    oak.produce_shade()
    display_any_plant_stats(oak)

    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    sun.grow()
    sun.age()
    sun.bloom()
    sun.show()
    display_any_plant_stats(sun)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_any_plant_stats(anon)
