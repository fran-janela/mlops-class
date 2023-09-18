-- Step 0: Delete table if exists
drop table if exists sales_analytics.scoring_ml_franciscopj;

-- Step 1: Create the Table
create table sales_analytics.scoring_ml_franciscopj(
	store_id INT,
	date_sale DATE,
	year INT,
	month INT,
	day INT,
	"weekday" INT,
	total_sales numeric(10, 2)
);

-- Step 2: Insert forecasted data into the new table
insert into sales_analytics.scoring_ml_franciscopj (store_id, date_sale)
select
    s.store_id,
    generate_series(current_date , current_date + INTERVAL '6 days', INTERVAL '1 day')::DATE AS date_sale
from
    (
    	SELECT store_id
    	FROM sales.item_sale
    	group by store_id
	) as s;

-- Step 3: Set total_sales to empty (NULL) initially
update sales_analytics.scoring_ml_franciscopj
set 
	total_sales = NULL,
	"year" = extract(year from date_sale),
	"month" = extract(month from date_sale),
	"day" = extract(day from date_sale),
	"weekday" = extract(dow from date_sale);

alter table sales_analytics.scoring_ml_franciscopj drop column date_sale;

-- Reading the Table
select
	store_id,
	"year",
	"month",
	"day",
	"weekday",
	total_sales
from sales_analytics.scoring_ml_franciscopj
order by 
	store_id, 
	"year",
	"month",
	"day",
	"weekday";