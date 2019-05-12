import csv

fileName = "abcnews-date-text.csv"

data = []
words = ["journalists", "killed", "death", "imprison", "missing", "reporter", "free", "speach", "freedom"]
with open(fileName, 'r') as fin:  
    #header
    line = fin.readline()
    data.append(line)

    line = fin.readline()
    cnt = 1
    while line:
        contain = False
        for w in words:
           if w in line:
               contain = True
               break
        
        if contain:
            data.append(line)
            
        line = fin.readline()
        cnt += 1
        if cnt % 1000 == 0:
            print cnt
    
with open('preprocessed_data.csv', 'w') as fout:
    for d in data:
        fout.write(d)