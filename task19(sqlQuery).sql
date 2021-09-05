--Написать представление 
--для таблицы products, 
--для таблиц order_status и order, 
--для таблиц products и category


CREATE VIEW count_prod  (cat_id, count_prod)
AS SELECT products.category_id, COUNT(*)
FROM products GROUP BY category_id;


CREATE VIEW ord_id_stat_name (order_id, carts_cart_id, status_name)
AS SELECT orders.order_id, orders.carts_cart_id, order_status.status_name
FROM orders INNER JOIN order_status ON orders.order_status_order_status_id = order_status.order_status_id;



CREATE VIEW prod_categories (product_title, categoty_title, category_description)
AS SELECT products.product_title, categories.category_title, categories.category_description
FROM products INNER JOIN categories ON products.category_id = categories.category_id;
