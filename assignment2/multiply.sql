select sum(prod)
from (
    select mA.value * mB.value AS prod
    from
        (select * from a where row_num = 2) mA,
        (select * from b where col_num = 3) mB
    where
        mA.col_num = mB.row_num
);