from dataclasses import dataclass, field

import coins


@dataclass
class VendingMachine:
    coins: list = field(default_factory=list)

    def insert_coin(self, coin):
        if not isinstance(coin, coins.Coin):
            raise ValueError

        self.coins.append(coin)
