select sum(product)
from (
    select f1.docId AS rowDoc, f2.docId AS colDoc, f1.term, f1.count, f2.count, f1.count * f2.count AS product
    from frequency f1, frequency f2
    where
        f1.docId = "10080_txt_crude" AND f2.docId = "17035_txt_earn" AND f1.term = f2.term
)
group by rowDoc, colDoc;


