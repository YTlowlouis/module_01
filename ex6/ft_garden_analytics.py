class Plant:
    """Base of the family tree."""

    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Standard growth action."""
        self.height += 1


class FloweringPlant(Plant):
    """Middle of the family tree."""

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = True


class PrizeFlower(FloweringPlant):
    """Top of the family tree."""

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.prize_points: int = points


class Garden:
    """Represents an individual garden collection."""

    def __init__(self, owner_name: str):
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden."""
        self.plants.append(plant)

    def nbr_plants(self) -> int:
        """Returns total number of plants using len()."""
        return len(self.plants)


class GardenManager:
    """Manages multiple gardens and provides analytics."""
    
    total_gardens_managed: int = 0

    def __init__(self):
        self._gardens: list[Garden] = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens_managed += 1

    def add_garden(self, garden: Garden) -> None:
        """Links a garden to the manager."""
        self._gardens.append(garden)

    @classmethod
    def get_global_report(cls) -> None:
        """Class method to show manager-level data."""
        print(f"Total gardens managed: {cls.total_gardens_managed}")

    @staticmethod
    def validate_height(height: int) -> bool:
        """Static utility: no self or cls needed."""
        return height > 0

    class GardenStats:
        """Nested helper class for data processing."""

        def calculate_score(self, garden: Garden) -> int:
            """Calculates a custom score for a garden."""
            score = 0
            for p in garden.plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.prize_points
            return score

        def count_types(self, garden: Garden) -> dict[str, int]:
            """Categorizes plants by their specific types."""
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for p in garden.plants:
                if isinstance(p, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(p, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    alice_garden = Garden("Alice")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    manager.add_garden(alice_garden)

    print(f"Added {len(alice_garden.plants)} plants to Alice's garden")
    for p in alice_garden.plants:
        p.grow()
        print(f"{p.name} grew 1cm")

    print(f"\n=== {alice_garden.owner_name}'s Garden Report ===")
    types = manager.stats.count_types(alice_garden)
    print(f"Plant types: {types['regular']} regular, "
          f"{types['flowering']} flowering, {types['prize']} prize")

    score = manager.stats.calculate_score(alice_garden)
    print(f"Garden score: {score}")

    is_valid = GardenManager.validate_height(oak.height)
    print(f"Height validation test: {is_valid}")

    GardenManager.get_global_report()
