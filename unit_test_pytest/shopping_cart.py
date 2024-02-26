from typing import List


class ShoppingCart():
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.items: List[str] = []

    def add(self, item: str):
        if self.size() >= self.max_size:
            raise OverflowError("Sacola cheia!")
        self.items.append(item)

    def size(self,) -> int:
        return len(self.items)

    def get_all_item(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map) -> float:
        total = 0
        for item in self.items:
            total += price_map.get(item)
        return total
