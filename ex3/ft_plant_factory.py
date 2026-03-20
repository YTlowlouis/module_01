class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        self.height += 1
        return 1

    def age_older(self) -> int:
        self.age += 1
        return 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm; {self.age} days old")


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
              new_plant.age, "days)")

    print("Total plants created:", len(list_plant))
