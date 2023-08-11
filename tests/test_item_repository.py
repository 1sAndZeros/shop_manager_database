from lib.item_repository import ItemRepository
from lib.item import Item

"""
When we call itemRepository#all
We get a list of item objects reflecting the seed data.
"""


def test_get_all_records(db_connection):
    # Seed our database with some test data
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)  # Create a new ItemRepository

    items = repository.all()  # Get all items

    # Assert on the results
    assert items == [
        Item(1, 'PS5', 349.99, 20),
        Item(2, 'Laptop', 529.99, 1),
        Item(3, 'XBox', 249.99, 15),
        Item(4, 'iPhone', 849.99, 200),
        Item(5, 'TV', 149.99, 42),
        Item(6, 'DVD Player', 19.99, 7),
        Item(7, 'Gaming PC', 799.99, 3)
    ]


def test_find_item_by_id(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)
    item = repository.find(4)
    assert item == Item(4, 'iPhone', 849.99, 200)


def test_create_item(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)
    item = Item(None, 'iMac', 1299.99, 11)
    repository.create(item)
    items = repository.all()
    assert items == [
        Item(1, 'PS5', 349.99, 20),
        Item(2, 'Laptop', 529.99, 1),
        Item(3, 'XBox', 249.99, 15),
        Item(4, 'iPhone', 849.99, 200),
        Item(5, 'TV', 149.99, 42),
        Item(6, 'DVD Player', 19.99, 7),
        Item(7, 'Gaming PC', 799.99, 3),
        Item(8, 'iMac', 1299.99, 11)
    ]


def test_delete_item(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)
    repository.delete(3)
    items = repository.all()
    assert items == [
        Item(1, 'PS5', 349.99, 20),
        Item(2, 'Laptop', 529.99, 1),
        Item(4, 'iPhone', 849.99, 200),
        Item(5, 'TV', 149.99, 42),
        Item(6, 'DVD Player', 19.99, 7),
        Item(7, 'Gaming PC', 799.99, 3)
    ]
