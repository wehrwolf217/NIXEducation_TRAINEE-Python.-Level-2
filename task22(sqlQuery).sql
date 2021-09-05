--Сравнить цену каждого продукта n с средней ценой продуктов в категории продукта n. Использовать window function. Таблица результата должна содержать такие колонки: category_title, product_title, price, avg. Пример для решения можно найти в теории.




SELECT 
	categories.category_title, 
	products.product_title, 
	products.price,
	avg(products.price) over (partition by categories.category_id order by categories.category_id) as avg_price
from products join categories on products.category_id = categories.category_id;


