# 1st Question
# class with class & object specific attributes
class IceCream:
    # class attribute which is static
    scoop_limit = 3

    # Instance/object attributes start with self.
    def __init__(self, size: str, flavors: str, cup_or_cone: str):
        self.size = size
        self.flavors = flavors
        self.cup_or_cone = cup_or_cone
        IceCream.scoop_limit += 1

    @classmethod
    def ice(cls):
        IceCream.scoop_limit += 1


Ice1 = IceCream("Large", "Mint", "Cone")
print(Ice1)


# 2nd question
class SalesPerson:
    sales = 0

    def __init__(self, first_name: str, last_name: str, sales: int):
        self.first_name = first_name
        self.last_name = last_name
        self.sales = sales

    def makeSale(self):
        SalesPerson.sales += 1

    def salesReport(self):
        print(f"My total sales are {self.sales}!")


p1 = SalesPerson("Annie", "Mae", 250)
p2 = SalesPerson("Manda", "Lynn", 150)
p3 = SalesPerson("Dick", "Biscuits", 6969)


def sales(self):
    sales.SalesPerson = [6969, 250, 150]
    print(sales.SalesPerson.sort())
    print(sales.SalesPerson)
