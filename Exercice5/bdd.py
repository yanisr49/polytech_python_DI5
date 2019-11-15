import sqlite3
from Exercice5.CSVParser import *


class Database(object):

    def __init__(self):
        self.db = sqlite3.connect('bdds/mydb.db')
        print('log - Connected to the databse')
        self.c = self.db.cursor()

    def reset_tables(self):
        self.c.execute('''DROP TABLE IF EXISTS region''')
        self.db.commit()

    def create_table_region(self):
        self.c.execute('''CREATE TABLE region (code, name, nb_arr, nb_canton, nb_commune, pop_mun, pop_tot)''')
        print('log - Table region created')
        self.db.commit()

    def add_all_regions(self):
        self.c.executemany('INSERT INTO region VALUES (?, ?, ?, ?, ?, ?, ?)', Parser('bdds/regions.csv').get_data()[8:])
        self.db.commit()
        print('log - '+str(len(Parser('bdds/regions.csv').get_data()[8:]))+' row inserted')


    def add_region(self, row):
        self.c.execute("INSERT INTO region VALUES ("
                       "'"+row[0]+"', '"+row[1]+"', '"+row[2]+"', '"+row[3]+"', '"+row[4]+"', '"+row[5]+"', '"+row[6]+"')")
        self.db.commit()

    def get_pop_tot(self):
        total = 0
        for row  in self.c.execute('SELECT pop_tot FROM region'):
            total = total + int(row[-1].replace(" ", ""))
        return total

    def print_region(self):
        t = ('RHAT',)
        self.c.execute('SELECT * FROM region ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - '+str(len(self.c.execute('SELECT * FROM region').fetchall()))+' rows found')

    def close(self):
        self.db.close()

database = Database()
database.reset_tables()
database.create_table_region()
database.add_all_regions()
print(database.get_pop_tot())
database.close()