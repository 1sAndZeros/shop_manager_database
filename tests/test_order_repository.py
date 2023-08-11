from lib.order_repository import OrderRepository
from lib.order import Order
from lib.item import Item

"""
When we call orderRepository#all
We get a list of order objects reflecting the seed data.
"""


def test_get_all_records(db_connection):
    # Seed our database with some test data
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)  # Create a new OrderRepository

    orders = repository.all()  # Get all orders

    # Assert on the results
    assert orders == [
        Order(1, 'Rikie Patrick', '2023-08-11'),
        Order(2, 'John Forster', '2022-12-03'),
        Order(3, 'Hafsah Saleh', '2021-01-25')
    ]


def test_find_order_by_id(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    order = repository.find(2)
    assert order == Order(2, 'John Forster', '2022-12-03')


def test_create_order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    order = Order(None, 'Tom Jones', '1998-11-13')
    repository.create(order)
    orders = repository.all()
    assert orders == [
        Order(1, 'Rikie Patrick', '2023-08-11'),
        Order(2, 'John Forster', '2022-12-03'),
        Order(3, 'Hafsah Saleh', '2021-01-25'),
        Order(4, 'Tom Jones', '1998-11-13'),
    ]


def test_delete_order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    repository.delete(3)
    orders = repository.all()
    assert orders == [
        Order(1, 'Rikie Patrick', '2023-08-11'),
        Order(2, 'John Forster', '2022-12-03')
    ]


def test_find_items_by_order_id(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    order = repository.find_by_order_id(1)
    assert order == Order(1, 'Rikie Patrick', '2023-08-11', [
        Item(1, 'PS5', 349.99, 20),
        Item(2, 'Laptop', 529.99, 1),
        Item(3, 'XBox', 249.99, 15),
        Item(4, 'iPhone', 849.99, 200)
    ])


def test_add_item_to_order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    repository.add_item(1, 5)
    order = repository.find_by_order_id(1)
    assert order == Order(1, 'Rikie Patrick', '2023-08-11', [
        Item(1, 'PS5', 349.99, 20),
        Item(2, 'Laptop', 529.99, 1),
        Item(3, 'XBox', 249.99, 15),
        Item(4, 'iPhone', 849.99, 200),
        Item(5, 'TV', 149.99, 42)
    ])


def test_delete_item_from_order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    repository.delete_item(1, 2)
    order = repository.find_by_order_id(1)
    assert order == Order(1, 'Rikie Patrick', '2023-08-11', [
        Item(1, 'PS5', 349.99, 20),
        Item(3, 'XBox', 249.99, 15),
        Item(4, 'iPhone', 849.99, 200),
    ])
