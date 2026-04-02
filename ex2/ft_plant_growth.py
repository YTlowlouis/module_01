class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}:"
              f"{round(self.height, 1)}cm, {self.age_days} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("rose", 25.0, 30)

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        if day < 7:
            rose.grow()
            rose.age()

    total_growth = rose.height - initial_height
    print(f"\nGrowth this week: {round(total_growth)}cm")


if __name__ == "__main__":
    main()
