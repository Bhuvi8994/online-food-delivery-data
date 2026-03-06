CREATE DATABASE online_delivery;
USE online_delivery;

SELECT COUNT(*) FROM food_orders;

SELECT * FROM food_orders LIMIT 10;

--- Identify top-spending customers ----
Select customer_id, SUM(order_value) as total_spent
from online_delivery
GROUP BY customer_id
ORDER BY total_spent DESC;

--- Analyze age group vs order value ---
Select Customer_Age, AVG(order_value) as avg_order_value, COUNT(*) as total_order
from online_delivery
GROUP BY Customer_Age
ORDER BY avg_order_value DESC

-- Weekend vs weekday order patterns ---
Select order_day, COUNT(*) AS total_order, AVG(order_value) AS avg_order_value
from online_delivery
GROUP BY order_day;

--- Monthly revenue trends ---
Select DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(order_value) AS Monthly_revenue 
FROM online_delivery
GROUP BY month
order by month;

--- Impact of discounts on profit ---
Select Final_Amount, AVG(profit_margin) AS AVG_profit
from online_delivery 
GROUP BY Final_amount 
order by avg_profit DESC;

--- High-revenue cities and cuisines ---
Select City, SUM(final_amount) AS total_revenue
From online_delivery
GROUP BY City
Order By total_revenue DESC;
 
 Select Cuisine_Type, SUM(final_amount) AS total_revenue
 from online_delivery
 GROUP BY Cuisine_Type
 ORDER BY total_revenue DESC;

--- Average delivery time by city ---
Select city, AVG(Delivery_Time_Min) AS avg_delivery_time
from online_delivery	
GROUP BY city 
ORDER BY avg_delivery_time;

--- Distance vs delivery delay analysis ---
select distance_km, AVG(delivery_time_min) AS avg_delivery_time
From online_delivery	
GROUP BY distance_km
ORDER BY distance_km;

--- Delivery rating vs delivery time ----
Select Delivery_Rating, AVG(delivery_time_min) AS avg_delivery_time
from online_delivery
GROUP BY Delivery_Rating
ORDER BY Delivery_Rating DESC;

--- Top-rated restaurants ---
Select Restaurant_Name, AVG(Restaurant_rating) AS avg_rating
from online_delivery	
GROUP BY Restaurant_Name
ORDER BY Restaurant_name DESC
LIMIT 10;

--- Cancellation rate by restaurant ---
SELECT 
    restaurant_name,
    COUNT(*) AS cancelled_orders
FROM food_orders
WHERE order_status = 'cancelled'
GROUP BY restaurant_name;

--- Cuisine-wise performance ---
Select Cuisine_type, Count(*) AS total_order
From online_delivery
GROUP BY Cuisine_type;

--- Peak hour demand analysis ---
Select HOUR(order_time) AS order_hour, COUNT(*) AS total_order
From online_delivery
GROUP BY order_hour
ORDER BY total_order DESC;

--- Payment mode preferences ---
Select Payment_Mode, count(*) AS Total_order
from online_delivery
GROUP BY Payment_Mode
ORDER BY Total_order DESC;

--- Cancellation reason analysis ---
Select Cancellation_Reason, COUNT(*) AS Total_Cancellation
From online_delivery
WHERE order_status = 'cancelled'
GROUP BY Cancellation_Reason
ORDER BY total_Cancellation DESC;

