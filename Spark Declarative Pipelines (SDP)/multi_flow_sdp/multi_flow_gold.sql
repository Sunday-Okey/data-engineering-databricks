

------------------------------------------
-- a. GOLD MATERIALIZED VIEW: DAILY SUBSIDIARY SCORECARD
-- Simple daily summary by subsidiary
------------------------------------------
CREATE OR REPLACE MATERIALIZED VIEW multi_flow_3_gold.mv_daily_subsidiary_scorecard_demo
AS
SELECT
  order_date,
  subsidiary_id,
  COUNT(DISTINCT order_id)    AS order_count,   -- how many unique orders occurred
  ROUND(SUM(total_amount),2)  AS total_revenue, -- total revenue for the day
  SUM(qty)                    AS total_units    -- total units sold
FROM multi_flow_2_silver.orders_silver_flows_demo
WHERE order_date IS NOT NULL
GROUP BY order_date, subsidiary_id;


------------------------------------------
-- b. GOLD MATERIALIZED VIEW: PRODUCT PERFORMANCE BY SUBSIDIARY
-- Basic units and revenue by product and subsidiary
------------------------------------------
CREATE OR REPLACE MATERIALIZED VIEW multi_flow_3_gold.mv_product_performance_by_subsidiary_demo
AS
SELECT
  subsidiary_id,
  category,
  sku,
  SUM(qty)                   AS units_sold,  -- total units sold for each SKU
  ROUND(SUM(total_amount),2) AS revenue      -- total revenue for each SKU
FROM multi_flow_2_silver.orders_silver_flows_demo
GROUP BY subsidiary_id, category, sku;

