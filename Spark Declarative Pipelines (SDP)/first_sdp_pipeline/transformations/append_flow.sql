CREATE STREAMING TABLE total_sales_sql;

-- add the first append flow
CREATE FLOW append1
AS INSERT INTO total_sales_sql BY NAME
SELECT * FROM STREAM(sales_north);

-- add the second append flow
CREATE FLOW append2
AS INSERT INTO total_sales_sql BY NAME
SELECT * FROM STREAM(sales_south);
