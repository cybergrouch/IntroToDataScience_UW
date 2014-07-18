select max(similarity)
from (
    select sum(product) as similarity
    from (
        select f1.docId AS rowDoc, f2.docId AS colDoc, f1.term, f1.count, f2.count, f1.count * f2.count AS product
        from 
            (
                SELECT * FROM frequency
                UNION
                SELECT 'q' as docid, 'washington' as term, 1 as count 
                UNION
                SELECT 'q' as docid, 'taxes' as term, 1 as count
                UNION 
                SELECT 'q' as docid, 'treasury' as term, 1 as count
            ) f1, 
            (
                SELECT * FROM frequency
                UNION
                SELECT 'q' as docid, 'washington' as term, 1 as count 
                UNION
                SELECT 'q' as docid, 'taxes' as term, 1 as count
                UNION 
                SELECT 'q' as docid, 'treasury' as term, 1 as count
            ) f2
        where
            f1.docId < f2.docId AND f1.term = f2.term AND (f1.docId = 'q' OR f2.docId = 'q')
    )
    group by rowDoc, colDoc
);


