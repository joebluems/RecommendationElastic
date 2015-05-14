import csv
import json

### read the output from MAHOUT and collect into hash ###
indicators={}
with open('output/part-r-00000','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    for row in csv_reader:
      ##### film indicators ###
      if float(row[2])>0.95:
        if row[0] not in indicators: indicators[row[0]]=[]
        if row[1] not in indicators: indicators[row[1]]=[]              
	indicators[row[0]].append(row[1])
	indicators[row[1]].append(row[0])
 
### print out the array of recs for each film ### 
for a in indicators:
    print '{ "update" : {"_id" : "%s", "_type" : "film", "_index" : "movie"} }'% a  
    print('{"doc": {"indicators":%s}}') % json.dumps(indicators[a])
