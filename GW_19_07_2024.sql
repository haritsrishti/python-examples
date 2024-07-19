--Write a query to find all orders placed by customer aged 25 or above
SELECT o.*, c.age, c.first_name
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
WHERE c.age >= 25;

-- List the total amount spend by customers with their first and last name

SELECT c.first_name, c.last_name, o.amount, SUM(o.amount) total_sum
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;


--Find the first name, last name, and total amount spent by customers who have placed an order for a 'Keyboard' and have a shipping status of 'Pending'.

SELECT c.first_name, c.last_name, o.amount, SUM(o.amount) total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Shippings s ON c.customer_id = s.customer
WHERE o.item = 'Keyboard' AND s.status = 'Pending'
GROUP BY c.customer_id;


--Find the first name, last name, and total amount spent by customers who have placed at least two orders, with at least one order for an item costing more than 1000, and have at least one shipment that is 'Pending'. Additionally, include the count of their total orders and the maximum amount of a single order they have placed


SELECT c.first_name, c.last_name, SUM(o.amount) AS total_amount_spent,  COUNT(o.order_id) AS total_orders, MAX(o.amount) AS max_single_order_amount
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Shippings s ON c.customer_id = s.customer
WHERE s.status = 'Pending' AND o.amount > 1000
GROUP BY c.customer_id
HAVING COUNT(o.order_id) >= 2



-- For each customer, what are the details of their orders, including the items they ordered, the amount spent on each item, and the shipping status of their orders?

SELECT c.customer_id, c.first_name, c.last_name, o.item, o.amount, s.status
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Shippings s ON c.customer_id = s.customer
ORDER BY c.customer_id
