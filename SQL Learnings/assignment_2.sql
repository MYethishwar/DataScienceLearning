
--  				SQL PRACTICE QUESTIONS

-- 	             LEVEL 1 – BASIC SELECT (10 Qs)

-- Show all clients from the sql_invoicing database.
select distinct name from clients;

-- List all products with price more than 3 from sql_store.products.
use sql_store;
select name, unit_price from products where unit_price > 3 order by unit_price;

-- Select all customers who live in Texas (TX).
select first_name, last_name, state from customers  where state = 'TX';


-- Show all employees with salary greater than 90,000.
use sql_hr;
select employee_id,first_name, salary from employees where salary > 90000;


-- Display all invoices with payment_total = 0.
use sql_invoicing;
select invoice_id, payment_total from invoices where payment_total = 0;


-- List all order statuses.
use sql_store;
select * from order_statuses;


-- Show the top 5 products with highest stock.
use sql_store;
select * from products order by quantity_in_stock desc limit 5;


-- Get all payments made using ‘Credit Card’.
use sql_invoicing;
select * from payment_methods where name = 'Credit Card';
select payments.payment_id, payment_methods.name from payments join payment_methods on 
payments.payment_method = payment_methods.payment_method_id;


-- Show all employees working in New York City.
use sql_hr;
select employees.first_name, offices.city from employees join offices on 
employees.office_id = offices.office_id
where offices.city = 'New York City';


-- Retrieve products sorted by price (highest first).
use sql_store;
select name,unit_price from products order by unit_price DESC;



--                LEVEL 2 – JOINS (10 Qs)

-- Get all invoice details along with client names.
use sql_invoicing;
select  clients.name, invoices.* from clients inner join invoices on clients.client_id = invoices.client_id;


-- List orders with customer full name and order date.
use sql_store;
select concat(customers.first_name, " ",customers.last_name) as customer_full_name, orders.order_date from customers join orders on 
customers.customer_id = orders.customer_id order by orders.order_date;



-- Show shipments with shipper name and shipped date.
select shippers.name, orders.shipped_date from shippers join orders on 
shippers.shipper_id = orders.shipper_id order by orders.shipped_date;


-- Show employees and their office locations.
use sql_hr;
select concat(employees.first_name," ", employees.last_name) as employee_name, concat(offices.address, ", ", offices.city, ", ", offices.state) as working_location
from employees join offices on 
employees.office_id = offices.office_id;


-- Display payments with client name and payment method.
select clients.name as client_name, payments.payment_id, payments.amount, payment_methods.name from payments
join clients on clients.client_id = payments.client_id 
join payment_methods on payment_methods.payment_method_id = payments.payment_method;




-- For each order, show total number of items ordered.
use sql_store;
select oi.order_id, sum(oi.quantity) as total_items
from order_items oi
group by oi.order_id; 


-- Show full details of order items including product name.
select products.name  as product_name ,order_items.*  from order_items join products on products.product_id = order_items.product_id;



-- List clients and their total invoices amount.
use sql_invoicing;
select clients.name, sum(invoices.invoice_total) as total_invoices_amount from  invoices join clients on 
clients.client_id = invoices.client_id group by clients.name;




-- Find orders with their status names (Delivered/Shipped/Processed).
use sql_store;
select orders.order_id, order_statuses.name from orders right join order_statuses on 
orders.status = order_statuses.order_status_id order by orders.order_id;



-- Get all payments with invoice numbers.
use sql_invoicing;
select payments.* , invoices.number from invoices join payments on 
invoices.invoice_id = payments.invoice_id;




--               LEVEL 3 – GROUP BY & AGGREGATE (5 Qs)

-- Find total revenue from all invoices.
use sql_invoicing;
select sum(invoice_total) as total_revenue from invoices ;



-- Show total amount paid by each client.
select clients.name, sum(payments.amount) as total_amount from clients join payments on 
clients.client_id = payments.client_id group by clients.name;


-- Number of orders placed by each customer.
use sql_store;
select customers.first_name as customer, count(orders.order_id)  as no_of_orders from 
customers join orders on customers.customer_id = orders.customer_id 
group by customers.first_name;



-- Find average salary of employees.
use sql_hr;
select round(avg(salary), 2) as average_salary from employees;



-- Show total quantity ordered for each product.
use sql_store;
select products.product_id, sum(order_items.quantity)  as total_quantity from products join order_items on
products.product_id = order_items.product_id  group by products.product_id;



--                  LEVEL 4 – SUBQUERIES (5 Qs)

-- Show clients who paid more than 50 in total.
use sql_invoicing;
select clients.name, sum(payments.amount) as paid from clients join payments on
clients.client_id = payments.client_id group by clients.client_id
having paid > 50;



-- List products that were never ordered.
use sql_store;
select products.product_id, products.name, count(order_items.order_id) as ordered from products join order_items
on products.zproduct_id = order_items.product_id  group by product_id 
having ordered = 0;


-- Get customers who placed more than 2 orders.
-- There exist no customers who placed order more than 2
use sql_store;
select concat(customers.first_name, " ", customers.last_name) as customer_name , count(orders.order_id) as no_of_orders 
from customers join orders on
customers.customer_id = orders.customer_id 
group by customer_name
having no_of_orders > 1; 



-- Show employees whose salary is above the company average.
use sql_hr;
select  employees.first_name, employees.salary from employees 
where salary  > (select avg(salary) from employees) order by salary ;




-- Get invoices that are fully paid.
SELECT *
FROM invoices
WHERE payment_total < invoice_total;


--                 LEVEL 5 – ADVANCED (BONUS: 8 Qs)
-- Create a view showing client name + total payments.
use sql_invoicing;
create view client_total_payments as
select clients.name, sum(payments.amount)  as total_amount from clients join payments on
clients.client_id = payments.client_id  group by clients.name;

select * from client_total_payments;




use sql_invoicing;




-- Find the average invoice total and list 
-- invoices higher than that average
select * from invoices where invoice_total > 
(select avg(invoice_total) from invoices) ;
select avg(invoice_total) from invoices;




-- show the employyes with highest salay
use sql_hr;
select * from employees where salary =
(select max(salary)  from employees);



-- list customers who haven't placed any orders;
use sql_store;
select * from customers 
where customer_id not in (select customer_id from orders);




-- Find products that have never been orderd
use sql_store;
select * from products where product_id not in 
(select product_id from order_items);

select * from order_items;





 -- show clients who paid more than the average total payment amount
use sql_invoicing;




-- show  products whose stock is higher than the avg stock of all products
use sql_store;
select * from products where quantity_in_stock > 
(select avg(quantity_in_stock) from products);




-- Rank customers by points using window function.
use sql_store;
select customers.first_name, customers.points, rank() over(order by points) as ranking from customers; 



-- Find top 3 most expensive products.
select * from products order by unit_price  desc limit 3;

SELECT *
FROM (
    SELECT 
        product_id,
        products.name,
        unit_price,
        RANK() OVER (ORDER BY unit_price DESC) AS price_rank
    FROM products
) AS ranked
WHERE price_rank <= 3;

    
    
-- Get revenue per year from invoices.
use sql_invoicing;
select month(invoices.invoice_date) as month, count(*) as no_of_payments,  sum(invoice_total) as revenue from invoices
group by month(invoices.invoice_date) order by month;


-- Show orders shipped within 1 day (fast delivery).
use sql_store;
select orders.order_id, order_statuses.name from orders join order_statuses on 
orders.status = order_statuses.order_status_id 
where order_statuses.name = 'Shipped' ;

SELECT orders.order_id,orders.order_date, orders.shipped_date, order_statuses.name from orders join order_statuses on orders.status = order_statuses.order_status_id
WHERE DATEDIFF(shipped_date, order_date) = 1 ;



-- Find employees who are managers (who have subordinates).
select employee_id, first_name, last_name from employees 
where employee_id in 
	(select  reports_to from employees where reports_to is not null); 


-- Show clients with pending payments.
SELECT *
FROM invoices
WHERE payment_total < invoice_total;



-- Find most frequently ordered product
use sql_store;
select products.name as product_name,count(order_items.order_id)  as no_of_orders from products join order_items on
products.product_id = order_items.product_id group by products.product_id order by no_of_orders desc limit 3;


call getAllEmployees;


