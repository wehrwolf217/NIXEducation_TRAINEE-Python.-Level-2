--Использовать транзакции для insert, update, delete на 3х таблицах. 

BEGIN TRANSACTION;

INSERT INTO users
 (user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address, phone_number)
VALUES
 (300100, 'ivanov@gmail.com', 123, 'ivan', 'ivanov', 'ivanovich', 1, 'ukraine', 'kyiv', 'some_address', 9999);

SAVEPOINT SP1;

UPDATE users SET email = 'sidorov@gmail.com', last_name = 'sidorov' WHERE user_id = 300100;

SAVEPOINT SP2;

DELETE FROM users WHERE last_name = 'sidorov';

COMMIT;




BEGIN TRANSACTION;

INSERT INTO products 
 (product_id, product_title, product_description, in_stock, price, slug)
VALUES
 (4001, 'tomat', 'red tomat', 33, 200.2, 'somesithg');

SAVEPOINT SP1;
-- ради примера
UPDATE products SET product_description = 'yelow tomat';
--UPDATE 4001

ROLLBACK to SP1;
--ROLLBACK

UPDATE products SET product_description = 'yelow tomat' where product_id = 4001;
--UPDATE 1

DELETE FROM products WHERE product_id = 4001;

COMMIT;



BEGIN transaction;

INSERT INTO categories
(category_id, category_title, category_description)
VALUES
(21, 'new category', 'description for new category');

SAVEPOINT SP1;

UPDATE categories SET category_title = 'updated new category' WHERE category_id = 21;

DELETE FROM categories WHERE category_id = 21;

COMMIT;




