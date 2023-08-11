from lib.item import Item


class ItemRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from items')
        items = []
        for row in rows:
            item = Item(row["id"], row["name"], row["price"], row["qty"])
            items.append(item)
        return items

    # find item by id
    def find(self, id):
        rows = self._connection.execute(
            f"SELECT * FROM items WHERE id = %s", [id])
        item_dict = rows[0]
        return Item(item_dict['id'], item_dict['title'], item_dict['release_year'], item_dict['artist_id'])

    def create(self, item):
        self._connection.execute('INSERT INTO items (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                 item.title, item.release_year, item.artist_id])
        return None

    def delete(self, item_id):
        self._connection.execute('DELETE FROM items WHERE id = %s', [item_id])
        return None
