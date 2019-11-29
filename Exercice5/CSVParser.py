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
            return [[row[2], row[3], row[0], 0] for row in spamreader][8:]

    def get_communes(self):
        with open("bdds/communes.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            return [[row[5], row[6], row[9], row[2]] for row in spamreader][8:]

    def get_new_regions(self):
        with open("bdds/zones-2016.csv", newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            reg_result = []
            for row in spamreader:
                if row[0] == "REG":
                    reg_result.append([row[1], row[2]])
            return reg_result