# Design Recipe

```text
As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.
```

```text
Nouns:
shop items, item name, item unit price, qty, create item, orders, customer name, order date, create order
```

Classes:
Item / ItemRepository:
    paramters: name, price, qty
    methods: all, create
Order / OrderRepository:
    parameters: customer_name, order_date
    methods: all, create
