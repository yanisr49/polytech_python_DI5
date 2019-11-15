import sqlite3
from Exercice5.CSVParser import *


class Database(object):

    def __init__(self):
        self.db = sqlite3.connect('bdds/mydb.db')
        print('log - Connected to the database')
        self.c = self.db.cursor()
        self.parser = Parser()

    def create_all(self):
        self.reset_tables()
        self.create_table_region()
        self.create_table_departement()
        self.create_table_commune()
        self.add_all_regions()
        self.add_all_departements()
        self.add_all_communes()
        self.print_regions()
        self.print_departements()
        self.print_communes()
        self.close()

    def reset_tables(self):
        self.c.execute('''DROP TABLE IF EXISTS region''')
        self.c.execute('''DROP TABLE IF EXISTS departement''')
        self.c.execute('''DROP TABLE IF EXISTS commune''')
        self.db.commit()

    def create_table_region(self):
        self.c.execute('''CREATE TABLE region (code_region integer PRIMARY KEY, name text NOT NULL)''')
        print('log - Table region created')
        self.db.commit()

    def create_table_departement(self):
        self.c.execute(
            '''CREATE TABLE departement (code_departement integer PRIMARY KEY, name text NOT NULL, code_region integer, FOREIGN KEY(code_region) REFERENCES region(code_region))''')
        print('log - Table departement created')
        self.db.commit()

    def create_table_commune(self):
        self.c.execute(
            '''CREATE TABLE commune (code_commune integer PRIMARY KEY, name text NOT NULL, pop_tot integer,code_departement integer, FOREIGN KEY(code_departement)REFERENCES departement(code_departement))''')
        print('log - Table commune created')
        self.db.commit()

    def add_all_regions(self):
        self.c.executemany('INSERT INTO region VALUES (?, ?)', self.parser.get_regions())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_regions())) + ' regions inserted')

    def add_all_departements(self):
        print(self.parser.get_departements()[0])
        self.c.executemany('INSERT INTO departement VALUES (?, ?, ?)', self.parser.get_departements())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_departements())) + ' departements inserted')

    def add_all_communes(self):
        self.c.executemany('INSERT INTO commune VALUES (?, ?, ?, ?)', self.parser.get_communes())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_communes())) + ' communes inserted')

    def print_regions(self):
        self.c.execute('SELECT * FROM region ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - ' + str(len(self.c.execute('SELECT * FROM region').fetchall())) + ' regions found')

    def print_departements(self):
        self.c.execute('SELECT * FROM departement ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - ' + str(len(self.c.execute('SELECT * FROM departement').fetchall())) + ' departements found')

    def print_communes(self):
        self.c.execute('SELECT * FROM commune ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - ' + str(len(self.c.execute('SELECT * FROM commune').fetchall())) + ' communes found')

    def close(self):
        self.db.close()


database = Database()
database.create_all()