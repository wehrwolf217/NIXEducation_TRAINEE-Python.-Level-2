--Придумать 3 запроса, которые можно оптимизировать с помощью индекса (проверять стоит ли оптимизировать запрос оператором explain) и оптимизировать их используя индекс. Результат проверять также оператором explain.


EXPLAIN SELECT * FROM users WHERE country = 'country 6';
                       QUERY PLAN                       
--------------------------------------------------------
 Seq Scan on users  (cost=0.00..97.50 rows=1 width=147)
   Filter: ((country)::text = 'country 6'::text)
(2 rows)

CREATE INDEX country_ind ON users(country);
CREATE INDEX

EXPLAIN SELECT * FROM users WHERE country = 'country 6';
                                QUERY PLAN                                 
---------------------------------------------------------------------------
 Index Scan using country_ind on users  (cost=0.28..8.30 rows=1 width=147)
   Index Cond: ((country)::text = 'country 6'::text)
(2 rows)





EXPLAIN ANALYZE SELECT FROM orders WHERE order_status_order_status_id = 3;
                                             QUERY PLAN                                              
-----------------------------------------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..31.75 rows=293 width=0) (actual time=0.035..0.903 rows=293 loops=1)
   Filter: (order_status_order_status_id = 3)
   Rows Removed by Filter: 1207
 Planning Time: 0.166 ms
 Execution Time: 1.021 ms
(5 rows)

CREATE INDEX ord_status_id ON orders(order_status_order_status_id);
CREATE INDEX

EXPLAIN ANALYZE SELECT FROM orders WHERE order_status_order_status_id = 3;
                                                          QUERY PLAN                                                           
-------------------------------------------------------------------------------------------------------------------------------
 Index Only Scan using ord_status_id on orders  (cost=0.28..9.40 rows=293 width=0) (actual time=0.238..0.412 rows=293 loops=1)
   Index Cond: (order_status_order_status_id = 3)
   Heap Fetches: 0
 Planning Time: 0.638 ms
 Execution Time: 0.511 ms
(5 rows)





EXPLAIN ANALYZE SELECT * FROM products WHERE category_id = 12;
                                               QUERY PLAN                                                
---------------------------------------------------------------------------------------------------------
 Seq Scan on products  (cost=0.00..155.00 rows=203 width=68) (actual time=0.050..0.566 rows=203 loops=1)
   Filter: (category_id = 12)
   Rows Removed by Filter: 3797
 Planning Time: 0.071 ms
 Execution Time: 0.590 ms
(5 rows)

CREATE INDEX cat_id_indx ON products(category_id);
CREATE INDEX

EXPLAIN ANALYZE SELECT * FROM products WHERE category_id = 12;
                                                       QUERY PLAN                                                       
------------------------------------------------------------------------------------------------------------------------
 Bitmap Heap Scan on products  (cost=5.85..113.88 rows=203 width=68) (actual time=0.086..0.309 rows=203 loops=1)
   Recheck Cond: (category_id = 12)
   Heap Blocks: exact=52
   ->  Bitmap Index Scan on cat_id_indx  (cost=0.00..5.80 rows=203 width=0) (actual time=0.055..0.055 rows=203 loops=1)
         Index Cond: (category_id = 12)
 Planning Time: 0.188 ms
 Execution Time: 0.388 ms
(7 rows)


