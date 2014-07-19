import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

processed = []
ignore = []

def mapper(record):
    # key1: person1, value1: person2
    # key2: person2, value2: person2
    person1 = record[0]
    person2 = record[1]
    
    pair1 = (person1, person2)
    pair2 = (person2, person1)
    
    if pair2 in processed:
        ignore.append(pair1)
        ignore.append(pair2)
    elif pair1 not in processed:
        mr.emit_intermediate(person1, person2)
        mr.emit_intermediate(person2, person1)
        processed.append(pair1)

def reducer(key, list_of_values):
    # key: person1
    # value: list of other persons associated with person1
    processed = []
    
    for friend in uniq(list_of_values):
        p1 = (key, friend)
        if p1 not in ignore:
            processed.append(p1)

    for p in processed:
        mr.emit(p)

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
