class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self) -> int:
        self.height += 1
        return 1

    def age(self) -> int:
        self.age_days += 1
        return 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    list_plant = []
    for data in plants_data:
        new_plant = Plant(data[0], data[1], data[2])
        list_plant.append(new_plant)
        print("Created:", new_plant.name, f"({new_plant.height}cm,",
              new_plant.age_days, "days)")

    print("Total plants created:", len(list_plant))
