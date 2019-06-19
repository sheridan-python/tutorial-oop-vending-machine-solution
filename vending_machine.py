from dataclasses import dataclass, field

import coins
import products


@dataclass
class VendingMachine:
    inserted_coins: list = field(default_factory=list)

    def insert_coin(self, coin):
        if not isinstance(coin, coins.Coin):
            raise ValueError

        self.inserted_coins.append(coin)

    def buy_product(self, product):
        if not issubclass(product, products.Product):
            raise ValueError
