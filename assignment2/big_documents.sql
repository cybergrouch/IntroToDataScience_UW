select count(*)
from (
    select docid, count(term)
    from frequency 
    group by docid
    having count(term) > 300
);
