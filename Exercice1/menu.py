#TP 1

#Question 1
print("Hello world !")

#Question 2
resume = True
filename = ""
text = ""
fil = None

while(resume):
	choice = input("\n1. Choisir un nom de fichier\n2. Ajouter un texte\n3. Afficher le fichier complet\n4. Vider le fichier\n9. Quitter le programme\n=> ")

	if choice == "1":
		filename = input("Nom de fichier ? (exemple.txt)\n=> ")
		fil = open(filename, "x")
	elif choice == "2":
		if filename != "":
			with open(filename, "a") as fil:
				fil.write(input("Rajouter du texte au fichier\n=> "))
		else:
			print("Vous devez préciser le nom du fichier avant d'écrire !")
	elif choice == "3":
		if filename != "":
			with open(filename, "r") as fil:
				print(fil.read())
		else:
			print("Vous devez préciser le nom du fichier avant de le lire !")
	elif choice == "4":
		if filename != "":
			open(filename, "w")
		else:
			print("Vous devez préciser le nom du fichier avant de le vider !")
	elif choice == "9":
		resume = False
	else:
		print("command inconnue")

	if fil != None:
		fil.close()
