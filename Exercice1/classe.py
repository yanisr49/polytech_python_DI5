import datetime

class Date(object):
	# Class defining a date containing a day / month / year

	def __init__(self, day, month, year):
		# Constructor	
		
		self.year = year
		self.month = month
		self.day = day
		
	def __repr__(self):
		# print overload
		
		return_val = ""

		if self.day < 10:
			return_val += "0" + str(self.day) + "/"
		else:
			return_val += str(self.day) + "/"

		if self.month < 10:
			return_val += "0" + str(self.month) + "/"
		else:
			return_val += str(self.month) + "/"
		
		return return_val + str(self.year)
	
	def __eq__(self, value):
		# equals overload
		return self.day == value.day and self.month == value.month and self.year == value.year

	def __lt__(self, value):
		# lower than overload
		return value.year > self.year or (value.year == self.year and value.month > self.month) or (value.year == self.year and value.month == self.month and value.day > self.day)

	# Getters and Setters
	
	# attribut day
	def _get_day(self):
		return self._day
	def _set_day(self, day):
		if not isinstance(day, int) and not isinstance(day, str):
			raise TypeError("Le jour doit être un entier ou une chaine de caractère")
		day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
		if day_in_month[self.month-1] < int(day):
			raise ValueError("Date incorrecte")
			
		self._day = int(day)
		
	day = property(_get_day, _set_day)
	
	# attribut month
	def _get_month(self):
		return self._month
	def _set_month(self, month):
		if not isinstance(month, int) and not isinstance(month, str):
			raise TypeError("Le mois doit être un entier ou une chaine de caractère")
		
		if int(month) > 12:
			raise ValueError("Le mois ne peux pas dépasser 12")
			
		self._month = int(month)
		
	month = property(_get_month, _set_month)
	
	# attribut year
	def _get_year(self):
		return self._year
	def _set_year(self, year):
		if not isinstance(year, int) and not isinstance(year, str):
			raise TypeError("L'année doit être un entier ou une chaine de caractère")
			
		self._year = int(year)
		
	year = property(_get_year, _set_year)


class Etudiant(object):
	""" Classe defining un étudiant, elle est composé d'nom, d'un prénom,et d'une date de naissance
	"""
	
	def __init__(self, lastname, firstname, birthdate):
		# Constructor
		
		self.lastname = lastname
		self.firstname = firstname
		self.birthdate = birthdate

	def __repr__(self):
		# print overload
		return "\nEtudiant : {} {} a {} ans.\nMail : {}".format(self.lastname, self.firstname, self.age(), self.adresselec())
	
	def age(self):
		# Get the age if the student
		now = datetime.datetime.now()
		if Date(now.day, now.month, self.birthdate.year) < self.birthdate:
			return now.year - self.birthdate.year - 1
		else:
			return now.year - self.birthdate.year
	
	def adresselec(self):
		return "{}.{}@etu.univ-tours.fr".format(self.firstname.lower(), self.lastname.lower())
	
	# Getters and Setters
	
	# attribute lastname
	def _get_lastname(self):
		return self._lastname
	def _set_lastname(self, lastname):
		if not isinstance(lastname, str):
			raise TypeError("Une chaine de caractère est attendue")
		self._lastname = lastname
	lastname = property(_get_lastname, _set_lastname)
	
	# attribute firstname
	def _get_firstname(self):
		return self._firstname
	def _set_firstname(self, firstname):
		if not isinstance(firstname, str):
			raise TypeError("Une chaine de caractère est attendue")
		self._firstname = firstname
	firstname = property(_get_firstname, _set_firstname)
	
	# attribute birthdate
	def _get_birthdate(self):
		return self._birthdate
	def _set_birthdate(self, birthdate):
		if not isinstance(birthdate, Date):
			raise TypeError("Une Date est attendue")
		self._birthdate = birthdate
	birthdate = property(_get_birthdate, _set_birthdate)
	
	
	
