class Item:
    def __init__(self, id: int, name: str, price: float, qty: int) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __repr__(self) -> str:
        return f"#{self.id} - {self.name} - £{self.price} - {self.qty} in stock"
    