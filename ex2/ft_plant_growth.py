class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> int:
        self.height += 1
        return 1

    def age_older(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm; {self.age} days old")


if __name__ == "__main__":
    rose = Plant("love", 12, 3)
    poppy = Plant("opium", 6, 4)
    blue_poppy = Plant("bread_seeds", 10, 5)
    growth = 0

    print("=== Day 1 ===")
    rose.get_info()
    poppy.get_info()
    blue_poppy.get_info()

    for _ in range(7):
        rose.age_older()
        growth += rose.grow()
        poppy.age_older()
        growth += poppy.grow()
        blue_poppy.age_older()
        growth += blue_poppy.grow()

    print("=== Day 7 ===")
    rose.get_info()
    poppy.get_info()
    blue_poppy.get_info()
    print(f"Growth this week: +{growth}cm")
