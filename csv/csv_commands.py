import csv

#read and write. create or overwrite
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])


#read
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


#append
with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])


#read as dictionary
with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


#write with dictionary
with open("data.csv", "a") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"id": 123, "title": "New title"})