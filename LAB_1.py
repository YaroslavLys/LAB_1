class Vase:

    number_of_obj = 0

    def __init__(self, volume=4, mass=1, material="porcelain", color="red", size="small", price=30):
        self.volume = volume
        self.mass = mass
        self.material = material
        self.color = color
        self.size = size
        self.price = price
        Vase.number_of_obj += 1

    @staticmethod
    def get_number_of_obj():
        return Vase.number_of_obj

    def __del__(self):
        print("Object is deleted")

    def __str__(self):
        return f"{self.volume} {self.mass} {self.material} {self.color} {self.size} {self.price}"


def main():
    vase1 = Vase(5)
    vase2 = Vase(3, 7)
    vase3 = Vase(2, 5, "clay")
    print("Number of objects:", Vase.get_number_of_obj())
    print(vase1.__str__())
    print(vase2.__str__())
    print(vase3.__str__())


if __name__ == "__main__":
    main()
