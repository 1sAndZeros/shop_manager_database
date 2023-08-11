from lib.item import Item


class ItemRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from items')
        for row in rows:
            print(row)
        return [Item(row["id"], row["name"], row["price"], row["qty"]) for row in rows]

    # find item by id
    def find(self, id):
        rows = self._connection.execute(
            f"SELECT * FROM items WHERE id = %s", [id])
        item_dict = rows[0]
        return Item(item_dict['id'], item_dict['name'], item_dict['price'], item_dict['qty'])

    def create(self, item):
        self._connection.execute('INSERT INTO items (name, price, qty) VALUES (%s, %s, %s)', [
                                 item.name, item.price, item.qty])
        return None

    def delete(self, item_id):
        self._connection.execute('DELETE FROM items WHERE id = %s', [item_id])
        return None
