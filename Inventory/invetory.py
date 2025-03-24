from Product.IProduct import IProduct
from Product.product import Mobile


class Inventory:
    products = {}

    def getquantity(self, product: IProduct):
        return product.AvalaibleQuantity
