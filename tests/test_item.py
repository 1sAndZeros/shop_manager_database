from lib.item import Item


def test_item_contructs():
    item1 = Item(1, 'PS5', 349.99, 20)
    assert item1.id == 1
    assert item1.name == 'PS5'
    assert item1.price == 349.99
    assert item1.qty == 20


def test_item_format():
    item1 = Item(1, 'PS5', 349.99, 20)
    assert str(item1) == '#1 - PS5 - £349.99 - 20 in stock'


def test_items_are_equal():
    item1 = Item(1, 'PS5', 349.99, 20)
    item2 = Item(1, 'PS5', 349.99, 20)
    assert item1 == item2
