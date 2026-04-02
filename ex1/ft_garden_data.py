class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("rosy", 15, 5)
    orange = Plant("orange", 2, 10)
    poppy = Plant("opium", 23, 4)
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{orange.name}: {orange.height}cm, {orange.age} days old")
    print(f"{poppy.name}: {poppy.height}cm, {poppy.age} days old")
