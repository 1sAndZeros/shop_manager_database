from lib.order import Order


def test_order_contructs():
    order1 = Order(1, 'Rikie Patrick', '2023/08/11')
    assert order1.id == 1
    assert order1.customer_name == 'Rikie Patrick'
    assert order1.order_date == '2023/08/11'


def test_order_format():
    order1 = Order(1, 'Rikie Patrick', '2023/08/11')
    assert str(order1) == '#1 - Rikie Patrick - 2023/08/11 - 0 items'


def test_orders_are_equal():
    order1 = Order(1, 'Rikie Patrick', '2023/08/11')
    order2 = Order(1, 'Rikie Patrick', '2023/08/11')
    assert order1 == order2
