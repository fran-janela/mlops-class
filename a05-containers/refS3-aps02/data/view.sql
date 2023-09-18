create view sales_analytics.view_abt_train_franciscopj as
	select 
		store_id,
		sum(price) as total_sales,
		extract(year from date_sale) as "year",
		extract(month from date_sale) as "month",
		extract(day from date_sale) as "day",
		extract(dow from date_sale) as  "weekday"
	from sales.item_sale as sales
	where
		sales.date_sale >= CURRENT_DATE - interval '1year' AND
		sales.date_sale < CURRENT_DATE
	group by
		store_id, 
		sales.date_sale
	order by 
		store_id,
		sales.date_sale