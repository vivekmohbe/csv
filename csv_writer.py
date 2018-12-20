import csv
import random

records=1000
print("Making %d records\n" % records)

fieldnames=['id','name','age','profession','city']
writer = csv.DictWriter(open("people1.csv", "w"), fieldnames=fieldnames)

names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai','Hyderabad']
profession=['Journalist','Engineer','Armed Forces','Professor','Civil Servant']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('id', i),
    ('name', random.choice(names)),
    ('age', str(random.randint(18,31))),
    ('profession', random.choice(profession)),
    ('city', random.choice(cities))]))
