from lib.order import Order
from lib.item import Item
import datetime


class OrderRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        return [Order(row["id"], row["customer_name"], row["order_date"].strftime('%F')) for row in rows]

    # find order by id
    def find(self, id):
        rows = self._connection.execute(
            f"SELECT * FROM orders WHERE id = %s", [id])
        order = rows[0]
        return Order(order['id'], order['customer_name'], order['order_date'].strftime('%F'))

    def create(self, order):
        self._connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)', [
                                 order.customer_name, order.order_date])
        return None

    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None

    def find_by_order_id(self, order_id):
        rows = self._connection.execute(
            'SELECT * FROM orders JOIN orders_items ON orders_items.order_id = orders.id JOIN items ON orders_items.item_id = items.id WHERE orders.id = %s', [order_id])
        items = []
        for row in rows:
            items.append(
                Item(row['item_id'], row['name'], row['price'], row['qty']))
        return Order(rows[0]['order_id'], rows[0]['customer_name'], rows[0]['order_date'].strftime('%F'), items)

    def add_item(self, order_id, item_id):
        self._connection.execute('INSERT INTO orders_items (order_id, item_id) VALUES (%s, %s)', [
                                 order_id, item_id])
        return None

    def delete_item(self, order_id, item_id):
        self._connection.execute('DELETE FROM orders_items WHERE order_id = %s AND item_id = %s', [
                                 order_id, item_id])
        return None
