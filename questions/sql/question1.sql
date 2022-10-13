select
        DATE_FORMAT(`date`, "%d/%m/%Y") as `date`,
        sum(prod_price * prod_qty) as ventes
from
    TRANSACTIONS
where
    `date` between '20190101' and '20191231'
group by `date`
order by `date`