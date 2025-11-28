-- Window Functions --
-- There are 3 types of window functions 
-- Ranking --> row_number(), rank(), dense_rank(), percent_rank(), ntile()
-- Aggregate --> avg(), max(), min(), sum(), count()
-- Value --> lag(), lead(), first_value(), last_value(), nth_value()
-- Running total -> sum() with over()
-- Averaging without using group by -> avg() over()



-- Rank by customers by their points;
use sql_store;
select customer_id, points,  rank() over(order by points desc) as rank_points
from customers; 

use sql_store;
select customer_id, points,  dense_rank() over(order by points desc) as rank_points
from customers; 



-- Running total of invoice payments
use sql_invoicing;
select invoice_id, payment_total, 
sum(payment_total) over( order by invoice_id) as running_total 
from invoices;




-- Number of order per customer without group by
use sql_store;
select customer_id, 
	count(order_id) over( partition by customer_id) as total_orders
from orders;



-- Compare current order with previous orders ( LAG)
use sql_store;
select order_id, customer_id, order_date
, LAG(order_date, 1) over( partition by customer_id order by order_date) as previous_orders
from orders;




-- CTE's  -- Common Table Expressions

use sql_store;
with my_cte as ( 
	select * from customers
    where points >= 500
    )
select first_name from my_cte;


use sql_invoicing;
with total_invoices as (
	select client_id, sum(invoice_total) as total_inv_amount
    from invoices
    group by client_id
)

select c.client_id, c.name, t.total_inv_amount
from clients c  join total_invoices t
on c.client_id = t.client_id;




-- CTE with Window Functions
use sql_invoicing;
with payments_cte as (
	select invoice_id, payment_total from invoices
    )
select *, 
sum(payment_total) over (order by invoice_id) as running_total 
from payments_cte;