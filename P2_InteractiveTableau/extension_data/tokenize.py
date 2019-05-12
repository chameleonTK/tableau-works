import csv

fileName = "preprocessed_data.csv"

data = []
with open(fileName, 'r') as fin:  
    #header
    line = fin.readline()
    data.append(line)

    line = fin.readline()
    cnt = 1
    while line:
        sp = line.strip().split(",")

        date = sp[0]
        for i in range(1, len(sp)):
            token = sp[i].split(" ")
            for j in range(len(token)):
                data.append(date+", "+token[j]+"\n")
        line = fin.readline()
        cnt += 1
        
    
with open('preprocessed_data_tokens.csv', 'w') as fout:
    for d in data:
        fout.write(d)