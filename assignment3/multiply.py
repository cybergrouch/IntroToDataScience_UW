import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record => [matrix, i, j, value]
    # output key => "all"
    # output value => [matrix, (row, column), value]
    key = "all"
    value = record
    mr.emit_intermediate(key, value)
    
matrixInput = {}
iMaxCList = []
jMaxCList = []

def reducer(key, list_of_values):
    # key: arbitrary
    # value: list [matrix, row, column, value]
    for v in list_of_values:
        matrix = v[0]
        i = v[1]
        j = v[2]
        value = v[3]
        if matrix == 'a' and i not in iMaxCList:
            iMaxCList.append(i)
        elif j not in jMaxCList:
            jMaxCList.append(j)
            
        if matrix not in matrixInput:
            matrixInput[matrix] = []
        
        matrixInput[matrix].append([i, j, value])
        
    print str(matrixInput['a'])
    print "___"
    print str(matrixInput['b'])
    print "___"
    

    L = len(iMaxCList)
    N = len(jMaxCList)
    
    print "L = " + str(L) + " : " + str(iMaxCList)
    print "M = " + str(N) + " : " + str(jMaxCList)
    
    for row in range(0, L):
        for col in range(0, N):
            rowMatrix = getRow(matrixInput['a'], row, 5)
            colMatrix = getCol(matrixInput['b'], col, 5)
            zipMatrix = zip(rowMatrix, colMatrix)

            print "A row " + str(row) + ": " + str(rowMatrix)
            print "B col" + str(col) + ": " + str(colMatrix)
            print "C" + str((row, col)) + ": " + str(zipMatrix)

            runningSum = 0
            for z in zipMatrix:
                runningSum += z[0] * z[1]
            mr.emit((row, col, runningSum))

def getRow(matrix, rowIndex, jMax):
    intermediate = {}
    for v in matrix:
        if v[0] == rowIndex:
            intermediate[v[1]] = v[2]
    print "getRow intermediate : " + str(intermediate)
    output = []
    for u in range(0, jMax):
        if u in intermediate:
            output.append(intermediate[u])
        else:
            output.append(0)
    return output
    
def getCol(matrix, colIndex, iMax):
    intermediate = {}
    for v in matrix:
        # print "processing... " + str(v)
        if v[1] == colIndex:
            #print "predicate true: " + str(intermediate)
            intermediate[v[0]] = v[2]
        #else:
            #print "predicate false: " + str(intermediate)
    print "getCol intermediate : " + str(intermediate)
    output = []
    for u in range(0, iMax):
        if u in intermediate:
            output.append(intermediate[u])
        else:
            output.append(0)
    return output
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
