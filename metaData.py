import csv
import re
import json

### extract year from date format: dd-Mon-ccyy ###

count=0
with open('./u.item','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='|')
    for row in csv_reader:
        title = re.sub(" \(.*\)$", "", re.sub('"','',row[1]))
        genre=[]
        if row[6]=='1': genre.append("Action")
        if row[7]=='1': genre.append("Adventure")
        if row[8]=='1': genre.append("Animation")
        if row[9]=='1': genre.append("Children")
        if row[10]=='1': genre.append("Comedy")
        if row[11]=='1': genre.append("Crime")
        if row[12]=='1': genre.append("Documentary")
        if row[13]=='1': genre.append("Drama")
        if row[14]=='1': genre.append("Fantasy")
        if row[15]=='1': genre.append("Noir")
        if row[16]=='1': genre.append("Horror")
        if row[17]=='1': genre.append("Musical")
        if row[18]=='1': genre.append("Mystery")
        if row[19]=='1': genre.append("Romance")
        if row[20]=='1': genre.append("Sci-Fi")
        if row[21]=='1': genre.append("Thriller")
        if row[22]=='1': genre.append("War")
        if row[23]=='1': genre.append("Western")
        print '{ "create" : { "_index" : "movie", "_type" : "film", "_id" : "%s" } }' % row[0]
        print '{ "title" : "%s", "year":"%s" , "url":"%s", "genre":%s }' % (title,row[2][-4:],row[4],json.dumps(genre))
