import csv
header = ['FirstName','LastName','DOB','Age']
file = open('patients.csv, 'a', newline=')
db = csv.writer(file)
db.writerow(header)
file.close()