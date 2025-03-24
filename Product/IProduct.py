from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod


class Category(Enum):
    Grain = 1
    Snack = 2
    Television = 3
    Electronic = 4


@dataclass
class ProductAttributes:
    Brand: str
    Title: str
    Description: str
    Price: float
    AvalaibleQuantity: int
    ProductCategory: Category


class IProduct(ABC, ProductAttributes):

    @abstractmethod
    def set_quantity(quantity: int):
        ProductAttributes.AvalaibleQuantity += quantity
