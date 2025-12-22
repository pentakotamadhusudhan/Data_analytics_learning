use online_shop;

desc orders;

select * from orders limit 50;

select count(*) as total_order, customer_id from orders group by customer_id limit 5;

show tables;

select p.product_name,c.category_id from products p left join categories c on c.category_id= p.category_id order by c.category_id;
select p.product_name,c.category_id from products p left join categories c on c.category_id= p.category_id where c.category_id =1;

select c.customer_id,o.customer_id from customers c left join orders o  on c.customer_id = o.customer_id where o.customer_id is null ;  
SELECT c.customer_id,o.customer_id FROM Customers c LEFT JOIN Orders o ON c.customer_id = o.customer_id WHERE o.customer_id IS NULL;

select count(*),region from  employees group by region;
SET SQL_SAFE_UPDATES = 0;




UPDATE employees
SET region = 'LA'
WHERE region IS NULL;

SET SQL_SAFE_UPDATES = 1;


select order_id, sum((unit_price*quantity)-discount) as revenu from order_details group by order_id;	

select  c.customer_id, sum((od.unit_price*od.quantity)-od.discount) as revenu from customers c left join orders o on o.customer_id=c.customer_id left join order_details od on o.order_id = od.order_id group by c.customer_id;

SELECT 
    c.customer_id,
    SUM(od.unit_price * od.quantity * (1 - od.discount)) AS total_revenue
FROM customers c
LEFT JOIN orders o 
    ON o.customer_id = c.customer_id
LEFT JOIN order_details od 
    ON o.order_id = od.order_id
GROUP BY c.customer_id;
