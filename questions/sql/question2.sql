select
        tr.client_id,
        sum(CASE WHEN prd.product_type = "MEUBLE" then (tr.prod_price * tr.prod_qty) END) as ventes_meuble,
        sum(CASE WHEN prd.product_type = "DECO" then (tr.prod_price * tr.prod_qty) END) as ventes_deco
from
    TRANSACTIONS tr
    LEFT JOIN PRODUCT_NOMENCLATURE prd ON tr.prop_id= prd.product_id
where
    `date` between '20190101' and '20191231'
group by client_id