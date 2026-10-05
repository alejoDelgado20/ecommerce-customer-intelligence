-- 1. Total revenue
SELECT
    ROUND(SUM(price)::numeric, 2) AS total_revenue
FROM order_items;


-- 2. Average order value
SELECT
    ROUND(AVG(order_total)::numeric, 2) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(price) AS order_total
    FROM order_items
    GROUP BY order_id
) AS t;


-- 3. Monthly revenue
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp::timestamp) AS month,
    ROUND(SUM(oi.price)::numeric, 2) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY 1
ORDER BY 1;


-- 4. Top 10 product categories by revenue
SELECT
    p.product_category_name,
    ROUND(SUM(oi.price)::numeric, 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;