select
	store_id,
	total_sales,
	"year",
	"month",
	"day",
	"weekday"
from sales_analytics.view_abt_train_franciscopj
order by 
	store_id, 
	"year",
	"month",
	"day",
	"weekday";