import MapReduce
import sys

mr = MapReduce.MapReduce()
processed = []

# =============================
# Do not modify above this line

def mapper(dna_record):
    # key: sequence identifier
    # value: dna sequence
    key = dna_record[0]
    value = dna_record[1]
    mr.emit_intermediate(key, value[:-10])

def reducer(key, list_of_values):
    # key: sequence identifier
    # value: dna sequence trimmed
    for v in list_of_values:
        if v not in processed:
            mr.emit(v)
            processed.append(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
