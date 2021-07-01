import csv
import json
import pathlib

data={}
data2=[]
#csvFilePath='/courses/par3.csv'
#jsonFilePath='/fixtures/student_3.json'
csvFilePath='/courses/par2.csv'
jsonFilePath='/fixtures/student_2.json'

path=str(pathlib.Path().absolute())
try:
    with open(path+csvFilePath) as csvFile:
        csvReader=csv.DictReader(csvFile)
        for rows in csvReader:
            id=rows['matricula']
            data[id]=rows
    
except:
    print("An exception occurred when you tried to read the CSV file")
for i in data.keys():
        d={}
        d['model']='evaluation.Student'
        d['fields']=data[i]
        d['fields']['matricula']=int(d['fields']['matricula'])
        d['fields']['group']=int(d['fields']['group'])
        d['fields']['paralelo']=int(d['fields']['paralelo'])
        data2.append(d)

try:
    with open(path+jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data2, indent=4))
except:
    print ("An exception occurred when you tried to create the JSON file")