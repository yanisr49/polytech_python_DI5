import sqlite3
from Exercice5.CSVParser import *


class Database(object):

    def __init__(self):
        self.db = sqlite3.connect('bdds/mydb.db')
        print('log - Connected to the database')
        self.c = self.db.cursor()
        self.parser = Parser()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

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
        self.find_different_commune()

    def reset_tables(self):
        self.c.execute('''DROP TABLE IF EXISTS region''')
        self.c.execute('''DROP TABLE IF EXISTS departement''')
        self.c.execute('''DROP TABLE IF EXISTS commune''')
        self.db.commit()

    def create_table_region(self):
        self.c.execute('''CREATE TABLE region (code_region text PRIMARY KEY, name text NOT NULL)''')
        print('log - Table region created')
        self.db.commit()

    def create_table_departement(self):
        self.c.execute(
            '''CREATE TABLE departement (code_departement text PRIMARY KEY, name text NOT NULL, code_region text, FOREIGN KEY(code_region) REFERENCES region(code_region))''')
        print('log - Table departement created')
        self.db.commit()

    def create_table_commune(self):
        self.c.execute(
            '''CREATE TABLE commune (code_commune text, name text NOT NULL, pop_tot text,code_departement text, FOREIGN KEY(code_departement)REFERENCES departement(code_departement))''')
        print('log - Table commune created')
        self.db.commit()

    def add_all_regions(self):
        self.c.executemany('INSERT INTO region VALUES (?, ?)', self.parser.get_regions())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_regions())) + ' regions inserted')

    def add_all_departements(self):
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

    def find_different_commune(self):
        self.c.execute('SELECT comu.name, comu.code_departement, com.code_departement FROM commune comu INNER JOIN commune com ON com.name = comu.name WHERE com.code_departement <> comu.code_departement')
        '''commuName = ""
        for row in self.c.fetchall():
            if commuName == "":
                commuName = row[0]
            elif commuName == row[0]:
                commuName += row[]
            print(row)'''

    def pop_tot(self):
        dep_pop_tot = []
        self.c.execute('SELECT d.name, c.pop_tot from departement d INNER JOIN commune c ON d.code_departement = c.code_departement ORDER BY d.name')
        for row in self.c.fetchall():
            if len(dep_pop_tot) > 0:
                if row[0] == dep_pop_tot[-1][0]:
                    dep_pop_tot[-1][1] = dep_pop_tot[-1][1] + int(row[1].replace(" ", ""))
                else:
                    dep_pop_tot.append([row[0], int(row[1].replace(" ", ""))])
            else:
                dep_pop_tot.append([row[0], int(row[1].replace(" ", ""))])

        reg_pop = []
        self.c.execute('SELECT r.name, d.name FROM region r INNER JOIN departement d ON r.code_region = d.code_region ORDER BY r.name')
        for row in self.c.fetchall():
            if len(reg_pop) > 0:
                if row[0] == reg_pop[-1][0]:
                    reg_pop[-1][1] = reg_pop[-1][1] + self.get_pop_from_dep(dep_pop_tot, row[1])
                else:
                    reg_pop.append([row[0], self.get_pop_from_dep(dep_pop_tot, row[1])])
            else:
                reg_pop.append([row[0], self.get_pop_from_dep(dep_pop_tot, row[1])])

        for row in dep_pop_tot:
            print(row[0] + " à une population de " + str(row[1]))
        for row in reg_pop:
            print(row[0] + " à une population de " + str(row[1]))

    def get_pop_from_dep(self, departements, departement):
        for row in departements:
            if row[0] == departement:
                return row[1]
        return 0

    def close(self):
        self.db.close()


with Database() as db:
    db.create_all()
    db.pop_tot()
