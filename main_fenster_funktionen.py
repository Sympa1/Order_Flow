import sqlite3
from tkinter import END


def kunde_suchen(kundennummer_entry, anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry,
				  stadt_entry, telefon_entry, mobil_entry, mail_entry):
	"""Diese Funktion sucht anhand der Kundennummer den jeweiligen Kunden und ggf. später die dem Kunden zugeordneten Aufträge
	raus."""
	kundennummer = int(kundennummer_entry.get())
	# Die Verbindung mit der Datenbank herstellen
	verbindung = sqlite3.connect("data.db")

	# "der_curser" führt z.B. SQL Abfragen aus
	der_cursor = verbindung.cursor()

	# SQL Abfrage
	query = "SELECT Kunden.Anrede, Kunden.Vorname, Kunden.Nachname, Kunden.Strasse, Kunden.Hausnummer, Kunden.PLZ, " \
			"Kunden.Stadt, Kontaktdaten.Telefonnummer, Kontaktdaten.Mobil, Kontaktdaten.Mail FROM Kunden INNER JOIN " \
			"Kontaktdaten ON Kunden.KontaktID = Kontaktdaten.ID WHERE Kunden.ID = ?"

	# SQL-Abfrage ausführen
	der_cursor.execute(query, (kundennummer,))

	# Kundendaten abrufen und als Tupel in der Variable "result" speichern
	result = der_cursor.fetchone()

	# Verbindung schließen
	verbindung.close()

	# Überprüfung, ob "result" leer ist
	if result is not None:
		# Jeder Wert des Tupels wird in einer separaten Variable gespeichert und an das passende Entry übergeben. Wichtig ist
		# die Reihenfolge.
		anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail = result
		print(anrede, vorname, nachname, strasse, hausnummer, plz, stadt, telefon, mobil, mail)
		anrede_combobox.set(anrede)
		vorname_entry.delete(0, END)
		vorname_entry.insert(0, vorname)
		nachname_entry.delete(0, END)
		nachname_entry.insert(0, nachname)
		strasse_entry.delete(0, END)
		strasse_entry.insert(0, strasse)
		hausnummer_entry.delete(0, END)
		hausnummer_entry.insert(0, hausnummer)
		plz_entry.delete(0, END)
		plz_entry.insert(0, plz)
		stadt_entry.delete(0, END)
		stadt_entry.insert(0, stadt)
		telefon_entry.delete(0, END)
		telefon_entry.insert(0, telefon)
		mobil_entry.delete(0, END)
		mobil_entry.insert(0, mobil)
		mail_entry.delete(0, END)
		mail_entry.insert(0, mail)
	else:
		kundennummer_entry.delete(0, END)
		kundennummer_entry.insert(0, str(kundennummer) + " ist keine bekannte Kundennummer!")
		anrede_combobox.set("")
		vorname_entry.delete(0, END)
		nachname_entry.delete(0, END)
		strasse_entry.delete(0, END)
		hausnummer_entry.delete(0, END)
		plz_entry.delete(0, END)
		stadt_entry.delete(0, END)
		telefon_entry.delete(0, END)
		mobil_entry.delete(0, END)
		mail_entry.delete(0, END)



def kunde_aendern(kundennummer_entry, anrede_combobox, vorname_entry, nachname_entry, strasse_entry, hausnummer_entry, plz_entry,
				  stadt_entry, telefon_entry, mobil_entry, mail_entry):
	"""Diese Funktion speichert die eingetragenen Änderungen der Kunden Stammdaten. Ggf. macht ein Bestätigung "Alert"
	Pop-up-Fenster sinn?"""
	print("HI")
