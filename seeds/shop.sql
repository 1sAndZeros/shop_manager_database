DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq CASCADE;
DROP TABLE IF EXISTS orders_items CASCADE;

CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price FLOAT,
    qty INT
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name TEXT,
    order_date DATE -- Change the data type to DATE
);

CREATE TABLE orders_items (
    order_id INT,
    item_id INT,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE, -- Correct reference to "orders(id)"
    CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE,
    PRIMARY KEY (order_id, item_id)
);

INSERT INTO items (name, price, qty) VALUES
('PS5', 349.99, 20),
('Laptop', 529.99, 1),
('XBox', 249.99, 15),
('iPhone', 849.99, 200),
('TV', 149.99, 42),
('DVD Player', 19.99, 7),
('Gaming PC', 799.99, 3);

INSERT INTO orders (customer_name, order_date) VALUES
('Rikie Patrick', '2023-08-11'),
('John Forster', '2022-12-03'),
('Hafsah Saleh', '2021-01-25');

INSERT INTO orders_items (order_id, item_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 4),
(2, 7),
(3, 5),
(3, 6);
