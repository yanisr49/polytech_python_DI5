from classe import *
import csv

students = []

with open('fichetu.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		bd = row[2].split("/")
		students.append(Etudiant(row[0], row[1], Date(bd[0], bd[1], bd[2])))
		
print(students)
