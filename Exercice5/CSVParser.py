import csv


class Parser(object):

    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        with open(self.filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            i = 0
            return [row for row in spamreader]