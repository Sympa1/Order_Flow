import sqlite3


def kunde_suchen(kundennummer_entry):
	"""Diese Funktion sucht anhand der Kundennummer die jeweiligen Kunden und ggf. später die dem Kunden zugeordneten Aufträge
	raus. """
	print("HI")
	# Die Verbindung mit der Datenbank herstellen
	verbindung = sqlite3.connect("data.db")

	# "der_curser" führt z.B. SQL Abfragen aus
	der_cursor = verbindung.cursor()

	# SQL Abfrage
	query = "SELECT * FROM Kunden WHERE ID = ?"

	# SQL-Abfrage ausführen
	der_cursor.execute(query, (kundennummer_entry,))

	# Ergebnis abrufen
	result = der_cursor.fetchone()

	# Verbindung schließen
	verbindung.close()

	print(result)


def kunde_aendern(anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry,
				  stadt_entry, telefon_entry, mobil_entry, mail_entry):
	"""Diese Funktion speichert die eingetragenen Änderungen der Kunden Stammdaten. Ggf. macht ein Bestätigung "Alert"
	Pop-up-Fenster sinn?"""
	print("HI")
