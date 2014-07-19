import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order id
    # value: record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order id
    # value: list of records from either line_item or order table
    line_items = []
    orders = []
    for v in list_of_values:
        if v[0] == "order":
            orders.append(v)
        else:
            line_items.append(v)            
    for order in orders:
        for item in line_items:
            mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
