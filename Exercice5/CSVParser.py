import csv


class Parser(object):

    def __init__(self):
        print("log - Parser, created")

    def get_regions(self):
        with open("bdds/regions.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [[row[0], row[1]] for row in spamreader][8:]

    def get_departements(self):
        with open("bdds/departements.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [[row[2], row[3], int(row[0])] for row in spamreader][8:]

    def get_communes(self):
        with open("bdds/communes.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [[int(row[5]), str(row[6]), int(row[9]), int(row[2])] for row in spamreader][8:]