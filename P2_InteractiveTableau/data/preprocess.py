import csv

fileName = "journalists_imprisoned_killed_missing_short.csv"

data = []
coverages = ["Business","Corruption","Crime","Culture","Human Rights","Politics","War","Sports"]
with open(fileName, 'r') as fin:  
    reader = csv.reader(fin)
    data = list(reader)
    data[0].insert(0, "id")

    for c in coverages:
        data[0].append("workWith"+c)

    for id in xrange(1, len(data)):
        data[id].insert(0, id)
        data[id][len(data[id])-1] = data[id][len(data[id])-1].strip()
        for c in coverages:
            if c in data[id][14]:
                data[id].append(True)
            else:
                data[id].append(False)

print len(data)
with open('preprocessed_data.csv', 'w') as fout:
    writer = csv.writer(fout)
    writer.writerows(data)
#    header = fin.readline().strip().split(",")

#    header
#    fout.write(",".join(header)+"\n")
#    index = 1

#    line = fin.readline()
#    while line:
#         item = line.strip().split(",")
#         item.insert(0, str(index))
#         print csv.reader(item, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        

#         fout.write(",".join(item)+"\n")
#         line = fin.readline()
#         index += 1

#         print item
#         break

fout.close()