--Создать функцию, которая сетит shipping_total = 0 в таблице order, если город юзера равен x. Использовать IF clause.


CREATE OR REPLACE FUNCTION set_shipping(_city varchar) 
RETURNS varchar 
AS $$

BEGIN

IF _city IN (SELECT city FROM (SELECT users.city, orders.shipping_total 
FROM users
JOIN carts ON users.user_id = carts.users_user_id
JOIN orders ON orders.carts_cart_id = carts.cart_id) AS x)

THEN
UPDATE orders SET shipping_total = 0 WHERE order_id = (
SELECT order_id FROM (SELECT orders.order_id
FROM users
JOIN carts ON users.user_id = carts.users_user_id
JOIN orders ON orders.carts_cart_id = carts.cart_id 
WHERE _city = users.city) AS y);

RETURN format('for orders which city is %s shipping_total = 0 is set', _city);

ELSE RETURN format('no orders with such user_city %s', _city);
END IF;

END; $$
LANGUAGE plpgsql;



