class Order:
    def __init__(self, id: int, customer_name: str, order_date: str, items=[]) -> None:
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
        self.items = items

    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__

    def __repr__(self) -> str:
        return f"#{self.id} - {self.customer_name} - {self.order_date} - {len(self.items)} item(s)"

    # def add_item(self, item):
    #     self.items.append(item)
