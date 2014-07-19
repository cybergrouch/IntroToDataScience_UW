import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

processed = []

def mapper(record):
    # key1: person1, value1: person2
    # key2: person2, value2: person2
    person1 = record[0]
    person2 = record[1]

    key1 = (person1, person2)
    if key1 not in processed:
        mr.emit_intermediate(person1, person2)
        processed.append(key1)

def reducer(key, list_of_values):
    # key: person1
    # value: list of other persons associated with person1
    mr.emit((key, len(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
