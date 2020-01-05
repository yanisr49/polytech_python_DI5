import sqlite3

from pip._vendor.html5lib.treebuilders import etree

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
        self.create_table_new_region()
        self.create_table_departement()
        self.create_table_commune()
        self.add_all_regions()
        self.add_all_new_regions()
        self.add_all_departements()
        self.add_all_communes()
        self.print_regions()
        #self.print_new_regions()
        self.print_departements()
        #self.print_communes()
        #self.find_different_commune()

    def reset_tables(self):
        self.c.execute('''DROP TABLE IF EXISTS region''')
        self.c.execute('''DROP TABLE IF EXISTS departement''')
        self.c.execute('''DROP TABLE IF EXISTS commune''')
        self.c.execute('''DROP TABLE IF EXISTS newregion''')
        self.db.commit()

    def create_table_region(self):
        self.c.execute('''CREATE TABLE region (code_region text PRIMARY KEY, name text NOT NULL)''')
        print('log - Table region created')
        self.db.commit()

    def create_table_new_region(self):
        self.c.execute('''CREATE TABLE newregion (code_newregion text PRIMARY KEY, name text NOT NULL)''')
        print('log - Table newregion created')
        self.db.commit()

    def create_table_departement(self):
        self.c.execute(
            '''CREATE TABLE departement (code_departement text PRIMARY KEY, name text NOT NULL, code_region text, code_newregion text DEFAULT NULL, FOREIGN KEY(code_region) REFERENCES region(code_region), FOREIGN KEY(code_newregion) REFERENCES newregion(code_newregion))''')
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

    def add_all_new_regions(self):
        self.c.executemany('INSERT INTO newregion VALUES (?, ?)', self.parser.get_new_regions())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_new_regions())) + ' newregions inserted')

    def add_all_departements(self):
        self.c.executemany('INSERT INTO departement VALUES (?, ?, ?, ?)', self.parser.get_departements())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_departements())) + ' departements inserted')

    def add_all_communes(self):
        self.c.executemany('INSERT INTO commune VALUES (?, ?, ?, ?)', self.parser.get_communes())
        self.db.commit()
        print('log - ' + str(len(self.parser.get_communes())) + ' communes inserted')

    def get_regions(self):
        return self.c.execute('SELECT * FROM region ORDER BY name').fetchall()

    def get_departements(self):
        return self.c.execute('SELECT * FROM departement ORDER BY name').fetchall()

    def get_communes(self):
        return self.c.execute('SELECT * FROM commune ORDER BY name').fetchall()

    def print_regions(self):
        self.c.execute('SELECT * FROM region ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - ' + str(len(self.c.execute('SELECT * FROM region').fetchall())) + ' regions found')

    def print_new_regions(self):
        self.c.execute('SELECT * FROM newregion ORDER BY name')
        for row in self.c.fetchall():
            print(row)
        print('log - ' + str(len(self.c.execute('SELECT * FROM newregion').fetchall())) + ' newregions found')

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
        departementName = ""
        commune = ""
        for row in self.c.fetchall():
            if departementName != row[0]:
                print(departementName + " -- " + commune)
                departementName = row[0]
                commune = ""
                commune = commune + row[1]
                commune = commune + ", " + row[2]
            elif departementName == row[0]:
                commune = commune + ", " + row[2]
        print(departementName + " -- " + commune)

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

    def to_xml(self):
        regionsXML = etree.Element("regions")
        for region in self.c.execute('SELECT * FROM region ORDER BY name').fetchall():
            regionXML = etree.SubElement(regionsXML, "region")
            regionXML.set("region-id", region[0])
            etree.SubElement(regionXML, "nom").text = region[1]
            departementsXML = etree.SubElement(regionXML, "departements")
            for departement in self.c.execute('SELECT * FROM departement WHERE code_region = \'' + region[0] + '\'').fetchall():
                departementXML = etree.SubElement(departementsXML, "departement")
                departementXML.set("departement-id", departement[0])
                etree.SubElement(departementXML, "nom").text = departement[1]
                communesXML = etree.SubElement(departementXML, "communes")
                for commune in self.c.execute('SELECT * FROM commune WHERE code_departement = \'' + departement[0] + '\'').fetchall():
                    communeXML = etree.SubElement(communesXML, "commune")
                    communeXML.set("commune-id", commune[0])
                    etree.SubElement(communeXML, "nom").text = commune[1]
                    etree.SubElement(communeXML, "pop_tot").text = commune[2]

        f = open("bdds/save.xml", "w")
        f.write(etree.tostring(regionsXML, pretty_print=True).decode("utf-8"))
        f.close()

    def close(self):
        self.db.close()


with Database() as db:
    db.create_all()
    #db.pop_tot()
    #db.find_different_commune()
    db.to_xml()
