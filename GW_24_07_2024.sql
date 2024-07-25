---find the cusotmers who have spent more than the average amount per order.
---for each customer provide first, last name, total amount spent and
---number of order they placed


SELECT c.first_name,
       c.last_name,
       sum(o.amount) total_amount,
       COUNT(o.order_id) no_of_orders
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_id
HAVING o.amount>(SELECT avg(amount)
                 FROM orders);



---retrieve the order ids, items and amounts for all orders where the
---amount spent is higher than the maximum amount of any pending shipment


SELECT item,
       order_id,
       amount
FROM orders
WHERE amount>(SELECT max(amount)
              FROM orders
              WHERE customer_id
              IN (SELECT customer
                  FROM shippings
                  WHERE status="Pending"));


---Retrieve the items and their corresponding amounts for orders that have an
---amount greater than the minimum amount of any 'Delivered' shipment.

SELECT item,
       amount
FROM orders
WHERE amount>(SELECT min(amount)
              FROM orders
              WHERE  customer_id
              IN (SELECT customer
                  FROM shippings
                  WHERE status="Delivered" ));