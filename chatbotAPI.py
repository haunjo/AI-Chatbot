
import json
import csv
import pandas as pd

# def csv2json(csvpath, jsonpath):
#     result = {}
#     with open(csvpath) as csvf:
#         csvReader = csv.DictReader(csvf)
        
#         for rows in csvReader:
#             key = rows['No.']
#             result[key] = rows
            
            
#     with open(jsonpath, 'w', encoding='utf-8') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))
        
def readCsv():
    with open("pill.csv", 'r', encoding='utf-8') as csvf:
        df = pd.DataFrame(csvf)
        print(df[A])
        
readCsv()