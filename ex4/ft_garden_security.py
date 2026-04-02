class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0

        print(f"Plant created: {self.name.capitalize()}: "
              f"{height}cm, {age} days old")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, "
                  "height can't be negative")
            print("Height update rejected")
            return
        self._height = value

    def get_height(self) -> float:
        return self._height

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = value

    def get_age(self) -> int:
        return self._age

    def grow(self) -> int:
        self._height += 1
        return 1

    def age(self) -> int:
        self._age += 1
        return 1

    def show(self) -> None:
        print(f"Current state: {self.name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-10.0)
    rose.set_age(-5)

    rose.show()


if __name__ == "__main__":
    main()
