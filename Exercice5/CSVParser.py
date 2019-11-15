import csv


class Parser(object):

    def __init__(self):
        print("log - Parser, created")

    def get_regions(self):
        with open("bdds/regions.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [row[0:2] for row in spamreader][8:]

    def get_departements(self):
        with open("bdds/departements.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [row[0:3] for row in spamreader][8:]

    def get_communes(self):
        with open("bdds/communes.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [[row[0], row[2], row[6], row[9]] for row in spamreader][8:]