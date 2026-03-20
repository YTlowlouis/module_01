class Plant:
    def __init__(self, name: str):
        self.name = name
        self._height = 0
        self._age = 0

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"""Invalid operation attempted: age {new_age}
days [REJECTED]""")
            print("Security: Negative age rejected")
            return
        self._age = new_age
        print(f"Age updated: {new_age} days [OK]")

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"""Invalid operation attempted: height
{new_height}cm [REJECTED]""")
            print("Security: Negative height rejected")
            return
        self._height = new_height
        print(f"Height updated: {new_height}cm [OK]")

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


if __name__ == "__main__":
    rose = Plant("rose")
    rose.set_height(5)
    rose.set_age(-5)
    rose.set_age(6)
