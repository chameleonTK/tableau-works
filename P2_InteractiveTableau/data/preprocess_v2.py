import csv

fileName = "journalists_imprisoned_killed_missing_short.csv"

data = []
coverages = ["Business","Corruption","Crime","Culture","Human Rights","Politics","War","Sports"]
#attr ['year', 'fullName', 'primaryNationality', 'secondaryNationality', 'tertiaryNationality', 'gender', 'photoUrl', 'photoCredit', 'typeOfDeath', 'status', 'employedAs', 'organizations', 'jobs', 'coverage', 'mediums', 'country', 'location', 'region', 'state', 'locality', 'province', 'localOrForeign', 'sourcesOfFire', 'motiveConfirmed', 'impunityMurder', 'tortured', 'captive', 'threatened', 'charges', 'lengthOfSentence', 'healthProblems', 'sentence', 'locationImprisoned']


with open(fileName, 'r') as fin:  
    reader = csv.reader(fin)
    data = list(reader)
    attrs = data[0]
    # for c in coverages:
    #     data[0].append("workWith"+c)

newData = [["id"]+data[0]]
for id in xrange(1, len(data)):
    cov = data[id][13].split(",")
    for c in cov:
        d = [str(id)] + list(data[id])
        d[14] = c
        newData.append(d)

with open('preprocessed_data_2.csv', 'w') as fout:
    writer = csv.writer(fout)
    writer.writerows(newData)